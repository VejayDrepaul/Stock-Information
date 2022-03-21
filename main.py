import os
from time import monotonic
from turtle import width
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")

# Page Config
st.set_page_config(page_title="Stock Information", page_icon="page_icon.png", layout="wide")
st.markdown("<h1 style='text-align: center'>Stock Information</h1>", unsafe_allow_html=True)

# Ticker Entry 
stock_ticker = st.text_input("Ticker Symbol", placeholder="Enter Ticker Symbol: ").upper()

# Checkboxes & checkboxes container
csv_col, daily_col, intraday_col, monthly_col = st.columns(4)
view_csv = csv_col.checkbox("Show CSV File", help="Selecting this option will show the stock's csv file")
view_daily = daily_col.checkbox("Daily Stock Chart", help="Selecting this option will show the stock's daily chart")
view_intraday = intraday_col.checkbox("Intraday Chart", help="Selecting this option will show the stock's intraday chart")
view_monthly = monthly_col.checkbox("Monthly Chart", help="Selecting this option will show the stock's montly chart")

# Container for charts and csv 
placeholder = st.empty()


# Retrive CSV data
def fetch_csv_data(ticker_symbol):
    #csv_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv"
    df = pd.read_csv("daily_IBM.csv")
    st.dataframe(df)


# Retrive daily data
def fetch_daily_data(ticker_symbol):
    #csv_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv"
    df = pd.read_csv("daily_IBM.csv")
    daily_df = df[["timestamp", "close"]]
    daily_df = daily_df.set_index("timestamp")
    placeholder.line_chart(daily_df, width=1162, use_container_width=False)


# Retrive intraday data
def fetch_intraday_data(ticker_symbol):
    #csv_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv"
    df = pd.read_csv("intraday_60min_ibm.csv")
    intraday_df = df[["timestamp", "close"]]
    intraday_df = intraday_df.set_index("timestamp")
    placeholder.line_chart(intraday_df, width=1162, use_container_width=False)


# Retrive monthly data
def fetch_monthly_data(ticker_symbol):
    #csv_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker}&apikey={ALPHA_VANTAGE_KEY}&datatype=csv"
    df = pd.read_csv("monthly_IBM.csv")
    monthly_df = df[["timestamp", "close"]]
    monthly_df = monthly_df.set_index("timestamp")
    placeholder.line_chart(monthly_df, use_container_width=False)


if view_csv == False and view_daily == False:
    fetch_daily_data(stock_ticker)
elif view_csv == True and view_daily == True:
    placeholder.write("To many paramaters selected")
elif view_csv == True and view_daily == False:
    fetch_csv_data(stock_ticker)
elif view_csv == False and view_daily == True:
    fetch_daily_data(stock_ticker)
else:
    fetch_daily_data(stock_ticker)

if view_intraday == True:
    fetch_intraday_data(stock_ticker)
else:
    st.write("Error")

if view_monthly == True:
    fetch_monthly_data(stock_ticker)
else: 
    st.write("error")