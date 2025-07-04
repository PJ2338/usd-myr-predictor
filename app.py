import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("rf_model.pkl")

st.set_page_config(page_title="USD/MYR Exchange Rate Predictor", layout="centered")
st.title("📈 USD/MYR Exchange Rate Predictor using Random Forest Model")

st.markdown("Enter 10 macroeconomic indicators to predict the **log(USD/MYR)** exchange rate.")

# Sidebar for input
st.sidebar.header("Input Macroeconomic Indicators")

features = {
    'MSIA_IR_lag1': st.sidebar.number_input("🇲🇾 Malaysia Interest Rate", value=3.0),
    'MSIA_UR_lag1': st.sidebar.number_input("🇲🇾 Malaysia Unemployment Rate", value=3.5),
    'FBMKLCI_Index_lag1': st.sidebar.number_input("🇲🇾 FBMKLCI Index", value=1450.0),
    'GVZ_lag1': st.sidebar.number_input("GVZ Index", value=19.0),
    'USA_IR_lag1': st.sidebar.number_input("🇺🇸 US Interest Rate", value=5.25),
    'USA_IPI_lag1': st.sidebar.number_input("🇺🇸 US Industrial Production Index", value=105.0),
    'USA_UR_lag1': st.sidebar.number_input("🇺🇸 US Unemployment Rate", value=3.6),
    'USA_M1_lag1': st.sidebar.number_input("🇺🇸 US M1 Money Supply", value=18000.0),
    'S&P_Index_lag1': st.sidebar.number_input("🇺🇸 S&P 500 Index", value=4400.0),
    'MSIA_NetTrade_lag1': st.sidebar.number_input("🇲🇾 Malaysia Net Trade", value=25.0)
}

# Convert to numpy array for prediction
input_array = np.array([list(features.values())])

# Predict
if st.button("Predict USD/MYR"):
    prediction = model.predict(input_array)[0]
    st.subheader("📊 Prediction Result")
    st.write(f"### 🔹 Predicted `USD/MYR` = `{prediction:.4f}`")
