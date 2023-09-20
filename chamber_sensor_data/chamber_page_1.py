import os

import pandas as pd
import streamlit as st
from download import download_selected_data_csv
import requests
from download import download_csv

def page_one():
    data_2 = pd.read_csv(rf'C:\code\chamber_sensor_data\data\total_data_1.csv')
    data_2[['date', 'time']] = data_2['created_at'].str.split('T').to_list()
    data_2['time'] = data_2['time'].apply(lambda x: x[:5])
    data_2 = data_2.set_index(keys='time')
    data_2.rename(columns={'field1': 'temperature'}, inplace=True)
    data_2.rename(columns={'field2': 'humidity'}, inplace=True)
    data_2.rename(columns={'field3': 'Lux'}, inplace=True)

    data_2 = data_2.drop(['entry_id', 'created_at'], axis=1)

    data = data_2.tail(480)

    st.title(f'chamber 1')

    st.header('온도')
    st.line_chart(data=data['temperature'], width=500, height=500)
    st.header('습도')
    st.line_chart(data=data['humidity'], width=500, height=500)
    st.header('광도')
    st.line_chart(data=data['Lux'], width=500, height=500)

    if st.checkbox('show raw data'):
        st.subheader('raw data')
        st.write(data)

    data_dir = rf'C:\code\chamber_sensor_data\data'
    csv_file_path_1 = os.path.join(data_dir, "total_data_1.csv")

    download_selected_data_csv(data_2)
    download_csv(csv_file_path_1)

    st.subheader("센서 알림")


    if st.button("온도 높음"):
        requests.post("https://ntfy.sh/Chamber-Sensor", data="온도 높음 주의".encode(encoding='utf-8'))

    if st.button("온도 낮음"):
        requests.post("https://ntfy.sh/Chamber-Sensor", data="온도 낮음 주의".encode(encoding='utf-8'))

    if st.button("습도 높음"):
        requests.post("https://ntfy.sh/Chamber-Sensor", data="습도 높음 주의".encode(encoding='utf-8'))


