from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "raw" / "Telco-Customer-Churn.csv"
OUT = ROOT / "outputs" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA)
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["ChurnFlag"] = (df["Churn"] == "Yes").astype(int)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(7,5))
sns.countplot(data=df, x="Churn")
plt.title("Customer Churn Distribution")
plt.tight_layout()
plt.savefig(OUT / "01_churn_distribution.png", dpi=180)
plt.close()

contract = pd.crosstab(df["Contract"], df["Churn"], normalize="index") * 100
contract.plot(kind="bar", figsize=(8,5))
plt.ylabel("Percentage of customers")
plt.title("Churn by Contract Type")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "02_churn_by_contract.png", dpi=180)
plt.close()

plt.figure(figsize=(8,5))
sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
plt.title("Monthly Charges vs Churn")
plt.tight_layout()
plt.savefig(OUT / "03_monthly_charges.png", dpi=180)
plt.close()

plt.figure(figsize=(8,5))
sns.histplot(data=df, x="tenure", hue="Churn", bins=30, kde=True, element="step")
plt.title("Tenure Distribution by Churn")
plt.tight_layout()
plt.savefig(OUT / "04_tenure.png", dpi=180)
plt.close()

internet = pd.crosstab(df["InternetService"], df["Churn"], normalize="index") * 100
internet.plot(kind="bar", figsize=(8,5))
plt.ylabel("Percentage of customers")
plt.title("Churn by Internet Service")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUT / "05_internet_service.png", dpi=180)
plt.close()

print(f"Saved EDA figures to {OUT}")
