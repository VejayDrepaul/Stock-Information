import os
import streamlit as st
import pandas as pd
from enum import auto
from multiprocessing.connection import wait
from dotenv import load_dotenv
load_dotenv()
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

# Page Config
st.set_page_config(page_title="Stock Information", page_icon="page_icon.png", layout="wide")
st.markdown("<h1 style='text-align: center'>Stock Information</h1>", unsafe_allow_html=True)

# Ticker Entry 
stock_ticker = st.text_input("Ticker Symbol", placeholder="Enter Ticker Symbol: ").upper()

# Checkboxes & checkboxes container
csv_checkbox_col, chart_checkbox_col = st.columns(2)
view_csv = csv_checkbox_col.checkbox("Show CSV File")
view_chart = chart_checkbox_col.checkbox("Show Stock Chart")

#csv_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv"
df = pd.read_csv("daily_IBM.csv")
chart_df = df[["timestamp", "close"]]
chart_df = chart_df.set_index("timestamp")

# Container for charts and csv 
placeholder = st.empty()

if view_csv == False and view_chart == False:
    placeholder.line_chart(chart_df, width=1162, use_container_width=False)
elif view_csv == True and view_chart == True:
    placeholder.write("To many paramaters selected")
elif view_csv == True and view_chart == False:
    placeholder.write(df)
elif view_csv == False and view_chart == True:
    placeholder.line_chart(chart_df, width=1162, use_container_width=False)
else:
    placeholder.line_chart(chart_df, width=1162, use_container_width=False)
