import os
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
view_chart = daily_col.checkbox("Daily Stock Chart", help="Selecting this option will show the stock's daily chart")
view_intraday = intraday_col.checkbox("Intraday Chart", help="Selecting this option will show the stock's intraday chart")
view_monthly = monthly_col.checkbox("Monthly Chart", help="Selecting this option will show the stock's montly chart")

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
    placeholder.dataframe(df)
elif view_csv == False and view_chart == True:
    placeholder.line_chart(chart_df, width=1162, use_container_width=False)
else:
    placeholder.line_chart(chart_df, width=1162, use_container_width=False)
