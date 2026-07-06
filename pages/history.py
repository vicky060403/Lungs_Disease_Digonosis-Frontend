import streamlit as st
import pandas as pd

from utils.database import get_predictions


st.set_page_config(

    page_title="Prediction History",

    page_icon="📜",

    layout="wide"

)

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

    c1.metric("Total", total)

    c2.metric("Pneumonia", pneumonia)

    c3.metric("Normal", normal)

    c4.metric("Avg Confidence", f"{avg:.2f}%")

    st.divider()

    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )