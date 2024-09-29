import streamlit as st
import requests
from config import fastapi_url


st.title("Sales Prediction and Forecasting Application")

response = requests.get(fastapi_url)
data = response.json()

# Display the app description
st.markdown(data["description"])

# Key Features Section
st.header("Key Features")

# Item-Level Sales Prediction
st.subheader("Item-Level Sales Prediction")
st.markdown("""
- **Predict Sales for Specific Items**: Allows users to predict sales for specific items within individual stores.
- **Advanced Algorithms**: Utilizes historical sales data and sophisticated algorithms to provide accurate forecasts.
- **Inventory Management**: Helps in inventory management and strategic planning for promotions.
- **Usage**: Navigate and click on Predict Sales on the left panel to use this feature.
""")

# Total Sales Forecasting
st.subheader("Total Sales Forecasting")
st.markdown("""
- **Store-Wide Forecasting**: Offers forecasts of total sales across all products in a store over specified periods.
- **Performance Assessment**: Enables businesses to assess overall performance and identify trends.
- **Data-Driven Decisions**: Supports data-driven decision-making for resource allocation and budget planning.
- **Usage**: Navigate anc click on Forecast Sales on the left panel to use this feature.
""")


st.markdown("### Click Below for the API endpoints details.")

if st.button('API End Points Details'):
    # Loop through each endpoint and display the information
    for endpoint in data["endpoints"]:
        st.subheader(f"Endpoint: {endpoint['path']}")
        st.write(f"**Method:** {endpoint['method']}")
        st.write(f"**Description:** {endpoint['description']}")
        
        # Check if the endpoint has additional params or expected output
        if "params" in endpoint:
            st.write(f"**Params:** {endpoint['params']}")
        if "API request" in endpoint:
            st.write("**API Request Example:**")
            st.json(endpoint["API request"])
        if "expected_output" in endpoint:
            st.write("**Expected Output:**")
            st.json(endpoint["expected_output"])

