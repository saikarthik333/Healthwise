# app.py
import streamlit as st
import pickle
from components.prediction import predict_disease
from components.recommendation import get_specialist, get_remedies, generate_report_pdf
from components.maps import find_nearby_doctors

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="HealthWise AI Pro", page_icon="🏥", layout="wide")

# --- LOAD ASSETS ---
with open("models/symptoms.pkl", "rb") as f:
    all_symptoms = pickle.load(f)

# --- UI ---
st.title("🧠 HealthWise Pro: Analysis, Remedies & Doctor Locator")
st.markdown("Your intelligent health companion for predictions, remedies, and finding local specialists.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Step 1: Tell Us Your Symptoms")
    selected_symptoms = st.multiselect("Choose the symptoms you are experiencing:", options=all_symptoms)
with col2:
    st.subheader("Step 2: Provide Your Location")
    location_input = st.text_input("Enter your City or a specific Address:", placeholder="e.g., Hyderabad, India")

if st.button("🚀 Get Full Health Analysis", type="primary"):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    elif not location_input:
        st.warning("Please enter your location.")
    else:
        with st.spinner("Performing analysis, suggesting remedies, and finding doctors..."):
            predicted_disease = predict_disease(selected_symptoms, all_symptoms)
            recommended_specialist = get_specialist(predicted_disease)
            remedies_list = get_remedies(predicted_disease)
            nearby_doctors, map_df = find_nearby_doctors(location_input)
            
            st.success("**Analysis Complete! Here is your comprehensive report.**")
            
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.subheader("🩺 AI Prediction")
                st.metric(label="Predicted Condition", value=predicted_disease.title())
                st.metric(label="Recommended Specialist", value=recommended_specialist)
                st.subheader("🌿 General Remedies")
                for remedy in remedies_list:
                    st.write(f"- {remedy}")
            with res_col2:
                st.subheader(f"📍 Nearby Doctors & Hospitals")
                if map_df is not None and not map_df.empty:
                    st.map(map_df, zoom=12)
                else:
                    st.info("Could not find any doctors on the map for your location.")
            
            st.subheader("📄 Download Your Report")
            pdf_data = generate_report_pdf(selected_symptoms, predicted_disease, recommended_specialist, remedies_list)
            st.download_button(
                label="📥 Download Full Report as PDF",
                data=pdf_data,
                file_name=f"HealthWise_Report_{predicted_disease}.pdf",
                mime="application/pdf"
            )

st.markdown("---")
st.warning("**Disclaimer:** This is an AI-powered system and not a substitute for professional medical advice.")