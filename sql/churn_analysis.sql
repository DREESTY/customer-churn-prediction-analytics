-- Customer Churn SQL Analysis
-- Load the cleaned/scored CSV into a table named customer_churn.

-- 1. Overall customer count and churn rate
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_pct
FROM customer_churn;

-- 2. Churn by contract
SELECT
    Contract,
    COUNT(*) AS customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS churned,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_pct
FROM customer_churn
GROUP BY Contract
ORDER BY churn_rate_pct DESC;

-- 3. Churn by tenure band
SELECT
    CASE
        WHEN tenure < 12 THEN '0-11 months'
        WHEN tenure < 24 THEN '12-23 months'
        WHEN tenure < 48 THEN '24-47 months'
        ELSE '48+ months'
    END AS tenure_band,
    COUNT(*) AS customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_pct
FROM customer_churn
GROUP BY tenure_band
ORDER BY churn_rate_pct DESC;

-- 4. High-risk customers
SELECT
    customerID,
    ChurnProbability,
    RiskBand,
    MonthlyCharges,
    ExpectedMonthlyRevenueAtRisk,
    RetentionAction
FROM customer_churn
WHERE RiskBand = 'High'
ORDER BY ChurnProbability DESC;

-- 5. High-risk + high-value customers
SELECT
    customerID,
    ChurnProbability,
    MonthlyCharges,
    ExpectedMonthlyRevenueAtRisk,
    RetentionAction
FROM customer_churn
WHERE RiskBand = 'High'
  AND CustomerValueBand = 'High Value'
ORDER BY ExpectedMonthlyRevenueAtRisk DESC;
