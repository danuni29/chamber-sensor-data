import streamlit as st
import datetime


def download_csv(file_path):
    with open(file_path, "rb") as f:
        csv_data = f.read()
    st.download_button(label="Download All Data", data=csv_data, file_name="data.csv")

def download_selected_data_csv(df):
    dates = list(df['date'].unique())

    start_date = datetime.datetime.strptime(dates[0], "%Y-%m-%d")
    end_date = datetime.datetime.strptime(dates[-1], "%Y-%m-%d")
    choose_date = st.slider('Select date range', min_value=start_date, value=[start_date, end_date],
                            max_value=end_date, format="YY/MM/DD")

    selected_start_date = choose_date[0].strftime("%Y-%m-%d")
    selected_end_date = choose_date[1].strftime("%Y-%m-%d")

    selected_date_range = df[(df['date'] >= selected_start_date) & (df['date'] <= selected_end_date)]

    selected_data_csv = selected_date_range.to_csv(index=False)
    st.download_button(label="Download Selected Data", data=selected_data_csv, file_name="selected_data.csv")
