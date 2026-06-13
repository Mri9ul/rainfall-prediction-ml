import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Configure the page
st.set_page_config(page_title="Rainfall Predictor", page_icon="🌧️")


# Load the model
@st.cache_resource
def load_model():
    with open('rainfall_rf_model.pkl', 'rb') as file:
        return pickle.load(file)


model = load_model()

st.title("🌧️ ML Rainfall Predictor")
st.write("Adjust the weather parameters below to predict if it will rain tomorrow.")

# Create columns for a cleaner UI layout
col1, col2 = st.columns(2)

with col1:
    pressure = st.number_input("Pressure (hPa)", min_value=900.0, max_value=1100.0, value=1015.0)
    maxtemp = st.number_input("Max Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
    temperature = st.number_input("Average Temperature (°C)", min_value=-10.0, max_value=50.0, value=20.0)
    mintemp = st.number_input("Min Temperature (°C)", min_value=-10.0, max_value=50.0, value=15.0)
    dewpoint = st.number_input("Dewpoint", min_value=-10.0, max_value=40.0, value=18.0)

with col2:
    humidity = st.slider("Humidity (%)", min_value=0, max_value=100, value=80)
    cloud = st.slider("Cloud Cover (%)", min_value=0, max_value=100, value=50)
    sunshine = st.number_input("Sunshine (Hours)", min_value=0.0, max_value=24.0, value=5.0)
    winddirection = st.number_input("Wind Direction (°)", min_value=0.0, max_value=360.0, value=120.0)
    windspeed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=150.0, value=20.0)

# Prediction button
if st.button("Predict Rainfall 🔮"):

    # Notice the spelling of 'temparature' in the columns list below!
    # It MUST have an 'a' to match your notebook's training data.
    input_data = pd.DataFrame([[
        pressure, dewpoint,
        humidity, cloud, sunshine, winddirection, windspeed
    ]], columns=['pressure', 'dewpoint', 'humidity', 'cloud', 'sunshine',
       'winddirection', 'windspeed'])

    # Make prediction
    prediction = model.predict(input_data)[0]

    st.write("---")
    if prediction == 1:
        st.error("### 🌧️ Prediction: It will RAIN.")
    else:
        st.success("### ☀️ Prediction: It will NOT RAIN (Clear Skies).")