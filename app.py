

import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("credit_risk_model.pkl")

st.set_page_config(
    page_title="Credit Risk & Loan Default Prediction",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Credit Risk & Loan Default Prediction")
st.write("Enter applicant details to predict loan default risk.")

person_age = st.number_input("Age", 18, 100, 28)
person_income = st.number_input("Annual Income", min_value=1000, value=60000)
person_home_ownership = st.selectbox(
    "Home Ownership",
    ["RENT", "OWN", "MORTGAGE", "OTHER"]
)
person_emp_length = st.number_input(
    "Employment Length (Years)", min_value=0.0, value=4.0
)
loan_intent = st.selectbox(
    "Loan Purpose",
    ["EDUCATION", "MEDICAL", "PERSONAL", "VENTURE", "HOMEIMPROVEMENT", "DEBTCONSOLIDATION"]
)
loan_grade = st.selectbox(
    "Loan Grade",
    ["A", "B", "C", "D", "E", "F", "G"]
)
loan_amnt = st.number_input("Loan Amount", min_value=500, value=12000)
loan_int_rate = st.number_input(
    "Interest Rate (%)", min_value=0.0, value=10.5
)
loan_percent_income = st.number_input(
    "Loan Percent of Income", min_value=0.0, value=0.20
)
cb_person_default_on_file = st.selectbox(
    "Previous Default",
    ["N", "Y"]
)
cb_person_cred_hist_length = st.number_input(
    "Credit History Length", min_value=1, value=5
)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "person_age":[person_age],
        "person_income":[person_income],
        "person_home_ownership":[person_home_ownership],
        "person_emp_length":[person_emp_length],
        "loan_intent":[loan_intent],
        "loan_grade":[loan_grade],
        "loan_amnt":[loan_amnt],
        "loan_int_rate":[loan_int_rate],
        "loan_percent_income":[loan_percent_income],
        "cb_person_default_on_file":[cb_person_default_on_file],
        "cb_person_cred_hist_length":[cb_person_cred_hist_length]
    })

    # Feature Engineering
    input_df["income_to_loan"] = (
        input_df["person_income"] / input_df["loan_amnt"]
    )
    input_df["experience_per_age"] = (
        input_df["person_emp_length"] / input_df["person_age"]
    )
    input_df["interest_amount"] = (
        input_df["loan_amnt"] * input_df["loan_int_rate"] / 100
    )

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

   if prediction == 1:
    st.error(
        f"⚠️ High Risk of Loan Default\n\n"
        f"Probability: {probability:.2%}"
    )
else:
    st.success(
        f"✅ Low Risk of Loan Default\n\n"
        f"Probability: {probability:.2%}"
    )
