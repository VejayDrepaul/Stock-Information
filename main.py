import os
import streamlit as st
import pandas as pd
import numpy as np
from enum import auto
from multiprocessing.connection import wait
from dotenv import load_dotenv
load_dotenv()
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

st.set_page_config(page_title="Stock Information", page_icon="page_icon.png", layout="centered")
st.markdown("<h1 style='text-align: center'>Stock Information</h1>", unsafe_allow_html=True)


stock_ticker = st.text_input("Ticker Symbol", placeholder="Enter Ticker Symbol: ").upper()
enable_csv = st.checkbox("Show CSV File")


csv_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv"
df = pd.read_csv(csv_url)

if stock_ticker == "":
    wait(auto)
else:
    st.write(df)


if enable_csv:
    chart_data = pd.DataFrame(
        df["timestamp"],
        df["close"]
    )
