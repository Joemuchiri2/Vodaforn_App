import streamlit as st
from PIL import Image
import pandas as pd
import csv

st.title('Welcome to my Data Science Project Looking at the Vodafone Customer Churn Project')

img = Image.open("C:\\Users\\Admin\\OneDrive\\Vodaforn_App\\Files\\churn-prediction-telecom-1000x550.jpg")
st.image(img, width=None, use_column_width=True)

st.subheader('Customer Churn is the percentage of customers that stopped using a company\'s product or service '
             'during a certain time frame. Understanding the primary cause of customer churn can help businesses '
             'create a retention strategy to reduce churn and boost revenue.')

#button to view the dataset
if st.button('View Dataset'):
    df = pd.read_csv('Files/vodafone_customer_churn.csv')
    st.write(df)

# Streamlit UI code
st.subheader('Share Your Feedback')
feedback = st.text_area('What do you think about this project?', height=100)
if st.button('Submit Feedback'):
    with open('feedback.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([feedback])
    st.success('Thank you for your feedback! It has been saved.')

# Add links to GitHub, LinkedIn, Medium, etc.
st.markdown('**Source Code:** [GitHub](https://github.com/yourusername/yourproject)')
st.markdown('**LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/yourusername)')
st.markdown('**Medium:** [Your Medium Profile](https://medium.com/@yourusername)')
