import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
import plotly.express as px

# Set the title of the Streamlit app
st.title('Stock Dashboard')

# Sidebar for user input
ticker = st.sidebar.text_input('Ticker Symbol', 'AAPL')
start_date = st.sidebar.date_input('Start Date', dt.date(2020, 1, 1))
end_date = st.sidebar.date_input('End Date', dt.date(2021, 1, 1))

# Validate the ticker symbol and date range
if ticker:
    try:
        # Download the data
        data = yf.download(ticker, start=start_date, end=end_date)

        # Check if the data is empty
        if data.empty:
            st.error("No data found for the specified ticker and date range. Please check the ticker symbol and date range.")
        else:
            # Plot the data using Plotly
            fig = px.line(data, x=data.index, y='Adj Close', title=f'{ticker} Adjusted Close Price')
            st.plotly_chart(fig)

            # Calculate the daily percentage change
            data['% Change'] = data['Adj Close'].pct_change() * 100
            data.dropna(inplace=True)

            # Display the data with percentage change
            st.write(data)

            # Calculate the annualized return
            annualized_return = (data['% Change'].mean() * 252)
            st.write(f'Annualized Return: {annualized_return:.2f}%')

            # Create tabs for different data sections
            tab1, tab2, tab3 = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

            # Pricing Data tab
            with tab1:
                st.write('Pricing Data')
                st.write(data)

            # Fundamental Data tab
            with tab2:
                st.write('Fundamental Data')
                # You can add fundamental data here

            # Top 10 News tab
            with tab3:
                st.write('Top 10 News')
                # You can add news data here

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please enter a ticker symbol.")
