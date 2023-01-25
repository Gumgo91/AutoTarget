import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(layout="wide")

st.title('AutoTarget')
st.write("Disease-associated drug targets recommendation system using graph theory and machine learning")

with st.spinner('Loading...'):
    from autotarget import autotarget
    searcher = autotarget.Searcher()

@st.experimental_memo
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

side_scope = st.sidebar.radio("Scope", ['positive', 'negative', 'all'])
side_mode = st.sidebar.radio("Mode", ['exact', 'partial'])

side_threshold = st.sidebar.text_input(label="Threshold", value="0.05", max_chars=10)
searcher.change_threshold(float(side_threshold))

side_link = st.sidebar.write("[@Hyunseung Kong](https://www.linkedin.com/in/hyunseungkong/)")

if side_mode == 'exact':
    disease = st.selectbox("Disease name", searcher.search_disease(''))
else:
    disease = st.text_input(label="Disease name", value="", max_chars=10)
 
df = searcher.search(disease, mode=side_mode, scope=side_scope)
csv = convert_df(df)
st.download_button(
   "Press to Download",
   csv,
   "autotarget.csv",
   "text/csv",
   key='download-csv'
)

st.dataframe(df)