'''
File: routes.py

Purpose:
    This script contains the backend build using fastapi. All the needed api endpoints would be listed here.


'''

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle
import sklearn
from datetime import datetime
import utils
import re
import gzip
import json

app = FastAPI()


def validate_date_format(date_str: str) -> bool:
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date_str))


with gzip.open('./models/predictive/compressed_decision_tree_final_tuned.pkl', 'rb') as f:
    p = pickle.Unpickler(f)
    prediction_model = p.load()

# with open('./models/predictive/compressed_decision_tree_final_tuned.pkl', 'rb') as file:
#     prediction_model = pickle.load(file)

with open('./models/forecasting/prophet_forecast_seasonality_holiday.pkl', 'rb') as file:
    np.float_ = np.float64
    forecast_model = pickle.load(file)

@app.get("/")
def read_root():
    data = {
        "description": "This application can be used for two purpose: Prediction of sales of an item in particular store and Forecasting the total sales of overall store.",
        "endpoints": [
            {"path": "/", "method": "GET", "description": "Get Overview of the project and API Documentation"},
            {"path": "/health/", "method": "GET", "description": "Checking the status of the API."},
            {"path": "/sales/national/", "method": "GET", 
             "description": "Returns the forcasted sales of 7 days from the selected date.", 
             "params": "Takes date as an input to the and provides forecasted sales each of 7 days onwards.", 
             "expected_output": {
                            "2015-04-12":112668.73,
                            "2015-04-13":112698.91,
                            "2015-04-14":112729.08,
                            "2015-04-15":112759.25,
                            "2015-04-16":112789.43,
                            "2015-04-17":112819.6,
                            "2015-04-18":112849.77}
        },
        {"path": "/sales/national/", "method": "GET", 
             "description": "Returns the forcasted sales of 7 days from the selected date.", 
             "params": "From UI Date, Statem, Store Number, Category, Department id and Item Number is taken. From these, Json value is generated",
             "API request": {
                                "date":"datetime.date(2015, 4, 12)",
                                "store_id":"CA_1",
                                "item_id":"HOUSEHOLD_1_053"
                            }, 
             "expected_output": {"prediction":10.4}
        },
        ]
    }
    return data


@app.get("/health/")
def read_health():
    data = {
        "Health": "APP is Runnning..."
    }
    return data


@app.get("/sales/national/")
async def forecast(request:Request):
    '''
        Returns next 7 days forecasted sales 

    '''
    data = await request.json()
    date = data['date']

    if not validate_date_format(date):
        raise HTTPException(status_code=400, detail="Date must be in 'yyyy-mm-dd' format")
    
    start_date = datetime.strptime(date, "%Y-%m-%d")
    date_range = pd.date_range(start=start_date, periods=7)
    df = pd.DataFrame({'ds': date_range})

    forecast = forecast_model.predict(df)

    forecast_response = forecast[['ds', 'trend']].set_index('ds')['trend'].to_dict()
    formatted_json_data = {date.strftime('%Y-%m-%d'): round(sales, 2) for date, sales in forecast_response.items()}

    return formatted_json_data


# function to sales prediction
def predict_sales(date: str, store_id: str, item_id: str) -> float:
    if not validate_date_format(date):
        raise HTTPException(status_code=400, detail="Date must be in 'yyyy-mm-dd' format")
     
    # Prepare the input data for prediction
    input_data = utils.extract_features(date, store_id, item_id)

    # Predict the sales
    try:
        predicted_sell_price = round(prediction_model.predict(input_data)[0],2)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error predicting sales: {str(e)}")

    # Return the prediction
    return {"prediction": predicted_sell_price}



@app.get("/sales/stores/items/")
async def get_sales_prediction(request: Request):
    data = await request.json()
    date = data['date']
    store_id = data['store_id']
    item_id = data['item_id']
    # print(data)
    # # Return the response as JSON
    return predict_sales(date, store_id, item_id)
