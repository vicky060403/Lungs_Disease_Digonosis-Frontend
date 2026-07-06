import streamlit as st


def prediction_card(result):

    if "error" in result:

        st.error(result["error"])

        return

    prediction = result["prediction"]

    confidence = result["confidence"]

    st.subheader("🤖 AI Prediction")

    if prediction == "PNEUMONIA":

        st.error("🫁 Pneumonia Detected")

    else:

        st.success("✅ Normal")

    st.metric(
        "Prediction",
        prediction
    )

    st.metric(
        "Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(confidence / 100)