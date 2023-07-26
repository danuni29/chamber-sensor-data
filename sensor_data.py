import csv
import json, urllib.request
import time
import pandas as pd
from pandas.io.json import json_normalize
import streamlit as st
from streamlit_option_menu import option_menu
from chamber_page_1 import page_one
from chamber_page_2 import page_two
from chamber_page_3 import page_three
from chamber_page_4 import page_four
from download import download_csv
# ------------- api 데이터 받아와서 csv파일로 저장 -----------------

api_key_1 = "HN55139L0VGN5XNM"
api_key_2 = "XP1R5CVUPVXTNJT0"
api_key_3 = "WAE2NS9GNFFBFH6F"
api_key_4 = "TYCQQ3CFQME0PITO"


count = 480

continent = "Asia"

city = "Seoul"

# 1번챔버
url_1 = "https://api.thingspeak.com/channels/1999882/feeds.json?" + "timezone=" + continent + "%2F" + city + "&" + \
      "api_key=" + api_key_1 + "&results=" + str(count)
# 2번챔버
url_2 = "https://api.thingspeak.com/channels/1999883/feeds.json?" + "timezone=" + continent + "%2F" + city + "&" + \
      "api_key=" + api_key_2 + "&results=" + str(count)
# 3번챔버
url_3 = "https://api.thingspeak.com/channels/1930822/feeds.json?" + "timezone=" + continent + "%2F" + city + "&" + \
      "api_key=" + api_key_3 + "&results=" + str(count)
# 4번챔버
url_4 = "https://api.thingspeak.com/channels/1999884/feeds.json?" + "timezone=" + continent + "%2F" + city + "&" + \
      "api_key=" + api_key_4 + "&results=" + str(count)

urls = [url_1, url_2, url_3, url_4]


# api 키를 이용해서 json 파일 불러오기

for i, url in enumerate(urls):
    dataset = urllib.request.urlopen(url).read()
    output = json.loads(dataset)
    output = output['feeds']
    new_data_df = pd.DataFrame(output)
    total_data = pd.read_csv(f'total_data_{i+1}.csv')

    df = pd.concat([total_data, new_data_df], ignore_index=False)
    df = df.drop_duplicates(subset='created_at', keep='last')
    df.to_csv(f'total_data_{i+1}.csv', index=False, encoding='utf-8-sig')






def main():


    st.sidebar.title("Chamber Data")
    options = ["Chamber 1", "Chamber 2", "Chamber 3", "Chamber 4"]
    choice = st.sidebar.selectbox("챔버 선택", options)

    csv_file_path_1 = "./total_data_1.csv"
    csv_file_path_2 = "./total_data_2.csv"
    csv_file_path_3 = "./total_data_3.csv"
    csv_file_path_4 = "./total_data_4.csv"


    if choice == "Chamber 1":
        page_one()
        download_csv(csv_file_path_1)
    elif choice == "Chamber 2":
        page_two()
        download_csv(csv_file_path_2)
    elif choice == "Chamber 3":
        page_three()
        download_csv(csv_file_path_3)
    elif choice == "Chamber 4":
        page_four()
        download_csv(csv_file_path_4)

if __name__ == '__main__':
    main()





