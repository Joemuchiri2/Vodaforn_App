import streamlit as st
import pandas as pd
import numpy as np 
from PIL import Image

st.set_page_config(
    page_title= 'Home',
    page_icon= ':)',
    layout= 'wide'
)

st.title('Welcome to my Data Science Project Looking at the Vodafone Customer Churn Project')

img = Image.open("C:\\Users\\Admin\\OneDrive\\Vodaforn_App\\Files\\churn-prediction-telecom-1000x550.jpg")
st.image(img, width=None, use_column_width=True)

st.subheader('Customer Churn is the percentage of customers that stopped using a company\'s product or service '
         'during a certain time frame. Understanding the primary cause of customer churn can help businesses '
         'create a retention strategy to reduce churn and boost revenue.')

df = pd.read_csv('Files/vodafone_customer_churn.csv')

st.dataframe(df)

