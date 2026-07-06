import streamlit as st
import pandas as pd
from components.stats import stats
from components.sidebar import show_sidebar
from components.hero import hero
from components.uploader import uploader
from components.footer import footer
from utils.database import create_table, get_predictions

def load_css():

    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

st.set_page_config(
    page_title="Lung Disease Diagnosis",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="expanded"
)

create_table()

load_css()

page = show_sidebar()

hero()

stats()

st.divider()

if page == "Home":

    st.success(
        "Welcome to Lung Disease Diagnosis System"
    )

elif page == "Prediction":

    uploader()
    
elif page == "History":

    st.title("📜 Prediction History")

    rows = get_predictions()

    if len(rows) == 0:

        st.info("No prediction history available.")

    else:

        df = pd.DataFrame(

            rows,

            columns=[
                "Patient",
                "Age",
                "Gender",
                "Doctor",
                "Symptoms",
                "Prediction",
                "Confidence",
                "Date"
            ]

        )

        total = len(df)

        pneumonia = len(df[df["Prediction"] == "PNEUMONIA"])

        normal = len(df[df["Prediction"] == "NORMAL"])

        avg = df["Confidence"].mean()

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("Total Predictions", total)

        c2.metric("Pneumonia", pneumonia)

        c3.metric("Normal", normal)

        c4.metric(
            "Average Confidence",
            f"{avg:.2f}%"
        )

        st.divider()

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

elif page == "About":

    st.title("🫁 About")

    st.write(
        """
### Lung Disease Diagnosis using Deep Learning

This project predicts lung diseases from Chest X-ray images.

### Technologies

- PyTorch
- BentoML
- Docker
- AWS EC2
- Amazon ECR
- Streamlit

### Model

Custom CNN Model trained on Chest X-ray dataset.

### Deployment

Docker + AWS EC2 + BentoML

### Developed By

Vicky Kumar
"""
    )


footer()