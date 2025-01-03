import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")
upload_file= st.file_uploader("Chose a CSV file",type="CSV")
if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns= st.selectbox("select colum to filter by", columns)
    unique_value = df[selected_columns].unique()
    selected_value = st.selectbox("select value",unique_value)

    filtered_df = df[df[selected_columns] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("select x_axis column",columns)
    y_column = st.selectbox("select y_axis column",columns)

    
    # st.write("File uploaded.....")
# st.write("hello world")
# st.write({"key": ["value"]})
# check git hub