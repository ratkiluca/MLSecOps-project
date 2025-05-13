import streamlit as st
import requests
import codecs
from pathlib import Path

st.title("Sentiment Analysis App")


# Szövegbevitel és predikció
user_input = st.text_input(label="Írd be a szöveget:")

if st.button(label="Predikció") and user_input:
    try:
        response = requests.post(
            url="http://mlsecops-api-service:8000/predict",
            json={"text": user_input},
            timeout=20,
        )
        if response.status_code == 200:
            result = response.json()
            st.write(f"Eredmény: {result['label']} ({result['score']:.2f})")
        else:
            st.write("Hiba a predikció során. Állapotkód:", response.status_code)
    except Exception as e:
        st.write("Nem sikerült elérni az API-t:", str(e))

# HTML fájlok megjelenítése
st.header("Adat Drift és Teszt Eredmények")

# Mentett HTML fájlok elérési útja
report_path = Path("data_drift_report.html")
suite_path = Path("suite.html")

# Ellenőrizzük, hogy a fájlok léteznek-e
if report_path.exists():
    with codecs.open(report_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=600)  # HTML fájl beágyazása

else:
    st.write("A `data_drift_report.html` fájl nem található.")

if suite_path.exists():
    with codecs.open(suite_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=600)  # HTML fájl beágyazása

else:
    st.write("A `suite.html` fájl nem található.")
