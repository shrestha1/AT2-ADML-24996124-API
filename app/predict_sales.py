## Prediction
## 

import streamlit as st
import requests
import datetime
import data
from config import fastapi_url


st.header("Item-Level Sales Prediction")

user_date = st.date_input("Select Date",  value = datetime.date(2015, 4, 12),
                            min_value = datetime.date(2015, 1, 1),
                            max_value = datetime.date(2025, 1, 12)
                            )

state_list = list(data.state_store.keys())

# state_id
st.info("To create the **Store ID**, select the State and Store Number.")

state = st.selectbox("Select State", state_list)
store = st.selectbox("Select Store Number", data.state_store[state])


# item_id
st.info("To create the **Item ID**, select the Category, Department, and Item Number.")

# department
cat_list = list(data.department.keys() )

# category 
category = st.selectbox("Select Category", cat_list)

department = st.selectbox("Select Department", data.department[category])

items_list = data.categories_department[category][department]
# item number
item_number = st.selectbox("Select Item Number", items_list)

# Constructing Store ID and Item ID
store_id = f"{state}_{store}"
item_id = f"{category}_{department}_{item_number:03}"


if st.button('Predict'):
    headers = {'Content-Type': 'application/json'}
    url = fastapi_url+'sales/stores/items/'
    
    json_data = {
        "date":user_date.strftime('%Y-%m-%d'),
        "store_id":store_id,
        "item_id":item_id
    }
    st.write("Json Data Sent to API:")
    st.json(json_data)  # Neater format for JSON display

    try:
        response = requests.get(url, params=json_data, headers=headers)
        
        # Check if the response is successful
        if response.status_code == 200:
            
            predicted_sales = response.json().get('prediction')
            st.success(f"Predicted Sales Price: {predicted_sales}")
            st.json(response.json())
        else:
            st.error(f"Error {response.status_code}: Unable to get prediction. Please check input values or try again.")
        
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while making the request: {e}")