import pandas as pd
import streamlit as st

def page_three():
    data_2 = pd.read_csv('data/total_data_3.csv').tail(480)
    data_2[['date', 'time']] = data_2['created_at'].str.split('T').to_list()
    data_2['time'] = data_2['time'].apply(lambda x: x[:5])
    data_2 = data_2.set_index(keys='time')

    data_2.rename(columns={'field1': 'temperature'}, inplace=True)
    data_2.rename(columns={'field2': 'humidity'}, inplace=True)
    data_2.rename(columns={'field3': 'Lux'}, inplace=True)

    data_2 = data_2.drop(['entry_id', 'created_at'], axis=1)

    st.title(f'chamber 3')

    st.header('온도')
    st.line_chart(data=data_2['temperature'], width=500, height=500)
    st.header('습도')
    st.line_chart(data=data_2['humidity'], width=500, height=500)
    st.header('광도')
    st.line_chart(data=data_2['Lux'], width=500, height=500)

    if st.checkbox('show raw data'):
        st.subheader('raw data')
        st.write(data_2)