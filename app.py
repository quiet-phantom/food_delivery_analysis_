import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Food Delivery Dashboard", layout="wide")
st.title("🍔 Food Delivery Dataset Analysis")

# Data Load
@st.cache_data
def load_data():
    df = pd.read_csv('food_delivery_dataset.csv')
    return df

try:
    df = load_data()
    st.success("Dataset successfully loaded!")

    # Overview Metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Orders", len(df))
    with col2:
        if 'Time_taken(min)' in df.columns:
            st.metric("Avg Delivery Time (min)", round(df['Time_taken(min)'].mean(), 2))

    # Data Display
    st.subheader("Data Preview")
    st.dataframe(df.head())

except Exception as e:
    st.error(f"File load nahi hui. Error: {e}")
