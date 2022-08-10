# Imports
# -----------------------------------------------------------
import streamlit as st
import pandas as pd
# -----------------------------------------------------------

# Helper functions
# -----------------------------------------------------------
# Load data from external source
df = pd.read_csv(
    "https://github.com/kpsenn/newapp/blob/main/stock_data.csv"
)
# -----------------------------------------------------------

# Sidebar
# -----------------------------------------------------------

# -----------------------------------------------------------


# Main
# -----------------------------------------------------------
# Create a title for your app
st.title("Interactive K-Means Clustering-KPS")

# A description
st.write("Here is the dataset used in this analysis:")

# Display the dataframe
st.write(df)
# -----------------------------------------------------------