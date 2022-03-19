import os
import streamlit as st
import pandas as pd
import numpy as np
from dotenv import load_dotenv
load_dotenv()
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

st.markdown("<h1 style='text-align: center'>Stock Information</h1>", unsafe_allow_html=True)
stock_ticker = st.text_input("Ticker Symbol", placeholder="Enter Ticker Symbol: ").upper()

csv_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv"
df = pd.read_csv(csv_url)
st.write(df)

