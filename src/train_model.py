from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from xgboost import XGBClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, ConfusionMatrixDisplay, RocCurveDisplay
)

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "Telco-Customer-Churn.csv"
PROCESSED = ROOT / "data" / "processed"
MODELS = ROOT / "models"
FIGURES = ROOT / "outputs" / "figures"

for p in [PROCESSED, MODELS, FIGURES]:
    p.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)

# Cleaning
df = df.drop(columns=["customerID"])
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna(subset=["TotalCharges"])

# Target
y = (df["Churn"] == "Yes").astype(int)
X = df.drop(columns=["Churn"])

# Identify feature groups
categorical = X.select_dtypes(include=["object", "string"]).columns.tolist()
numeric = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

numeric_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("onehot", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_pipe, numeric),
    ("cat", categorical_pipe, categorical)
])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

models = {
    "Logistic Regression": LogisticRegression(
        max_iter=2000,
        class_weight=None
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=500,
        max_depth=8,
        min_samples_leaf=2,
        random_state=42,
        class_weight=None,
        n_jobs=-1
    ),

    "XGBoost": XGBClassifier(
        n_estimators=500,
        max_depth=4,
        learning_rate=0.03,
        subsample=0.85,
        colsample_bytree=0.85,
        min_child_weight=3,
        reg_lambda=2,
        reg_alpha=0.1,
        objective="binary:logistic",
        eval_metric="logloss",
        random_state=42,
        n_jobs=-1
    )
}

results = []
fitted = {}

for name, model in models.items():
    pipe = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])
    pipe.fit(X_train, y_train)

    pred = pipe.predict(X_test)
    prob = pipe.predict_proba(X_test)[:, 1]

    metrics = {
        "model": name,
        "accuracy": accuracy_score(y_test, pred),
        "precision": precision_score(y_test, pred, zero_division=0),
        "recall": recall_score(y_test, pred, zero_division=0),
        "f1": f1_score(y_test, pred, zero_division=0),
        "roc_auc": roc_auc_score(y_test, prob)
    }
    results.append(metrics)
    fitted[name] = pipe

metrics_df = pd.DataFrame(results).sort_values("roc_auc", ascending=False)
metrics_df.to_csv(PROCESSED / "model_metrics.csv", index=False)

best_name = metrics_df.iloc[0]["model"]
best_model = fitted[best_name]
joblib.dump(best_model, MODELS / "churn_model.joblib")

# Evaluate best model
best_pred = best_model.predict(X_test)
best_prob = best_model.predict_proba(X_test)[:, 1]

ConfusionMatrixDisplay.from_predictions(y_test, best_pred)
plt.title(f"Confusion Matrix - {best_name}")
plt.tight_layout()
plt.savefig(FIGURES / "06_confusion_matrix.png", dpi=180)
plt.close()

RocCurveDisplay.from_predictions(y_test, best_prob)
plt.title(f"ROC Curve - {best_name}")
plt.tight_layout()
plt.savefig(FIGURES / "07_roc_curve.png", dpi=180)
plt.close()

# Score all original customers
# The model pipeline contains an imputer, so it can handle missing
# TotalCharges values in the original dataset.

scored = pd.read_csv(DATA)

# Make TotalCharges numeric in the same way as training
scored["TotalCharges"] = pd.to_numeric(
    scored["TotalCharges"],
    errors="coerce"
)

# Prepare features exactly as used during training
score_input = scored.drop(
    columns=["customerID", "Churn"]
)

# Predict churn probability for ALL original customers
risk_prob = best_model.predict_proba(score_input)[:, 1]

scored["ChurnProbability"] = risk_prob

def risk_band(p):
    if p >= 0.70:
        return "High"
    if p >= 0.40:
        return "Medium"
    return "Low"

scored["RiskBand"] = scored["ChurnProbability"].apply(risk_band)

def value_band(row):
    if row["MonthlyCharges"] >= scored["MonthlyCharges"].quantile(0.75):
        return "High Value"
    elif row["MonthlyCharges"] >= scored["MonthlyCharges"].quantile(0.50):
        return "Mid Value"
    return "Standard Value"

scored["CustomerValueBand"] = scored.apply(value_band, axis=1)

def retention_action(row):
    if row["RiskBand"] == "High" and row["CustomerValueBand"] == "High Value":
        return "Priority save offer + proactive support"
    if row["RiskBand"] == "High":
        return "Retention offer + service/support outreach"
    if row["RiskBand"] == "Medium":
        return "Targeted engagement + plan review"
    return "Loyalty communication"

scored["RetentionAction"] = scored.apply(retention_action, axis=1)

scored["ExpectedMonthlyRevenueAtRisk"] = (
    scored["MonthlyCharges"] * scored["ChurnProbability"]
)

scored.to_csv(PROCESSED / "churn_scored_customers.csv", index=False)

summary = {
    "best_model": best_name,
    "rows_used_for_modeling": int(len(df)),
    "test_rows": int(len(X_test)),
    "metrics": metrics_df.iloc[0].to_dict()
}
with open(PROCESSED / "run_summary.json", "w") as f:
    json.dump(summary, f, indent=2, default=str)

print("\nModel comparison:")
print(metrics_df.to_string(index=False))
print(f"\nBest model: {best_name}")
print(f"Scored customer file: {PROCESSED / 'churn_scored_customers.csv'}")
