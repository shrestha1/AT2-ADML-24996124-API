"""
File: main.py

Purpose:
    This script is main python file that run the streamlit application
"""

import streamlit as st
import requests

st.title('ML Streamlit App')

fastapi_url = 'http://backend:8000/'

if st.button('Test'):
   response = requests.get(fastapi_url)
   
   st.write(response.json())