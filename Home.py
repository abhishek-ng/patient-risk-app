import streamlit as st

st.set_page_config(page_title='Patient Risk Assessment System', layout='wide')
st.title('Patient Risk Assessment System')

st.markdown(
  """
  This demo app shows a small multipage workflow to upload patient data, clean & explore it,
  run a simple risk-scoring model, and generate a downloadable report.
  
  
  Use the sidebar (Pages) to navigate between pages:
  - Upload Patient Data
  - Clean and Explore Data
  - Risk Analysis
  - Generate Report
  """
)

st.info('This is the Home page. Use this sidebar to open other pages.')
st.write('**Quick start:** Upload a CSV file via `Upload Patient Data` page, then go to `Risk Analysis`.')
