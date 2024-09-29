import streamlit as st
import requests
from config import fastapi_url

st.header("API Running Test")

if st.button('Health'):
   response = requests.get(fastapi_url+"/health/")
   data = response.json()
   
   if data[1] == 200:
     st.write(data[0])
   else:
     st.markdown("Application is not working") 
   
#    st.write(response.json())