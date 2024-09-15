'''
File: routes.py

Purpose:
    This script contains the backend build using fastapi. All the needed api endpoints would be listed here.


'''

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle
import sklearn
from datetime import datetime

app = FastAPI()


with open('../models/predictive/final.pkl', 'rb') as file:
    model = pickle.load(file)

@app.get("/")
def read_root():
    data = {
        "description": "This is a FastAPI application.",
        "endpoints": [
            {"path": "/items/{item_id}", "method": "GET", "description": "Get item by ID"},
            {"path": "/items", "method": "POST", "description": "Create a new item"},
            # Add more endpoints as needed
        ]
    }
    return data


@app.get("/health/")
def read_health():
    data = {

    }
    return


@app.get("/sales/national/")
def forecast(date):
    '''
        Returns next 7 days forecasted sales 

    '''
    return

# Define a function to simulate prediction
def predict_sales(date: str, store_id: int, item_id: int) -> float:
    date = datetime.strptime(date, "%Y-%m-%d")

    try:
        date = pd.to_datetime(date)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD.")

    # Extract features from the date
    month = date.month
    week = date.isocalendar()[1]
    day_of_week = (date.weekday() + 1) % 7  # Adjust so Sunday = 0
    
    # Prepare the input data for prediction
    input_data = np.array([[month, week, day_of_week, store_id, item_id]])

    # Predict the sales
    try:
        predicted_sell_price = round(model.predict(input_data)[0],2)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error predicting sales: {str(e)}")

    # Return the prediction
    return {"prediction": predicted_sell_price}



@app.get("/sales/stores/items/")
async def get_sales_prediction( date: str,
    store_id: int,
    item_id: int):
    
    
    # Return the response as JSON
    return predict_sales(date, store_id, item_id)
