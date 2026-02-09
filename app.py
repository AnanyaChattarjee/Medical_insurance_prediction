import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load saved model files
theta = joblib.load("theta_final.pkl")
columns = joblib.load("model_columns.pkl")
label_encodings = joblib.load("label_encodings.pkl")

st.set_page_config(page_title="Medical Insurance Charges Predictor", layout="centered")

st.title("💉 Medical Insurance Charges Prediction")
st.write("Predict medical insurance charges using a Linear Regression model trained with Gradient Descent.")

# Inputs
age = st.number_input("Age", min_value=1, max_value=100, value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=27.0)
children = st.number_input("Children", min_value=0, max_value=10, value=0)

sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

# Encode categorical values using saved mapping
sex_encoded = label_encodings["sex"][sex]
smoker_encoded = label_encodings["smoker"][smoker]
region_encoded = label_encodings["region"][region]

# Create input dataframe
input_data = pd.DataFrame([{
    "age": age,
    "sex": sex_encoded,
    "bmi": bmi,
    "children": children,
    "smoker": smoker_encoded,
    "region": region_encoded
}])

# Ensure correct column order
input_data = input_data[columns]

# Prediction
if st.button("Predict Charges 💰"):
    y_pred = np.dot(input_data.values, theta)[0][0]
    st.success(f"Predicted Insurance Charges: ₹ {y_pred:,.2f}")
