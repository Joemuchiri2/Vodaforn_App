import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from PIL import Image
import pandas as pd
import csv

st.set_page_config(
    page_title='Vodafone Churn Analysis',
    layout='wide',
    page_icon='📊'
)

# Authentication setup
with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login(location='sidebar')

if authentication_status:
    authenticator.logout(location='sidebar', key='logout-button')

    st.title('Welcome to my Data Science Project Looking at the Vodafone Customer Churn Project')

    img = Image.open("C:\\Users\\Admin\\OneDrive\\Vodaforn_App\\Files\\churn-prediction-telecom-1000x550.jpg")
    st.image(img, width=None, use_column_width=True)

    
    import streamlit as st

column_1 = """
### Customer Churn
It is the percentage of customers that stopped using a company's product or service during a certain time frame. Understanding the primary cause of customer churn can help businessescreate a retention strategy to reduce churn and boost revenue 

### Key Features
- **View Data:** Access proprietary data from IBM.
- **Dashboard:** Explore interactive data visualizations for insights.
- **Real-time Prediction:** Instantly see predictions for employee attrition.
- **History:** See past predictions made.

### User Benefits
- **Data-driven Decisions:** Make informed decisions backed with data analytics.
- **Easy Machine Learning:** Utilize powerful machine learning algorithms effortlessly.


"""

column_2 = """
### Machine Learning Integration
- **Model Selection:** Choose between two advanced models for accurate predictions.
- **Seamless Integration:** Integrate predictions into your workflow with a user-friendly interface.
- **Probability Estimates:** Gain insights into the likelihood of predicted outcomes.
"""

st.title('Welcome to my Data Science Project Looking at the Vodafone Customer Churn Project')

# Display the columns with additional content
col1, col2 = st.columns(2)
with col1:
    st.markdown(column_1, unsafe_allow_html=True)
with col2:
    st.markdown(column_2, unsafe_allow_html=True)

# Rest of your Streamlit UI code (e.g., dataset viewing, feedback form, etc.)


    # Button to view the dataset
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



    
    elif authentication_status is None:
        st.info('Enter username and password to use the app.')
        st.code("""
            Test Account
            Username: joemuchy2
            Password: 654321""")

    elif not authentication_status:
       st.error('Username/password is incorrect')



    # Add links to GitHub, LinkedIn, Medium, etc.
st.markdown('**Source Code:** [GitHub](https://github.com/Joemuchiri2/Vodaforn_App.git)')
st.markdown('**LinkedIn:** [Your LinkedIn Profile](www.linkedin.com/in/josephmuchiri337)')
st.markdown('**Medium:** [Your Medium Profile](https://medium.com/@muchirijoseph337/deploying-machine-learning-models-with-streamlit-91ad889578e1)')
