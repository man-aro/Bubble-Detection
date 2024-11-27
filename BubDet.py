# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:13:17 2024

@author: ManishArora
"""

import streamlit as st
import pandas as pd
import io

import requests

st.title('Deep Calibration Framework for Detecting Stock Bubbles using Option Prices')




stock = st.selectbox("Select a Stock: ", ('MSFT', 'AMZN', 'NVDA', 'AMD', 'META'))
st.write("Selected Stock: ", stock)




window_size = st.selectbox("Select a Window Size (days): ",('30', '60'))
st.write("Window size determines the number of historical observations (days) from which information is considered for bubble detection.")
st.write("Selected Window Size (days) is: ", window_size)

sig_level = st.selectbox("Select a Level of Significance (%): ", ('10%', '5%', '1%'))
st.write("Bubble detection is stricter for lower levels of significance.")
st.write("Selected Significance Level: ", sig_level)


calibration_type = st.selectbox("Select Calibration Form :", ('Most Liquid Smile', 'Entire Surface'))
st.write("Daily information regarding forward looking expectations of market participants can be gathered from the most liquid volatility smile (option maturity), or the entire surface.")
st.write("Selected Calibration Form: ", calibration_type)
         

x = window_size
st.write(x)



calibration = 'HCV'

if calibration_type == 'Most Liquid Smile':
   calibration = 'HCV'
else:
   calibration = 'ATO'
    
    

url="https://raw.githubusercontent.com/man-aro/BubbleDetection/main/Data/" + stock + "_NN/Bubble_Magnitudes_NN_" + calibration + "_671_i_" + window_size + ".csv"

st.write(url)

df = pd.read_csv(url)
