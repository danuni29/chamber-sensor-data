import streamlit as st


def download_csv(file_path):
    with open(file_path, "rb") as f:
        csv_data = f.read()
    st.download_button(label="Download CSV File", data=csv_data, file_name="data.csv")