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



st.write('The window size determines the extent to which information from historical observations are considered whilst examining the significance of the bubble.')
st.write('The selection of a window length can be interpretated as being analogous to the risk-appetite of investors. For instance, a more conservative (larger window) detection approach would signal lower regulatory pressure on capital requirements, and a riskier outlook from investors, who would reveal looser preferences towards protecting positions from the potential  presence of bubbles.')





window_size = st.selectbox("Select a Window Size (days): ",('30', '60'))
st.write("Selected Window Size (days) is: ", window_size)

sig_level = st.selectbox("Select a Level of Significance (%): ", ('10%', '5%', '1%'))
st.write("Selected Significance Level: ", sig_level)