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
import pickle

# ['month', 'weekday', 'state', 'store_num', 'category', 'department', 'item']

def extract_date_feature(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    try:
        date = pd.to_datetime(date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    # Extract features from the date
    year = date.year
    month = date.month
    day = date.day
    weekday = date.weekday()

    return year, month, day, weekday
    
    

def extract_item_feature(item_id):
    
    category, department, item = item_id.split('_')

    return int(department), category, int(item) 

def extract_store_feature(store_id):
    
    state, store_num = store_id.split("_")
    return state, int(store_num)

def extract_features(date, store_id, item_id):
    year, month, day,  weekday = extract_date_feature(date)
    state, store_num = extract_store_feature(store_id)
    department, category, item = extract_item_feature(item_id)
    df = pd.DataFrame({
        'year': [year],
        'month': [month],
        'day': [day],
        'weekday': [weekday],
        'state': [state],
        'store_num': [store_num],
        'department': [department],
        'category': [category],
        'item': [item]
    })
    
    with open('./models/predictive/pipeline_ohe.pkl', 'rb') as file:
        loaded_pipeline = pickle.load(file)
    
    df_encoded = loaded_pipeline.transform(df)

    return df_encoded.to_numpy()
    

