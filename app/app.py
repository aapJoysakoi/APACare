import streamlit as st
import pandas as pd
from faker import Faker

fake = Faker()

st.set_page_config(
    page_title="APACare",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ APACare")
st.subheader("Because your health data deserves borders too")

st.markdown("""
**APACare** is an AI-inspired privacy sentinel for healthcare data.  
It helps individuals check whether their personal health-related identity
appears in leaked or breached datasets.

This is a **prototype for Society 5.0**, where humans stay in control of their data.
""")

st.divider()

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
hospital = st.text_input("Hospital or Healthcare Provider")

if st.button("Scan for Data Exposure"):
    st.subheader("Scan Results")

    if "joysa" in name.lower():
        st.success("✅ No data found. Your digital health identity appears safe.")
    elif "Seint" in name.lower():
        st.success("you're safe! Keep eating apples!")
    else:
        st.warning("⚠️ Potential exposure detected")

        fake_results = {
            "Source": ["Third-party analytics vendor", "Unsecured cloud database"],
            "Data Type": ["Email + Hospital Name", "Metadata"],
            "Risk Level": ["Medium", "High"]
        }

        df = pd.DataFrame(fake_results)
        st.table(df)

        st.info("""
        This does NOT mean your medical records were leaked.
        It indicates possible secondary data exposure.
        """)

st.divider()

st.caption("APACare • Society 5.0 • Asia-Pacific Youth Innovation")
