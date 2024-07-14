import streamlit as st, pandas as pd, numpy as np, yfinance as yf, datetime as dt
import plotly.express as px

st.title('Stock Dashboard')
ticker = st.sidebar.text_input('Stock Dashboard')
start_date = st.sidebar.date_input('Start Date', dt.date(2020,1,1))
end_date = st.sidebar.date_input('End Date', dt.date(2021,1,1))

data = yf.download(ticker, start=start_date, end=end_date)
fig = px.line(data, x = data.index, y=['Adj Close'], title = ticker)
st.plotly_chart(fig)
st.write(data)

pricing_data, fundamental_data = data, news = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

with pricing_data:
    st.write('Price')
    data2 = data
    data2['% Change'] = data2['Adk Close'] / data2['Adj Close'].shift(1)
    data2.dropna(inplace=True)      
    st.write(data2)
    annaulized_return = (data2['% Change'].mean()*252*100

with fundamental_data:
    st.write('Fundamental')

with news:
    st.write('News')
    
