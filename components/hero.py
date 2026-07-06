import streamlit as st


def hero():

    st.markdown(
        """
        <div style="
            padding:40px;
            border-radius:20px;
            background:linear-gradient(90deg,#0f62fe,#42a5f5);
            color:white;
            text-align:center;
            margin-bottom:30px;
        ">
            <h1>🫁 Lung Disease Diagnosis</h1>
            <h3>AI Powered Chest X-ray Analysis</h3>
            <p>
                Upload a Chest X-ray and receive an instant medical diagnosis(This model uses CNN model to analyze the medical images).
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )