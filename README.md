# USD/MYR Exchange Rate Predictor (log-scale)

A simple Streamlit web app that allows users to input macroeconomic indicators to predict the **log(USD/MYR)** exchange rate using a trained Random Forest model.

## 🔧 Features
- Manual input of macroeconomic variables via Streamlit sidebar
- Predicts exchange rate in log scale
- Deployed on Streamlit Cloud

## 🧪 Example Variables
- Malaysia & US interest rates, unemployment, CPI, trade
- FBMKLCI, S&P500, VIX, GVZ

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
