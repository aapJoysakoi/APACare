import streamlit as st
from utils.matcher import check_exposure
from ai.risk_engine import calculate_risk, explain_risk

st.set_page_config(page_title="APACare", layout="centered")

st.title("APACare")
st.caption("In Society 5.0, AI should care back.")

st.write(
    "APACare helps people understand whether their health-related data may have been exposed "
    "and what that exposure could mean for them."
)

user_input = st.text_input("Enter email, phone number, or hospital name")

if st.button("Scan with APACare"):
    results = check_exposure(user_input)

    if results.empty:
        st.success("No exposure found. APACare did not detect any known health data exposure.")
    else:
        st.warning("Potential health data exposure detected.")

        for _, row in results.iterrows():
            risk_score = calculate_risk(row["category"])
            explanation = explain_risk(row["category"])

            st.subheader(f"Source: {row['source']}")
            st.write(f"Data type: {row['category']}")
            st.write(f"Risk score: {risk_score} / 10")
            st.write(f"Why this matters: {explanation}")
            st.write("Suggested action: Contact the healthcare provider and request clarification.")
