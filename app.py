# app.py
import streamlit as st
import pandas as pd
from components.predict import predict_disease

# Load symptoms list
df = pd.read_csv('data/symptoms.csv')
all_symptoms = df.columns[:-1].tolist()  # all except the last column

st.set_page_config(page_title="HealthWise", page_icon="🩺", layout="centered")
st.title("🧠 HealthWise - AI Symptom Checker & Doctor Recommender")

st.write("Select your symptoms and get instant health advice.")

# Multiselect input
selected_symptoms = st.multiselect("Choose your symptoms:", all_symptoms)

if st.button("🔍 Predict"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        prediction, doctor = predict_disease(selected_symptoms, all_symptoms)
        st.success(f"🦠 **Predicted Disease:** {prediction}")
        st.info(f"👨‍⚕️ **Recommended Doctor:** {doctor}")
