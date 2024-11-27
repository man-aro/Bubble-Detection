# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:13:17 2024

@author: ManishArora
"""

import streamlit as st
import pandas as pd



st.title('Deep Calibration Framework for Detecting Stock Bubbles using Option Prices')




stock = st.selectbox("Select a Stock: ", ('MSFT', 'AMZN', 'NVDA', 'AMD', 'META'))
st.write("Selected Stock: ", stock)


window_size = st.number_input('Window Size', min_value = 30, max_value = 60, step = 30)
st.write('Current Window Size is ', window_size)

