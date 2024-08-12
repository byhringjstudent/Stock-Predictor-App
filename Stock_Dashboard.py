import yfinance as yf
import streamlit as st
from datetime import datetime
import plotly.express as px
import numpy as np

# Sidebar dropdown for ticker symbol selection
ticker = st.sidebar.selectbox(
    "Select Stock Ticker",
    options=["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "F", "BABA", "TSM", "NVDA", "LNVGY", "BTC", "ETH", "DASH"],
    index=0
)

# Sidebar date inputs for start and end dates
start_date = st.sidebar.date_input("Start Date", value=datetime(2022, 1, 1))
end_date = st.sidebar.date_input("End Date", value=datetime(2022, 12, 31))

# Fetch the data using Yahoo Finance API
data = yf.download(ticker, start=start_date, end=end_date)
fig = px.line(data, x=data.index, y=data['Adj Close'], title=ticker)
st.plotly_chart(fig)

# Ensure the user has selected a ticker symbol and valid date range
if ticker:
    # Initialize the Ticker object
    stock = yf.Ticker(ticker)

    # Display the dashboard header
    st.title("Stock Dashboard")

    # Add tabs for different sections
    tab1, tab2, tab3 = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

    with tab1:
        st.subheader("Pricing Movements")
        data2 = data
        data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1)
        data2.dropna(inplace=True)
        st.write(data2)
        
        annualized_return = data2['% Change'].mean()*252*100
        st.write(f'Annualized Return: {annualized_return}%')
        # stdev = np.std(data2['% Change'])
        # st.write(f"Standard Deviation: {stdev}")
        stdev = np.std(data2['% Change'])*np.sqrt(252)
        st.write('Standard Devision is ', stdev*100, '%')
        st.write('Risk Adj. Return is ',annualized_return/(stdev*100))
        

    with tab2:
        st.subheader("Fundamental Data")
        try:
            # Balance Sheet
            st.subheader('Balance Sheet')
            balance_sheet = stock.balance_sheet
            bs = balance_sheet.T
            bs = bs.loc[:,~bs.columns.duplicated()]  # Drop duplicate columns
            st.write(bs)

            # Income Statement
            st.subheader('Income Statement')
            income_statement = stock.financials
            income_statement_data = income_statement.T
            income_statement_data = income_statement_data.loc[:,~income_statement_data.columns.duplicated()]  # Drop duplicate columns
            st.write(income_statement_data)

            # Cash Flow
            st.subheader('Cash Flow')
            cash_flow = stock.cashflow
            cf = cash_flow.T
            cf = cf.loc[:,~cf.columns.duplicated()]  # Drop duplicate columns
            st.write(cf)
        except Exception as e:
            st.error(f"An error occurred while fetching fundamental data: {e}")

    with tab3:
        st.subheader("Top 10 News")
        try:
            # Fetch the top news
            if (news := stock.news[:10]):
                for article in news:
                    st.write(f"### {article['title']}")
                    st.write(f"*Published on: {article['providerPublishTime']}*")
                    st.write(f"[Read more]({article['link']})")
                    st.write("Sentiment Analysis: ", article['sentiment'])
                    st.write("---")
            else:
                st.write("No news articles available for this ticker.")
        except Exception as e:
            st.error(f"An error occurred while fetching the news: {e}")
else:
    st.warning("Please select a ticker symbol and a valid date range to continue.")
