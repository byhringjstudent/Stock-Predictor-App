import streamlit as st, pandas as pd, numpy as np, yfinance as yf, datetime as dt
import plotly.express as px

st.title('Stock Dashboard')
ticker = st.sidebar.text_input('Stock Dashboard')
start_date = st.sidebar.date_input('Start Date', dt.date(2020,1,1))
end_date = st.sidebar.date_input('End Date', dt.date(2021,1,1))

# Fetch the data using Yahoo Finance API
# data = yf.download(ticker, start=start_date, end=end_date)
# fig = px.line(data, x = data.index, y=['Adj Close'], title = ticker)
# st.plotly_chart(fig)
# st.write(data)

# Balance Sheet
# st.subheader('Balance Sheet')
# balance_sheet = stock.balance_sheet
# bs = balance_sheet.T.iloc[2:]  # Skip the first two rows for headers and unnecessary data
# bs.columns = list(balance_sheet.T.iloc[0])  # Set columns to the first row of transposed data
# st.write(bs)

# Income Statement
# st.subheader('Income Statement')
# income_statement = stock.financials
# income_statement_data = income_statement.T.iloc[2:, :]  # Skip the first two rows for headers and unnecessary data
# income_statement_data.columns = list(income_statement.T.iloc[0])  # Set columns to the first row of transposed data
# st.write(income_statement_data)

# Cash Flow
# st.subheader('Cash Flow')
# cash_flow = stock.cashflow
# cf = cash_flow.T.iloc[2:]  # Skip the first two rows for headers and unnecessary data
# cf.columns = list(cash_flow.T.iloc[0])  # Set columns to the first row of transposed data
# st.write(cf)


# with pricing_data:
    # st.write(data)
    #st.write('Price')
    #data2 = data
    #data2['% Change'] = data2['Adk Close'] / data2['Adj Close'].shift(1)
    #data2.dropna(inplace=True)      
    #st.write(data2)
    #annaulized_return = (data2['% Change'].mean()*252*100


# with fundamental_data:
    # st.write('Fundamental')
    # stock = yf.Ticker(ticker)

# with news:
    # st.write('Top 10 News will be displayed here.')
    
