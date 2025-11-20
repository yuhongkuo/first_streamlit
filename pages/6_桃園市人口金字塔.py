import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.markdown("""
    <style>
    [data-testid="stToolbar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

df=pd.read_csv('./data/性別比.csv')

data={
    "age_group": df.iloc[ :, 0],
    "male": df.iloc[ :, 1],
    "female": df.iloc[ :, 2]
}

# 為了顯示金字塔，將男性值變成負數（水平條）
fig = go.Figure()

fig.add_trace(go.Bar(
    y=data["age_group"],
    x=-data["male"],                # 讓男性向左
    name="Male",
    orientation='h',
    hovertemplate='Age: %{y}<br>Male: %{text}',  # 設定顯示格式
    text=data["male"],
    marker_color='steelblue' 
))

fig.add_trace(go.Bar(
    y=data["age_group"],
    x=data["female"],               # 女性向右
    name="Female",
    orientation='h',
    hovertemplate='Age: %{y}<br>Female: %{text}',
    text=data["female"],
    marker_color='salmon'
))

# 美化與軸設定
fig.update_layout(
    title="桃園市男女人口數按性別及五歲年齡組分(113年)",
    barmode='overlay',
    bargap=0.15,
    yaxis=dict(title='年齡組'),  # 讓年齡從上到下
)

fig.update_traces(marker_line_width=0)  # 去除條紋線
st.plotly_chart(fig)
