import streamlit as st
import pandas as pd

# Ensure df exists
if "raw_data" not in st.session_state:
    st.warning("No data found. Please upload data first.")
    st.stop()

df = st.session_state["raw_data"].copy()

st.subheader("Summary Statistics")
st.write(df.describe(include='all'))

st.subheader("Missing Values")
missing = df.isna().sum()
st.write(missing[missing > 0] if missing.any() else "No missing values detected.")

st.markdown("---")
st.subheader("Cleaning Actions")

submitted = False  # avoid undefined variable issues

with st.form("clean_form"):
    fill_na_method = st.selectbox(
        "Fill missing numeric values with:",
        ["Mean", "Median", "Zero", "None"],
        index=0
    )
    drop_cols = st.multiselect(
        "Drop columns (if any):",
        options=list(df.columns)
    )

    submitted = st.form_submit_button("Apply")

# -------------------------
# APPLY CLEANING LOGIC
# -------------------------
if submitted:
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()

    # Fill NA options
    if fill_na_method == "Mean":
        df[num_cols] = df[num_cols].fillna(df[num_cols].mean())
    elif fill_na_method == "Median":
        df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    elif fill_na_method == "Zero":
        df[num_cols] = df[num_cols].fillna(0)
    # "None" → do nothing

    # Drop selected columns
    if drop_cols:
        df = df.drop(columns=drop_cols)

    # Save cleaned dataframe
    st.session_state["clean_data"] = df
    st.success("Cleaning applied and saved to session as `clean_data`.")

    st.rerun()

# -------------------------
# SHOW CLEANED PREVIEW
# -------------------------
st.markdown("---")

if "clean_data" in st.session_state:
    st.subheader("Current Cleaned Data Preview")
    st.dataframe(st.session_state["clean_data"].head(100))

    if st.button("Use cleaned data for analysis"):
        st.session_state["use_clean_for_analysis"] = True
        st.success("Clean data will be used in Risk Analysis page.")
