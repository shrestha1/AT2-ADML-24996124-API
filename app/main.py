"""
File: main.py

Purpose:
    This script is main python file that run the streamlit application
"""

import streamlit as st
import requests
import datetime

st.title('ML Streamlit App')

# while testing with local system docker
fastapi_url = 'http://backend:8000/'

# while testing with deployed docker 
# remote_fastapi_url = ''
# fastapi_url = remote_fastapi_url


## while test in local device without docker
# local_url = 'http://127.0.0.1:8000/'
# fastapi_url = local_url

st.header("Testing API")

if st.button('Test'):
   response = requests.get(fastapi_url)
   
   st.write(response.json())


## Prediction
## 
st.header("Prediction of the Sales of Item in a Store for Selected Date. ")
user_date = st.date_input("Select Date",  value = datetime.date(2017, 1, 1),
                            min_value = datetime.date(2017, 1, 1),
                            max_value = datetime.date(2025, 1, 12)
                            )

categories = {
    "FOODS": ["001", "002", "003", "004", "005"],
    "HOBBIES": ["001", "002", "003", "004", "005"],
    "HOUSEHOLDS": ["001", "002", "003", "004", "005"]
}




# state_id
state = st.selectbox("Select State", ["WI"])
store = st.selectbox("Select Store", list(range(1,4)))


# item_id
# department
department = st.selectbox("Select Department", list(range(1, 6)))

# category 
category = st.selectbox("Select Category", ["FOODS", "HOBBIES", "HOUSEHOLDS"])

# item number
item_number = st.selectbox("Select Item Number", categories[category])

store_id = state+"_"+str(store)
item_id = category+"_"+str(department)+"_"+ item_number

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
    st.write(response.json())

    # Check if the response is successful
    if response.status_code == 200:
        # Parse and display the JSON response
        predicted_sales = response.json().get('prediction')
        st.write(f"Predicted Sales Price: {predicted_sales}")
    else:
        st.write(f"Error {response.status_code}: Unable to get prediction. Please check input values or try again.")
