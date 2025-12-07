import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("Customer Churn Prediction App")
st.write("Enter customer details and predict churn in real time.")

name = st.text_input("Customer Name")
age = st.number_input("Age", min_value=1)
gender = st.selectbox("Gender", ["Male", "Female"])
tenure = st.number_input("Tenure (months)", min_value=0)
monthly_charges = st.number_input("Monthly Charges")
total_charges = st.number_input("Total Charges")

gender_val = 1 if gender == "Male" else 0

if st.button("Predict Churn"):
    input_data = np.array([[age, gender_val, tenure, monthly_charges, total_charges]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success(f"Prediction for {name}: Will Churn")
    else:
        st.success(f"Prediction for {name}: Will Not Churn")
