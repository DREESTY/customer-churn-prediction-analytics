# Customer Churn Prediction & Retention Analytics

An end-to-end data analytics and machine learning project that identifies customer churn drivers, predicts churn risk, segments customers, and translates model outputs into retention strategies through Power BI.

## Business Problem

Customer churn reduces recurring revenue and increases the pressure to acquire replacement customers. The goal of this project is to answer:

1. Which customer characteristics are associated with churn?
2. Which customers have the highest predicted churn risk?
3. Which customer segments should a retention team prioritize?
4. What retention action can be associated with each risk/segment?

## Tech Stack

- Python
- Pandas / NumPy
- Scikit-learn
- Matplotlib / Seaborn
- SQL
- Power BI + DAX
- Git / GitHub

## Dataset

This project uses the IBM Telco Customer Churn dataset containing 7,043 customer records and 21 columns. The target is `Churn` (Yes/No).

Download the dataset and place it at:

`data/raw/Telco-Customer-Churn.csv`

A public IBM repository provides the same dataset and sample workflow:
https://github.com/IBM/telco-customer-churn-on-icp4d

An alternative Kaggle listing is:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

## Project Workflow

Raw data
→ cleaning
→ exploratory analysis
→ feature engineering
→ train/test split
→ classification models
→ model evaluation
→ customer churn probability
→ risk segmentation
→ retention strategy mapping
→ Power BI dashboard

## Folder Structure

```text
Customer-Churn-Prediction/
│
├── data/
│   ├── raw/
│   │   └── Telco-Customer-Churn.csv
│   └── processed/
│       └── churn_scored_customers.csv
│
├── models/
│   └── churn_model.joblib
│
├── notebooks/
│   └── Customer_Churn_Analysis.ipynb
│
├── outputs/
│   └── figures/
│
├── powerbi/
│   └── POWER_BI_BUILD_GUIDE.md
│
├── sql/
│   └── churn_analysis.sql
│
├── src/
│   ├── train_model.py
│   └── make_eda.py
│
├── docs/
│   └── DATA_DICTIONARY.md
│
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone <your-repository-url>
cd Customer-Churn-Prediction

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
```

Then place the CSV in `data/raw/`.

## Run the Project

### 1. Generate EDA figures

```bash
python src/make_eda.py
```

### 2. Train the model and score customers

```bash
python src/train_model.py
```

The script creates:

- model evaluation metrics
- confusion matrix
- ROC curve
- feature importance
- `data/processed/churn_scored_customers.csv`
- `models/churn_model.joblib`

## Important: Do Not Fabricate Metrics

After running the pipeline, copy the actual Accuracy, Precision, Recall, F1 and ROC-AUC values into the final report/README. Do not use example metrics from another repository.

## Power BI

Open Power BI Desktop and import:

`data/processed/churn_scored_customers.csv`

Build the three pages described in:

`powerbi/POWER_BI_BUILD_GUIDE.md`

Recommended pages:

1. Churn Overview
2. High-Risk Customers
3. Retention Strategy

## Key Business Outputs

The final dashboard should make it possible to identify:

- overall churn rate
- churn by contract type
- churn by tenure
- churn by internet service
- churn by payment method
- high-risk customers
- high-value customers at risk
- expected monthly revenue exposure
- recommended retention action

## Limitations

- This is a public historical dataset, not live customer data.
- Churn predictions indicate statistical risk, not causal reasons for leaving.
- The dataset does not contain every real-world retention signal such as detailed complaints, call-center history or customer satisfaction.
- Retention recommendations are business rules layered on top of model outputs and should be validated experimentally.

## Resume Version

**Customer Churn Prediction & Retention Analytics | Python, SQL, Scikit-learn, Power BI**
- Analyzed customer behavioral and demographic data to identify churn drivers and high-risk segments.
- Built a classification pipeline to predict customer churn risk and translated model outputs into customer segmentation and retention strategies through an interactive Power BI dashboard.

Replace/add quantified results only after you run the model and have verified the metrics.
