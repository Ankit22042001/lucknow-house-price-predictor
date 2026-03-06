import streamlit as st
import pickle
import numpy as np

# Model load karein
model = pickle.load(open('lko_model.pkl', 'rb'))

st.title("Lucknow House Price Predictor 🏠")
st.write("Apne sapno ke ghar ki keemat check karein!")

# User Inputs
area = st.number_input("Area (Square Feet)", min_value=500, max_value=10000, value=1200)
bhk = st.selectbox("BHK", [1, 2, 3, 4, 5])
bath = st.selectbox("Bathrooms", [1, 2, 3, 4])

if st.button("Predict Price"):
    # Note: Prediction ke liye locality encoding dhyan mein rakhni hogi
    prediction = model.predict([[1, bhk, area, bath]]) # 1 dummy locality code hai
    st.success(f"Estimated Price in Lucknow: ₹{prediction[0]:.2f} Lakhs")