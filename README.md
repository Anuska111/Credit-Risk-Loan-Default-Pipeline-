# 💳 Credit Risk & Loan Default Prediction Pipeline

> **A Production-Ready Machine Learning Pipeline for Predicting Loan Default Risk**

This project develops an end-to-end Credit Risk Prediction Pipeline that automatically preprocesses raw banking data, trains a machine learning model, optimizes hyperparameters, and predicts whether a loan applicant is likely to default. The project follows industry-standard machine learning practices using **Scikit-Learn Pipelines** to prevent data leakage and ensure reproducibility.

---

# 📌 Problem Statement

Financial institutions receive thousands of loan applications every day. Approving loans for high-risk customers can lead to significant financial losses, while rejecting reliable customers reduces business opportunities.

The objective of this project is to build a robust machine learning pipeline capable of accurately identifying potential loan defaulters using customer demographic, financial, and credit history information.

---

# 🎯 Project Objectives

- Predict whether a customer will default on a loan.
- Build a production-ready preprocessing pipeline.
- Prevent data leakage using Scikit-Learn Pipelines.
- Automatically optimize model performance using GridSearchCV.
- Evaluate the model using metrics suitable for imbalanced datasets.
- Generate business insights for better loan approval decisions.

---

# 📂 Dataset

The dataset contains customer financial and credit information, including:

- Customer Age
- Annual Income
- Employment Length
- Home Ownership
- Loan Amount
- Loan Intent
- Loan Grade
- Interest Rate
- Loan Percent Income
- Previous Loan Default History
- Credit History Length

**Target Variable**

- **Loan Status**
  - 0 → Non-Default
  - 1 → Default

---

# 🛠 Tech Stack

## Programming Language

- Python

## Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn

## Machine Learning

- Scikit-Learn
- Random Forest Classifier
- Pipeline
- ColumnTransformer
- SimpleImputer
- StandardScaler
- OneHotEncoder
- GridSearchCV

## Model Persistence

- Joblib

---

# 📊 Exploratory Data Analysis

The project includes comprehensive EDA to understand customer behavior and loan characteristics.

Performed analysis includes:

- Dataset Overview
- Missing Value Analysis
- Duplicate Check
- Statistical Summary
- Target Variable Distribution
- Numerical Feature Analysis
- Correlation Analysis
- Feature Importance Analysis

---

# ⚙️ Data Preprocessing Pipeline

The preprocessing pipeline automatically performs:

- Missing Value Imputation
- Numerical Feature Scaling
- Categorical Feature Encoding
- Column Transformation
- Feature Engineering Pipeline
- Data Leakage Prevention

Pipeline Flow

```
Raw Data
     │
     ▼
Missing Value Imputation
     │
     ▼
Feature Scaling
     │
     ▼
One-Hot Encoding
     │
     ▼
ColumnTransformer
     │
     ▼
Random Forest Classifier
```

---

# 🤖 Machine Learning Model

The project uses:

**Random Forest Classifier**

Reasons for selection:

- Handles nonlinear relationships
- Robust against overfitting
- Performs well on structured banking datasets
- Provides Feature Importance
- Suitable for binary classification

---

# 🔍 Hyperparameter Tuning

Model optimization was performed using **GridSearchCV** with 5-Fold Cross Validation.

Optimized Parameters:

- Number of Trees
- Maximum Tree Depth
- Minimum Samples Split

Evaluation Metric:

- Recall Score

---

# 📈 Model Evaluation

The model was evaluated using multiple classification metrics.

## Performance Metrics

| Metric | Score |
|---------|-------|
| Recall | **0.716** |
| Cross Validation Recall | **0.720** |
| Precision-Recall AUC | **0.880** |
| ROC AUC | **0.920** |

Additional evaluation includes:

- Confusion Matrix
- Classification Report
- Precision-Recall Curve
- ROC Curve
- Threshold Optimization
- Cross Validation

---

# 📊 Feature Importance

Random Forest Feature Importance was used to identify the most influential variables affecting loan default prediction.

This improves model interpretability and supports business decision-making.

---

# 💼 Business Insights

Key findings from the analysis:

- Customers with higher loan-to-income ratios have a greater probability of default.
- Previous loan default history is one of the strongest indicators of future default.
- Applicants with lower annual income exhibit higher financial risk.
- Higher interest rates are associated with increased default probability.
- Credit history length contributes significantly to loan approval decisions.

---

# 📌 Business Recommendations

Based on model predictions:

- Carefully review customers with high loan-to-income ratios.
- Apply stricter verification for applicants with previous defaults.
- Consider income stability before approving high-value loans.
- Use the prediction pipeline as an intelligent decision-support system during loan approval.

---

# 🚀 Production Features

✔ Automated Data Preprocessing

✔ Scikit-Learn Pipeline

✔ ColumnTransformer

✔ Data Leakage Prevention

✔ Hyperparameter Optimization

✔ Feature Importance Analysis

✔ Threshold Optimization

✔ Model Serialization using Joblib

✔ New Customer Prediction Pipeline

---

# 📁 Project Structure

```
Credit-Risk-Loan-Default-Pipeline/
│
├── data/
│   └── credit_risk_dataset.csv
│
├── notebook/
│   └── Credit_Risk_Loan_Default_Pipeline.ipynb
│
├── model/
│   └── credit_risk_pipeline.pkl
│
├── images/
│
├── README.md
│
├── requirements.txt
│
└── LICENSE
```

---

# 🎯 Future Improvements

- XGBoost and LightGBM Comparison
- SHAP Explainability
- Streamlit Web Application
- Model Deployment using FastAPI
- Real-Time Loan Risk Prediction API

---

# 🏆 Key Learning Outcomes

- End-to-End Machine Learning Pipeline Development
- Data Leakage Prevention
- Feature Engineering
- Hyperparameter Optimization
- Model Evaluation for Imbalanced Data
- Production-Ready ML Workflow
- Business-Oriented Model Interpretation

---

# 👩‍💻 Author

**Anuska Biswas**

Data Science & Machine Learning Enthusiast

```


