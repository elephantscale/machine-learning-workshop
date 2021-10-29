## TODO: work in progress

import streamlit as st
import pandas as pd

# get data
import os
import urllib.request

# download data
data_location = "flights.csv.gz"
data_url = 'https://elephantscale-public.s3.amazonaws.com/data/nycflights13/flights.csv.gz'

if not os.path.exists (data_location):
    data_location = os.path.basename(data_location)
    if not os.path.exists(data_location):
        urllib.request.urlretrieve(data_url, data_location)
        print ('Downloading : ', data_url)
print('data_location :', data_location)  


# load data
flights_all = pd.read_csv(data_location)
flights = flights_all.sample(10000)

dest = flights['dest'].unique()
# dest_select = st.select_box("Choose Destination", dest, default='ORD')

type(dest_select)
flights_by_dest = flights[(flights['dest'] == 'ORD')]

st.write("# Flights Data", flights_by_dest)

st.bar_
