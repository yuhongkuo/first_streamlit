import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("""
    <style>
    [data-testid="stToolbar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# 讀取 CSV
population = pd.read_csv('./data/總人口.csv')

fig = px.line(
    population, 
    x='year', 
    y='pop',
    markers=True,
    title="桃園市人口(95~113年)",
    labels={'year': '年分', 'pop': '人口'}
    )

st.plotly_chart(fig)