import streamlit as st
import pyodbc
import pandas as pd

st.set_page_config(
    page_title='View Data',
    page_icon='',
    layout ='wide'
)

st.title ('Proprietory Data from IBM')

@st.cache_resource(show_spinner='Connecting to Database.....')
def initialize_conn():
    
    connection = pyodbc.connect(
        "DRIVER={SQL Server}; SERVER="
        + st.secrets['server']
        +";DATABASE="
        + st.secrets['database_name']
        +";UID="
        + st.secrets['username']
        +";PWD="
        + st.secrets['password']
    )
    
    return connection


conn = initialize_conn()


@st.cache_data()
def database_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        
    

        df =  pd.DataFrame.from_records(data=rows, columns=[column [0] for column in cur.description])

    return df

@st.cache_data()
def select_features():
    query = "Select * FROM dbo.LP2_Telco_churn_first_3000"
    df =  database_query(query)

    return df

def select_numerical_features():
    query = "Select * FROM dbo.LP2_Telco_churn_first_3000"
    df =  database_query(query)

    return df



if __name__ == "__main__":
    col1, col2 = st.columns(2)

    with col1:
        st.selectbox("Select the type of features", 
                    options=["All Features", "Numerical Features"],
                    key = "select_columns")

    with col2:
        pass

    if st.session_state['select_columns'] =="All Features":
        data = select_features()
        st.dataframe(data)

    # st.write(st.session_state)

    