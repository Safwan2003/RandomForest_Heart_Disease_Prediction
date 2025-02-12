import streamlit as st
import pandas as pd
import joblib

# Load the pipeline
pipeline = joblib.load("model/heart_disease_pipeline.pkl")

# Streamlit UI
st.title("Heart Disease Prediction")

# User input fields
smoking = st.selectbox("Smoking (0 = No, 1 = Yes)", [0, 1])
stroke = st.selectbox("Stroke (0 = No, 1 = Yes)", [0, 1])
physical_health = st.slider("Physical Health (0 to 30 days)", 0, 30, 10)
diff_walking = st.selectbox("Difficulty Walking (0 = No, 1 = Yes)", [0, 1])
age_category = st.slider("Age Category (18 to 100)", 18, 100, 55)
diabetic = st.selectbox("Diabetic (0 = No, 1 = Yes)", [0, 1])
kidney_disease = st.selectbox("Kidney Disease (0 = No, 1 = Yes)", [0, 1])

# Age binning logic
binned_age_senior = 1 if age_category >= 60 else 0
binned_age_middle_aged = 1 if 40 <= age_category < 60 else 0
binned_age_young = 1 if age_category < 40 else 0

# Create a dataframe for the input
input_data = pd.DataFrame([[smoking, stroke, physical_health, diff_walking, diabetic, kidney_disease, 
                           binned_age_senior, binned_age_middle_aged, binned_age_young]], 
                         columns=["Smoking", "Stroke", "PhysicalHealth", "DiffWalking", "Diabetic", "KidneyDisease", 
                                  "BinnedAge_Senior", "BinnedAge_Middle-aged", "BinnedAge_Young"])

# Prediction
if st.button("Predict"):
    prediction = pipeline.predict(input_data)
    result = "Heart Disease" if prediction[0] == 1 else "No Heart Disease"
    st.write(f"Prediction: **{result}**")
