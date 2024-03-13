import streamlit as st
import joblib 
import pandas as pd
import os as os
import datetime



# Set page configuration
st.set_page_config(
    page_title='Models',
    page_icon=':)',
    layout = 'wide',
)

# Cache resource for model loading
st.cache_resource(show_spinner  ='Model Loading')
def load_decision():
     pipeline = joblib.load('models/decision_tree_balanced.joblib')
     return pipeline


st.cache_resource(show_spinner='Model Loading')    
def load_nb():
     pipeline = joblib.load('models/nb_classifier.joblib')
     return pipeline



# Function to select model based on user input
def select_model():
     
    col1, col2 = st.columns(2)

    with col1:
          st.selectbox('Select a Model',  options=['Decision Tree', 'Naive Bayes'], key='selected_model')
    with col2:
          pass
    
    if st.session_state['selected_model'] == 'Decision Tree':
        pipeline =   load_decision()
    else:
        pipeline = load_nb()

    encoder = joblib.load('models\label_encoder.joblib')

    return pipeline, encoder 

# Check if the 'prediction' key is already in session state
if 'prediction' not in st.session_state:
    # Initialize the 'prediction' key with a default value
    st.session_state['prediction'] = None

# Now you can safely access the 'prediction' key
prediction = st.session_state['prediction']

# Check if the 'probability' key is already in session state
if 'probability' not in st.session_state:
    # Initialize the 'probability' key with a default value
    st.session_state['probability'] = None

if not os.path.exists('./data/history.csv'):
         os.mkdir("./data/")


# Function to make prediction
def make_prediction(pipeline, encoder):
 
 # Extract input features from session state
    gender = st.session_state['gender']
    senior_citizen = st.session_state['SeniorCitizen']
    dependents = st.session_state['Dependents']
    partner = st.session_state['Partner']
    payment_method = st.session_state['PaymentMethod']
    contract = st.session_state['Contract']
    tenure = st.session_state['tenure']
    internet_service = st.session_state['InternetService']
    online_security = st.session_state['OnlineSecurity']
    online_backup = st.session_state['OnlineBackup']
    monthly_charges = st.session_state['MonthlyCharges']
    total_charges = st.session_state['TotalCharges']
    multiple_lines = st.session_state['MultipleLines']
    streaming_tv = st.session_state['StreamingTV']
    streaming_movies = st.session_state['StreamingMovies']
    phone_service = st.session_state['PhoneService']
    paperless_billing = st.session_state['PaperlessBilling']
    tech_support = st.session_state['TechSupport']
    device_protection = st.session_state['DeviceProtection']
    
 # Create DataFrame with input data
    columns = [ 'gender', 'SeniorCitizen', 'Dependents', 'Partner', 'PaymentMethod', 'Contract',
        'tenure', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'MonthlyCharges', 'TotalCharges',
        'MultipleLines', 'StreamingTV', 'StreamingMovies', 'PhoneService', 'PaperlessBilling', 'TechSupport', 'DeviceProtection'
    ]
    data = [[ gender, senior_citizen, dependents, partner, payment_method, contract, tenure, internet_service, online_security, online_backup, monthly_charges, total_charges, 
        multiple_lines, streaming_tv, streaming_movies,   phone_service, paperless_billing, tech_support, device_protection  ]]
    
    df2 = pd.DataFrame(data, columns=columns)

    df2['Prediction Time '] = datetime.date.today()

    df2.to_csv('./data/history.csv', mode='a', header=not os.path.exists('./data/history.csv'), index=False)

# Make prediction using pipeline
    pred = pipeline.predict(df2)
    prediction =  int(pred[0])

 # Inverse transform prediction using encoder
    prediction = encoder.inverse_transform([prediction])
    probability = pipeline.predict_proba(df2)

    st.session_state['prediction'] = prediction
    st.session_state['probability'] = probability

# Store prediction in session state
    return  prediction, probability
     

# Function to create the prediction form
def pred_form():
   
    with st.form('input-feature'):
        # Select model and load encoder
        pipeline, encoder = select_model()


# Divide form into three columns         
        col1, col2, col3 = st.columns(3)

 # Column 1: Personal Information
        with col1:
              
              st.write('### Personal Information')
              st.selectbox('Gender', ['Male', 'Female'],  key='gender')
              st.selectbox('Senior Citizen', [False, True], key='SeniorCitizen')
              st.selectbox('Dependents', [False, True], key='Dependents')
              st.selectbox('Partner', [False, True], key='Partner')
              st.selectbox('Payment Method', ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'], key='PaymentMethod')
              st.selectbox('Contract', ['Two year', 'One year', 'Month-to-month'], key='Contract')

# Column 2: User Information
        with col2:
              st.write('### User Information')
              st.number_input('Tenure', min_value=0, max_value=72, step=1, value=0, key='tenure')
              st.selectbox('Internet Service', ['DSL', 'Fiber optic', 'No'], key='InternetService')
              st.selectbox('Online Security', [False, True], key='OnlineSecurity')
              st.selectbox('Online Backup', [False, True], key='OnlineBackup')
              st.number_input('Monthly Charges', min_value=18.399999618530277, max_value=118.6500015258789, key='MonthlyCharges')
              st.number_input('Total Charges', min_value=18.799999237060547, max_value=8670.099609375, key='TotalCharges')


# Column 3: Satisfaction Information 
        with col3:
              st.write('### Satisfaction Information')
              st.selectbox('Multiple Lines', [False, True], key='MultipleLines')
              st.selectbox('Streaming TV', [False, True], key='StreamingTV')
              st.selectbox('Streaming Movies', [False, True], key='StreamingMovies')
              st.selectbox('Phone Service', [False, True], key='PhoneService')
              st.selectbox('Paperless Billing', [False, True], key='PaperlessBilling')
              st.selectbox('Tech Support', [False, True], key='TechSupport')
              st.selectbox('Device Protection', [False, True], key='DeviceProtection')

# Submit button to make prediction
        st.form_submit_button('Submit', on_click=make_prediction, kwargs=dict(pipeline=pipeline, encoder=encoder))

if __name__=="__main__":
    st.title('Make a Prediction')
    pred_form()

    # Display final prediction and session state
    # final_prediction = st.session_state['prediction']
    # st.markdown(f'The predicted outcome is: **{final_prediction[0]}**')

    prediction = st.session_state['prediction']
    probability = st.session_state['probability']

    if not prediction:
        st.markdown("### Prediction will show here")

    elif prediction == "Yes":
        probability_of_yes = probability[0][1] * 100
        st.markdown(f"### The employee will leave the company with a probability of {probability_of_yes}%")

    else:
        probability_of_no = probability[0][0]
        st.markdown(f"### Employee will not leave with a probability of {probability_of_no}%")
         

    st.write(st.session_state)
