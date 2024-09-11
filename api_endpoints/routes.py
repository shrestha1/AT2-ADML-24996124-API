'''
File: routes.py

Purpose:
    This script contains the backend build using fastapi. All the needed api endpoints would be listed here.


'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    data = {
        "description": "",
        "endpoints": [],

    }
    return 


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

@app.get("/sales/stores/items/")
def predict(date, store_id, item_id):
    '''
        Returns predicted sales for the following expected input parameters
        Args:
            date:
            store_id:
            item_id:

    '''

    return
