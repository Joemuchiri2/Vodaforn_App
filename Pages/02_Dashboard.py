import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)





st.set_page_config(
    page_title='Dashboard',
    page_icon='',
    layout ='wide'
)

st.title ('# Vodafone Customer Churn :chart :bar_chart :phone ')
st.markdown("Vodafone Customer Churn Dashboard lets look at the data that we will be intreacting with in this project!")


df = pd.read_csv('Files/vodafone_customer_churn.csv')



# Start building your EDA dashboard
st.title('Vodafone Churn Project - EDA Dashboard')

# Display the dataset
st.subheader('Raw Data')
st.write(df)

container = st.container()
col1, col2 = container.columns(2)

with col1:
    st.subheader('Basic Information')
    st.write(f"Number of rows: {len(df)}")
    st.write(f"Number of columns: {len(df.columns)}")
    st.write(f"Column names: {', '.join(df.columns)}")
    st.write(f"Data types:\n{df.dtypes}")

with col2:
    # Show basic statistics
    st.subheader('Basic Statistics')
    st.write(df.describe())



# Show a bar chart of the 'Gender' column
st.subheader('Gender Distribution')
gender_counts = df['Gender'].value_counts()
fig, ax = plt.subplots(figsize=(8, 6))
sns.barplot(x=gender_counts.index, y=gender_counts.values, ax=ax)
ax.set_xlabel('Gender')
ax.set_ylabel('Count')
ax.set_title('Gender Distribution')
st.pyplot(fig)


# Show a bar chart of the 'Contract' column
st.subheader('Contract Types')
contract_counts = df['Contract'].value_counts()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=contract_counts.index, y=contract_counts.values, ax=ax)
ax.set_xlabel('Contract Type')
ax.set_ylabel('Count')
ax.set_title('Contract Types')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)






container = st.container()
col1, col2 = container.columns(2)

with col1:
    pass

with col2:
    pass




