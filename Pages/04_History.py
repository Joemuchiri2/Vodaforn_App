import streamlit as st
import pandas as pd

st.set_page_config(
    page_title='History',
    page_icon='',
    layout='wide'
)

st.title('Prediction History')

def history():
    csv_path = "./data/history.csv"
    hist =  pd.read_csv(csv_path)

    return hist


if __name__ =="__main__":
  hist =   history()
  st.dataframe(hist)