import streamlit as st


def patient_form():

    st.subheader("👤 Patient Details")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input("Patient Name")

        age = st.number_input(
            "Age",
            1,
            120,
            25
        )

    with col2:

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female",
                "Other"
            ]
        )

        doctor = st.text_input(
            "Doctor"
        )

    symptoms = st.text_area(
        "Symptoms"
    )

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "doctor": doctor,
        "symptoms": symptoms
    }