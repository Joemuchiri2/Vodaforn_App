import streamlit as st
from PIL import Image
import pandas as pd
import csv

st.set_page_config(
    page_title='Vodafone Churn Analysis',
    layout='wide',
    page_icon='📊'
)

st.title('Welcome to my Data Science Project Looking at the Vodafone Customer Churn Project')

img = Image.open("./Files/churn-prediction-telecom-1000x550.jpg")
st.image(img, width=None, use_column_width=True)

column_1 = """
### Customer Churn
It is the percentage of customers that stopped using a company's product or service during a certain time frame. Understanding the primary cause of customer churn can help businesses create a retention strategy to reduce churn and boost revenue 

### Key Features
- **View Data:** Access proprietary data from IBM.
- **Dashboard:** Explore interactive data visualizations for insights.
- **Real-time Prediction:** Instantly see predictions for employee attrition.
- **History:** See past predictions made.
"""

column_2 = """
### Machine Learning Integration
- **Model Selection:** Choose between two advanced models for accurate predictions.
- **Seamless Integration:** Integrate predictions into your workflow with a user-friendly interface.
- **Probability Estimates:** Gain insights into the likelihood of predicted outcomes.


### User Benefits
- **Data-driven Decisions:** Make informed decisions backed with data analytics.
- **Easy Machine Learning:** Utilize powerful machine learning algorithms effortlessly.
"""

# Display the columns with additional content
col1, col2 = st.columns(2)
with col1:
    st.markdown(column_1, unsafe_allow_html=True)
with col2:
    st.markdown(column_2, unsafe_allow_html=True)

# Button to view the dataset
if st.button('View Dataset'):
    try:
        df = pd.read_csv('./Files/vodafone_customer_churn.csv')
        st.write(df)
    except FileNotFoundError:
        st.error("Dataset file not found.")

# Streamlit UI code
st.subheader('Share Your Feedback')
feedback = st.text_area('What do you think about this project?', height=100)
if st.button('Submit Feedback'):
    try:
        with open('feedback.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([feedback])
        st.success('Thank you for your feedback! It has been saved.')
    except Exception as e:
        st.error(f"Failed to save feedback: {e}")

# Add links to GitHub, LinkedIn, Medium, etc.
st.markdown('**Source Code:** [GitHub](https://github.com/Joemuchiri2/Vodaforn_App.git)')
st.markdown('**LinkedIn:** [Your LinkedIn Profile](https://www.linkedin.com/in/josephmuchiri337/)')
st.markdown('**Medium:** [Your Medium Profile](https://medium.com/@muchirijoseph337/deploying-machine-learning-models-with-streamlit-91ad889578e1)')
