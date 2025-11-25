import streamlit as st
import pandas as pd

st.page_confg(page_title='Upload Patient Data')
st.title('1. Upload patient Data')
st.write('Upload a CSV or Excel file with patient records. The app expects column like:')
st.write('`patient_id, name, age, gender, bmi, systolic_bp, diastolic_bp, cholesterol, diabetes` (optional)')

uploaded = st.file_uploader('Choose a CSV or Excel file', type=['csv', 'xlsx'])
if uploaded is not None:
  try:
    if uploaded.name.endswith('.csv'):
      df = pd.read_csv(uploaded)
    else:
      df = pd.read_excel(uploaded)

    st.session_state['raw_data']=df
    st.success(f'Loaded {len(df)} rows from `{uploaded.name}`')
    st.subheader('Preview')
    st.dataframe(df.head(10))
    st.markdown('---')
    if st.button('Save to app storage/continue'):
      st.session_state['data_uploaded'] = True
      st.success('Data saved to session state. GO to "Clean and Explore Data" or "Risk Analysis".')

  except Exception as e:
    st.error('Failed to read file. Make sure it is a valid CSV/XLSX and has a reader row.')
    st.exception(e)

else:
  st.info('No file uploaded yet. You can try the included demo database below.')

if st.button('Load Demo Dataset'):
  import numpy as np
  df = pd.DataFrame({
  "patient_id": range(1,101),
  "name": [f"Patient {i}" for i in range(1,101)],
  "age": np.random.randint(20, 90, size=100),
  "gender": np.random.choice(["M","F"], size=100),
  "bmi": (np.random.normal(26, 4, size=100)).round(1),
  "systolic_bp": np.random.randint(100, 180, size=100),
  "diastolic_bp": np.random.randint(60, 110, size=100),
  "cholesterol": np.random.randint(150, 280, size=100),
  "diabetes": np.random.choice([0,1], size=100, p=[0.85,0.15])
  })
  st.session_state['raw_data']=df
  st.success('Demo dataset loaded into session state')
  st.experimental_rerun()
