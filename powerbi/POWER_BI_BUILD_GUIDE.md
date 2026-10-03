# Power BI Build Guide

## 1. Load Data

Open Power BI Desktop.

Get Data → Text/CSV → select:

`data/processed/churn_scored_customers.csv`

Load the table as `ChurnCustomers`.

## 2. Create Core Measures

Create these DAX measures:

```DAX
Total Customers =
COUNTROWS(ChurnCustomers)
```

```DAX
Churned Customers =
CALCULATE(
    COUNTROWS(ChurnCustomers),
    ChurnCustomers[Churn] = "Yes"
)
```

```DAX
Churn Rate =
DIVIDE([Churned Customers], [Total Customers], 0)
```

```DAX
Active Customers =
[Total Customers] - [Churned Customers]
```

```DAX
Average Monthly Charge =
AVERAGE(ChurnCustomers[MonthlyCharges])
```

```DAX
Expected Revenue at Risk =
SUM(ChurnCustomers[ExpectedMonthlyRevenueAtRisk])
```

```DAX
High Risk Customers =
CALCULATE(
    COUNTROWS(ChurnCustomers),
    ChurnCustomers[RiskBand] = "High"
)
```

```DAX
High Risk Revenue =
CALCULATE(
    SUM(ChurnCustomers[MonthlyCharges]),
    ChurnCustomers[RiskBand] = "High"
)
```

## Page 1 — Churn Overview

### KPI cards
- Total Customers
- Churned Customers
- Churn Rate
- High Risk Customers
- Expected Revenue at Risk

### Charts
1. Churn Rate by Contract — clustered column chart
2. Churn Rate by Internet Service — column chart
3. Churn Rate by Payment Method — bar chart
4. Churn Distribution — donut chart
5. Tenure vs Churn — column chart using a tenure band
6. Monthly Charges vs Churn — box plot if available, otherwise column/bar aggregation

### Slicers
- Contract
- InternetService
- PaymentMethod
- SeniorCitizen
- Partner
- Dependents

## Page 2 — High-Risk Customers

Add a table with:

- customerID
- ChurnProbability
- RiskBand
- CustomerValueBand
- Contract
- tenure
- MonthlyCharges
- InternetService
- ExpectedMonthlyRevenueAtRisk
- RetentionAction

Add a visual filter:

`RiskBand = High`

Sort by:

`ExpectedMonthlyRevenueAtRisk` descending.

Add a scatter chart:
- X = MonthlyCharges
- Y = ChurnProbability
- Legend = RiskBand
- Size = ExpectedMonthlyRevenueAtRisk

This creates the business-prioritization view.

## Page 3 — Retention Strategy

### Visual 1
Retention Action by Customer Count

### Visual 2
Expected Revenue at Risk by Retention Action

### Visual 3
Risk Band by Contract

### Visual 4
Customer Value Band by Risk Band

### Strategy table

| Segment | Example Action |
|---|---|
| High Risk + High Value | Priority save offer + proactive support |
| High Risk + Mid/Standard Value | Retention offer + service/support outreach |
| Medium Risk | Targeted engagement + plan review |
| Low Risk | Loyalty communication |

These are analytical business rules for the portfolio project, not claims that a specific intervention will definitely prevent churn.

## Dashboard Design

Use a clean consulting/analytics style:

- white/light background
- one accent color
- consistent typography
- KPI cards at the top
- charts below
- slicers in a single horizontal or vertical area
- avoid excessive pie charts
- keep the dashboard focused on decisions rather than decoration

## Screenshots to Export

Save screenshots as:

```text
docs/
├── dashboard_overview.png
├── high_risk_customers.png
└── retention_strategy.png
```

Then embed them in the GitHub README.
