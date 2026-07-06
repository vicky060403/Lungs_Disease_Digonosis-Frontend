import streamlit as st


def stats():

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Model Accuracy",
            "95.65%"
        )

    with col2:

        st.metric(
            "Disease Classes",
            "2"
        )

    with col3:

        st.metric(
            "Deployment",
            "AWS EC2"
        )