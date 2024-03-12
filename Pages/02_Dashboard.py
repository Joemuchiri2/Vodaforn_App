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



container = st.container()
col1, col2 = container.columns(2)

with col1:
    # Show a bar chart of the 'Gender' column
    st.subheader('Gender Distribution')
    gender_counts = df['gender'].value_counts()
    fig_gender, ax_gender = plt.subplots(figsize=(8, 6))
    sns.barplot(x=gender_counts.index, y=gender_counts.values, ax=ax_gender)
    ax_gender.set_xlabel('Gender')
    ax_gender.set_ylabel('Count')
    ax_gender.set_title('Gender Distribution')
    st.pyplot(fig_gender)

with col2:
    # Show a bar chart of the 'Contract' column
    st.subheader('Contract Types')
    contract_counts = df['Contract'].value_counts()
    fig_contract, ax_contract = plt.subplots(figsize=(10, 6))
    sns.barplot(x=contract_counts.index, y=contract_counts.values, ax=ax_contract)
    ax_contract.set_xlabel('Contract Type')
    ax_contract.set_ylabel('Count')
    ax_contract.set_title('Contract Types')
    ax_contract.set_xticklabels(ax_contract.get_xticklabels(), rotation=45)
    st.pyplot(fig_contract)




import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_clv(df):
    # Assuming CLV is the sum of Total Charges for each customer
    return df.groupby('customerID')['TotalCharges'].sum().mean()

# Define the calculate_retention_rate function
def calculate_retention_rate(df):
    # Assuming RetentionRate is a column in your DataFrame
    return df['Churn'].mean() * 100

# Define the calculate_arpu function
def calculate_arpu(df):
    # Assuming ARPU is calculated as the mean of 'MonthlyCharges'
    return df['MonthlyCharges'].mean()




# Calculate KPIs
churn_rate = df['Churn'].mean() * 100
clv = calculate_clv(df)
retention_rate = calculate_retention_rate(df)
arpu = calculate_arpu(df)


# Display KPIs
st.title('Vodafone Churn Project - KPIs Dashboard')

st.subheader('Key Performance Indicators')
st.write(f"Churn Rate: {churn_rate:.2f}%")
st.write(f"Customer Lifetime Value: ${clv:.2f}")
st.write(f"Customer Retention Rate: {retention_rate:.2f}%")
st.write(f"Average Revenue Per User: ${arpu:.2f}")


# Visualize KPIs
st.subheader('Visualizations')
fig, axes = plt.subplots(2, 2, figsize=(12, 8))

# Churn Rate
sns.histplot(df['Churn'], bins=2, ax=axes[0, 0])
axes[0, 0].set_title('Churn Rate')

# CLV Distribution
sns.histplot(df['TotalCharges'], bins=30, ax=axes[0, 1])
axes[0, 1].set_title('Customer Lifetime Value Distribution')


# ARPU Distribution
sns.histplot(df['MonthlyCharges'], bins=30, ax=axes[1, 1])
axes[1, 1].set_title('Average Revenue Per User Distribution')

st.pyplot(fig)





