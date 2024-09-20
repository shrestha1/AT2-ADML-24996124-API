# ''' api request data
#     {

#          "date": "2024-09-16",

#         "store_id": "WI_1",

#         "item_id": "HOBBIES_1_001"

# } 
# '''
import pandas as pd
import numpy as np
from fastapi import HTTPException
from datetime import datetime

# ['month', 'weekday', 'state', 'store_num', 'category', 'department', 'item']

def extract_date_feature(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    try:
        date = pd.to_datetime(date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    # Extract features from the date
    month = date.month
    weekday = date.weekday()

    return month, weekday
    
    

def extract_item_feature(item_id):
    category_encoding = {
        'FOODS': 0,
        'HOBBIES': 1,
        'HOUSEHOLDS':2
    }
    category, department, item = item_id.split('_')

    return int(department), category_encoding[category], int(item) 

def extract_store_feature(store_id):
    state_encoding = {
        'WI' : 0
    }
    state, store_num = store_id.split("_")
    return state_encoding[state], int(store_num)

def extract_features(date, store_id, item_id):
    month, weekday = extract_date_feature(date)
    state, store_num = extract_store_feature(store_id)
    department, category, item = extract_item_feature(item_id)
    return np.array([[month, weekday, state, store_num, category, department, item]])
    

