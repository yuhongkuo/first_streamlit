import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    [data-testid="stToolbar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

sales = pd.read_csv('./data/sales.csv')

st.table(sales)