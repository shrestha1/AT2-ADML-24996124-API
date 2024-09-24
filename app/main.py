"""
File: main.py

Purpose:
    This script is main python file that run the streamlit application
"""

import streamlit as st
import requests
import datetime
import data


st.title('ML Streamlit App')

# while testing with local system docker
fastapi_url = 'http://backend:8000/'

# while testing with deployed docker 
# remote_fastapi_url = ''
# fastapi_url = remote_fastapi_url


## while test in local device without docker
# local_url = 'http://127.0.0.1:8000/'
# fastapi_url = local_url


st.header("Project Overview")

if st.button('Overview'):
   response = requests.get(fastapi_url)
   
   st.write(response.json())


if st.button('Health'):
   response = requests.get(fastapi_url+"/health/")
   
   st.write(response.json())
 
## Forecasting 
##
st.header("Forecasting the total Sales of 7 days from Selected Date onwards.")

user_date = st.date_input("Select Date",  value = datetime.date(2015, 4, 12),
                            min_value = datetime.date(2015, 1, 1),
                            max_value = datetime.date(2016, 12, 29)
                            )
if st.button('Forecast'):
    url = fastapi_url+'sales/national/'
    # response = requests.get()
    params = {
        "date":user_date,
    }
    response = requests.get(url, params=params)
    st.write(response.json())
    

## Prediction
## 
st.header("Prediction of the Sales of Item in a Store for Selected Date. ")
user_date = st.date_input("Select Date",  value = datetime.date(2015, 4, 12),
                            min_value = datetime.date(2015, 1, 1),
                            max_value = datetime.date(2025, 1, 12)
                            )

state_list = list(data.state_store.keys())

# state_id
state = st.selectbox("Select State", state_list)
store = st.selectbox("Select Store Number", data.state_store[state])


# item_id
# department
cat_list = list(data.department.keys() )

# category 
category = st.selectbox("Select Category", cat_list)

department = st.selectbox("Select Department", data.department[category])

items_list = data.categories_department[category][department]
# item number
item_number = st.selectbox("Select Item Number", items_list)

store_id = state+"_"+str(store)
item_id = category+"_"+str(department)+"_"+ "{:03}".format(item_number)


if st.button('Predict'):
    url = fastapi_url+'sales/stores/items/'
    # response = requests.get()
    params = {
        "date":user_date,
        "store_id":store_id,
        "item_id":item_id
    }
   # Make the GET request with the parameters
    response = requests.get(url, params=params)
    st.write("Json Data Sent:")
    st.write(params)
    st.write("Json Response obtained From API:")
    st.write(response.json())

    # Check if the response is successful
    if response.status_code == 200:
        # Parse and display the JSON response
        predicted_sales = response.json().get('prediction')
        st.write(f"Predicted Sales Price: {predicted_sales}")
    else:
        st.write(f"Error {response.status_code}: Unable to get prediction. Please check input values or try again.")
