import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    [data-testid="stToolbar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

sales = pd.read_csv('./data/sales.csv')

st.table(sales.groupby('業務單位')[['銷售數量','銷售金額']].sum().style.highlight_min())