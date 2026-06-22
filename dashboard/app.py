import streamlit as st
import pandas as pd

df = pd.read_csv("../data/raw/hdfc_top100_clean.csv")

st.title("📈 Mutual Fund Analytics Dashboard")

st.metric("Latest NAV", round(df["nav"].iloc[-1], 2))

st.line_chart(df["nav"])

st.write("Total Records:", len(df))