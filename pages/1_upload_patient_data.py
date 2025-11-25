import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title='Upload Patient Data')
st.title('1. Upload Patient Data')

st.write("Upload a CSV or Excel file with patient records. Expected columns:")
st.write("`patient_id, name, age, gender, bmi, systolic_bp, diastolic_bp, cholesterol, diabetes`")

uploaded = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

# -------------------------
# File Upload
# -------------------------
if uploaded is not None:
    try:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)

        st.session_state["raw_data"] = df

        st.success(f"Loaded {len(df)} rows from `{uploaded.name}`")
        st.subheader("Preview")
        st.dataframe(df.head(10))

        st.markdown("---")

        # 🎯 Save + Loading animation + Redirect
        if st.button("Save and Continue"):
            st.session_state["data_uploaded"] = True

            st.switch_page('pages/2_clean_and_explore_data.py')

    except Exception as e:
        st.error("Failed to read file. Check format.")
        st.exception(e)

else:
    st.info("No file uploaded yet. You can try the demo dataset below.")

# -------------------------
# Demo dataset button
# -------------------------
if st.button("Load Demo Dataset"):
    df = pd.DataFrame({
        "patient_id": range(1, 101),
        "name": [f"Patient {i}" for i in range(1, 101)],
        "age": np.random.randint(20, 90, 100),
        "gender": np.random.choice(["M", "F"], 100),
        "bmi": np.random.normal(26, 4, 100).round(1),
        "systolic_bp": np.random.randint(100, 180, 100),
        "diastolic_bp": np.random.randint(60, 110, 100),
        "cholesterol": np.random.randint(150, 280, 100),
        "diabetes": np.random.choice([0, 1], 100, p=[0.85, 0.15]),
    })

    st.session_state["raw_data"] = df

    st.switch_page('pages/2_clean_and_explore_data.py')
