import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.title("🫁 Lung AI")

        st.divider()

        page = st.radio(
            "Navigation",
            [
                "Home",
                "Prediction",
                "History",
                "About"
            ]
        )

        st.divider()

        st.success("Backend Online")

        st.write("✅ BentoML")

        st.write("✅ Docker")

        st.write("✅ AWS EC2")

        st.write("✅ Amazon ECR")

        st.divider()

        st.caption("Version 1.0")

    return page