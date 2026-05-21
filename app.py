import streamlit as st
import pickle
import numpy as np

# Load model
with open("salary_prediction_model(1).pkl", "rb") as file:
    model = pickle.load(file)

st.title("Salary Prediction App")

# User input
experience = st.number_input("Enter Years of Experience", min_value=0.0)

# Prediction
if st.button("Predict Salary"):
    prediction = model.predict([[experience]])

    st.success(f"Predicted Salary: {prediction[0]:,.2f}")
