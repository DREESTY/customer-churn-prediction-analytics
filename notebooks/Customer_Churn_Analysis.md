# Customer Churn Analysis Notebook Guide

Use this as the narrative structure for your Jupyter notebook.

## 1. Business Objective

Predict which customers are likely to churn and identify customer segments that deserve retention attention.

## 2. Import Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

## 3. Load Data

```python
df = pd.read_csv("../data/raw/Telco-Customer-Churn.csv")
df.head()
df.shape
df.info()
```

## 4. Data Cleaning

```python
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.isna().sum()
df = df.dropna(subset=["TotalCharges"])
```

Explain why `TotalCharges` needs conversion and why missing values are handled before modeling.

## 5. Exploratory Data Analysis

Analyze:
- churn distribution
- contract type
- tenure
- monthly charges
- internet service
- payment method
- senior citizen status
- partner/dependents

For each chart, write one factual observation based on the actual result.

## 6. Feature Engineering

Create:
- ChurnFlag
- tenure bands
- optional service-count features
- model-ready numerical/categorical feature groups

Do not create features using information that would only become available after the customer has already churned.

## 7. Train/Test Split

Use stratification because churn is the minority class.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
```

## 8. Models

Train:
- Logistic Regression as an interpretable baseline
- Random Forest as a nonlinear tree-based model

Compare:
- Accuracy
- Precision
- Recall
- F1
- ROC-AUC

For churn detection, discuss recall because missing a genuinely at-risk customer may reduce the value of a retention system.

## 9. Customer Risk Scoring

Use predicted probability rather than only the Yes/No prediction.

Risk bands:
- High: probability >= 0.70
- Medium: 0.40–0.69
- Low: < 0.40

These thresholds are project rules and can be changed based on business costs.

## 10. Customer Segmentation

Combine:
- churn probability
- monthly charges
- tenure
- contract
- service characteristics

Create a practical retention segment.

## 11. Business Translation

Example logic:

High risk + high value → priority retention outreach

High risk → retention offer and service/support review

Medium risk → targeted engagement

Low risk → loyalty communication

Do not claim these actions were proven to reduce churn unless you have experimental evidence.

## 12. Power BI

Export the scored customer table and build the three-page dashboard described in `powerbi/POWER_BI_BUILD_GUIDE.md`.

## 13. Conclusion

Your conclusion should contain:
- actual model performance
- top observed churn patterns
- size of high-risk population
- revenue exposure
- recommended analytical retention priorities
- limitations
