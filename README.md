# Customer Churn Prediction & Retention Analytics

An end-to-end **Data Analytics, Machine Learning, SQL, and Business Intelligence project** that analyzes customer churn, identifies key churn drivers, predicts individual customer churn probability, segments customers based on retention risk and customer value, estimates revenue exposure, and translates analytical results into actionable retention strategies.

The project follows a complete analytics workflow:

**Raw Data → Data Cleaning → Exploratory Analysis → Machine Learning → Customer Risk Scoring → SQL Analytics → Power BI → Retention Strategy → Executive Recommendations**

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Business Problem](#-business-problem)
- [Business Objectives](#-business-objectives)
- [Project Approach](#-project-approach)
- [Dataset](#-dataset)
- [Data Preparation](#-data-preparation)
- [Exploratory Data Analysis](#-exploratory-data-analysis)
- [Machine Learning](#-machine-learning)
- [Customer Risk Segmentation](#-customer-risk-segmentation)
- [Customer Value Segmentation](#-customer-value-segmentation)
- [SQL Analytics](#-sql-analytics)
- [Power BI Dashboard](#-power-bi-dashboard)
  - [Page 1 - Customer Churn & Retention Analytics](#page-1---customer-churn--retention-analytics)
  - <img width="1206" height="680" alt="Screenshot 2026-10-03 203241" src="https://github.com/user-attachments/assets/df04e30c-0028-4e4c-9a18-e3821bc7a3f6" />

  - [Page 2 - Customer Risk Analysis](#page-2---customer-risk-analysis)
  - <img width="1207" height="676" alt="Screenshot 2026-10-03 203320" src="https://github.com/user-attachments/assets/a42fcfc7-3675-47ce-a878-321acad944d9" />

  - [Page 3 - Customer Retention Strategy](#page-3---customer-retention-strategy)
  - <img width="1444" height="811" alt="Screenshot 2026-10-03 203405" src="https://github.com/user-attachments/assets/94d287d3-77f3-4d81-a553-5fb5e5a133b1" />

  - [Page 4 - Executive Recommendations](#page-4---executive-recommendations)
  - <img width="1441" height="815" alt="Screenshot 2026-10-03 203435" src="https://github.com/user-attachments/assets/edf99867-624f-435f-8a6a-5f13598d8d7f" />

- [End-to-End Business Flow](#-end-to-end-business-flow)
- [Key Business Insights](#-key-business-insights)
- [Project Structure](#-project-structure)
- [Setup](#-setup)
- [Running the Project](#-running-the-project)
- [Power BI Report](#-power-bi-report)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Resume Version](#-resume-version)

---

# 📌 Project Overview

Customer churn is an important business problem because losing existing customers can reduce recurring revenue and increase the cost of acquiring replacement customers.

This project develops an end-to-end customer churn analytics solution using the **IBM Telco Customer Churn dataset**.

Instead of stopping at simply predicting whether a customer will churn, the project extends the analysis into a business-oriented retention framework.

The project:

1. Analyzes historical customer behavior.
2. Identifies patterns associated with customer churn.
3. Builds machine learning models to predict customer churn probability.
4. Generates an individual churn probability for each customer.
5. Segments customers into Low, Medium, and High risk bands.
6. Combines churn risk with customer value.
7. Identifies high-risk and high-value customers.
8. Estimates potential revenue exposure.
9. Uses SQL to generate business-level analytical metrics.
10. Builds an interactive four-page Power BI dashboard.
11. Maps customer segments to retention actions.
12. Summarizes the analysis into executive-level recommendations.

The final solution connects **technical machine learning outputs with business decision-making**.

---

# 💼 Business Problem

A telecommunications company may have thousands of customers, but not every customer has the same probability of leaving.

A useful churn analytics system should therefore answer more than:

> "Who is going to churn?"

It should also help answer:

- Why are certain customer groups experiencing higher churn?
- Which customers have elevated predicted churn probability?
- Which high-risk customers have greater customer value?
- How much revenue is associated with customers at risk?
- Which customers should receive different types of retention attention?
- What patterns should business teams investigate further?

This project addresses these questions by combining **descriptive analytics, predictive analytics, segmentation, and business intelligence**.

---

# 🎯 Business Objectives

The project was designed around the following objectives:

### 1. Understand Customer Churn

Analyze historical churn patterns across:

- Contract type
- Tenure
- Internet service
- Payment method
- Monthly charges
- Customer characteristics

### 2. Predict Customer Churn

Build classification models that estimate the probability of a customer churning.

### 3. Identify High-Risk Customers

Use predicted churn probabilities to classify customers into different risk segments.

### 4. Incorporate Customer Value

Combine churn risk with customer value so that retention analysis considers both:

- Probability of churn
- Potential business value

### 5. Estimate Revenue Exposure

Estimate the amount of revenue associated with high-risk customers.

### 6. Develop Retention Strategies

Map different customer risk/value segments to potential retention actions.

### 7. Communicate Insights

Create a Power BI dashboard that allows business users to understand:

- What is happening?
- Which customers are at risk?
- Which segments require attention?
- What actions could be considered?

---

# 🔄 Project Approach

The complete project follows the pipeline below:

```text
                    RAW CUSTOMER DATA
                           │
                           ▼
                DATA CLEANING & PREPARATION
                           │
                           ▼
                EXPLORATORY DATA ANALYSIS
                           │
                           ▼
                  FEATURE ENGINEERING
                           │
                           ▼
                  MACHINE LEARNING
                           │
                           ▼
              CUSTOMER CHURN PROBABILITY
                           │
                           ▼
                  RISK SEGMENTATION
                           │
                           ▼
                CUSTOMER VALUE BANDING
                           │
                           ▼
                    SQL ANALYTICS
                           │
                           ▼
                  POWER BI DASHBOARD
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        CHURN OVERVIEW   CUSTOMER     RETENTION
                          RISK         STRATEGY
              │
              ▼
        EXECUTIVE RECOMMENDATIONS
