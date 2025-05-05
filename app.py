import streamlit as st
import requests

st.title(body="Sentiment Analysis App")
user_input = st.text_input(label="Írd be a szöveget:")

if st.button(label="Predikció"):
    response = requests.post(
        url="http://localhost:8000/predict",
        json={"text": user_input},
        timeout=20
    )
    if response.status_code == 200:
        result = response.json()
        st.write(f"Eredmény: {result['label']} ({result['score']:.2f})")
