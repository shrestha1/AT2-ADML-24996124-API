## Forecasting 
##
import streamlit as st
import requests
import datetime
from config import fastapi_url


st.header("Total Sales Forecast")

user_date = st.date_input("Select Date",  value = datetime.date(2015, 4, 12),
                            min_value = datetime.date(2015, 1, 1),
                            max_value = datetime.date(2016, 12, 29)
                            )

# Forecast Button
if st.button('Forecast'):
    # loading spinner while waiting for the response
    with st.spinner('Fetching forecast...'):
        headers = {'Content-Type': 'application/json'}
        url = fastapi_url + 'sales/national/'

        json_data = {
            "date": user_date.strftime('%Y-%m-%d'),
        }

        try:
            # GET request with the parameters
            response = requests.get(url, params=json_data, headers=headers, timeout=10)

            # Check if the response is successful
            if response.status_code == 200:
                result = response.json()
                st.success("Forecast retrieved successfully!")
                
                st.write("Forecast for 7 days from the selected date:")
                st.json(result) 

            else:
                st.error(f"Error {response.status_code}: Unable to fetch forecast.")

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")