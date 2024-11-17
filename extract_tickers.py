import re
import streamlit as st
import yfinance as yf

def extract_tickers(text):
    # Modify the regex pattern based on your requirements
    pattern = r'\b[A-Z]{1,5}\b'
    return re.findall(pattern, text)

@st.cache_data
def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    return stock.info
