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
