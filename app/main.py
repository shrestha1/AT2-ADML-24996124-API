import streamlit as st

pg = st.navigation([st.Page("home.py"), st.Page("health.py"), st.Page("forecast_sales.py"), st.Page("predict_sales.py")])

pg.run()