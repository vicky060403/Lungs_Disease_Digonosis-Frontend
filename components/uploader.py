import streamlit as st
from PIL import Image
from datetime import datetime
from utils.database import save_prediction
from components.patient_form import patient_form
from components.prediction import prediction_card
from utils.api import predict_image
from utils.report import create_report


def uploader():

    st.subheader("📤 Upload Chest X-ray")

    # ---------------- Patient Details ---------------- #

    patient = patient_form()

    st.divider()

    # ---------------- Upload Image ---------------- #

    uploaded_file = st.file_uploader(
        "Choose a Chest X-ray",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is None:
        return

    image = Image.open(uploaded_file)

    col1, col2 = st.columns([1, 1])

    with col1:

        st.markdown("### 🩻 Uploaded X-ray")

        st.image(
            image,
            use_container_width=True
        )

    with col2:

        st.markdown("### 🤖 AI Analysis")

        if st.button(
            "🔍 Analyze Chest X-ray",
            use_container_width=True
        ):

            # Validate Patient Name
            if patient["name"].strip() == "":

                st.warning("Please enter the patient name.")

                return

            # Call API
            with st.spinner("Analyzing Chest X-ray..."):

                result = predict_image(uploaded_file)

            # Handle API Error
            if "error" in result:

                st.error(result["error"])

                return

            # Show Prediction
            prediction_card(result)

            # Save Prediction History
            current_time = datetime.now().strftime("%d-%m-%Y %H:%M")

            save_prediction(

                patient,

                result["prediction"],

                result["confidence"],

                current_time

            )

            # Generate PDF Report
            pdf = create_report(

                patient=patient,

                prediction=result["prediction"],

                confidence=result["confidence"],

                image=uploaded_file

            )

            st.success("✅ Report Generated Successfully")

            st.download_button(

                label="📄 Download Diagnosis Report",

                data=pdf,

                file_name=f"{patient['name']}_Diagnosis_Report.pdf",

                mime="application/pdf",

                use_container_width=True
            )