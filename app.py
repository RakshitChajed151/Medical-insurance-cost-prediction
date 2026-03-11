import streamlit as st
import pandas as pd
import joblib

model = joblib.load("insurance_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Medical Insurance Cost Prediction")

age = st.number_input("Age",18,100)
sex = st.selectbox("Sex",["Female","Male"])
bmi = st.number_input("BMI",10.0,50.0)
children = st.number_input("Children",0,5)
smoker = st.selectbox("Smoker",["No","Yes"])
region = st.selectbox("Region",["Southwest","Southeast","Northwest","Northeast"])

sex = 1 if sex=="Male" else 0
smoker = 1 if smoker=="Yes" else 0

region_dict = {
    "Southwest":0,
    "Southeast":1,
    "Northwest":2,
    "Northeast":3
}

region = region_dict[region]

# Prediction
if st.button("Predict Insurance Cost"):

    input_data = pd.DataFrame({
        "age":[age],
        "sex":[sex],
        "bmi":[bmi],
        "children":[children],
        "smoker":[smoker],
        "region":[region]
    })

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)

    st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")
