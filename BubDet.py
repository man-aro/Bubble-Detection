# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:13:17 2024

@author: ManishArora
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FormatStrFormatter
from datetime import datetime

st.title('Deep Calibration Framework for Detecting Stock Bubbles using Option Prices')




stock = st.selectbox("Select a Stock*: ", (' ', 'MSFT', 'AMZN', 'NVDA', 'AMD', 'META'))
st.write("Selected Stock: ", stock)




window_size = st.selectbox("Select a Window Size (days)*: ",(' ', '30', '60'))
st.write("Window size determines the number of historical observations (days) from which information is considered for bubble detection.")
st.write("Selected Window Size (days) is: ", window_size)

sig_level = st.selectbox("Select a Level of Significance (%)*: ", (' ', '10%', '5%', '1%'))
st.write("Bubble detection is stricter for lower levels of significance.")
st.write("Selected Significance Level: ", sig_level)


calibration_type = st.selectbox("Select Calibration Form :", (' ', 'Most Liquid Smile', 'Entire Surface'))
st.write("Daily information regarding forward looking expectations of market participants can be gathered from the most liquid volatility smile (option maturity), or the entire surface.")
st.write("Selected Calibration Form: ", calibration_type)

if calibration_type == 'Most Liquid Smile':
   calibration = 'HCV'
elif calibration_type == 'Entire Surface':
   calibration = 'ATO'
   
if sig_level == '10%':
    sig= 'BUB_10'
    Threshold = 'Threshold_10'
elif sig_level == '5%':
    sig = 'BUB_5'
    Threshold = 'Threshold_5'
elif sig_level == '1%': 
    sig = 'BUB_1'
    Threshold = 'Threshold_1'
    
#stock = 'AMD'
#window_size = str(30)
#calibration = 'HCV'
#sig = 'BUB_10'
#Threshold = 'Threshold_10'


Date_Period = st.slider("Select Period:", value=(datetime(2022, 10, 25), datetime(2024, 4, 30)))


if stock == ' ' or window_size == ' ' or calibration_type == ' ' or sig_level == ' ':
    st.write('Please select required fields *')
else: 
    url="https://raw.githubusercontent.com/man-aro/BubbleDetection/main/Data/" + stock + "_NN/Bubble_Magnitudes_NN_" + calibration + "_671_i_" + window_size + ".csv"
    Bubble = pd.read_csv(url)
    
    Bubble['Date'] = pd.to_datetime(Bubble['Date'])
    Bubble.sort_values('Date', inplace = True)
    Bubble.reset_index(inplace = True)
    
    
    Bubble['Str_Date'] = Bubble['Date'].apply(lambda x: x.strftime('%Y-%m-%d'))
    start = Bubble['Str_Date'].iloc[0]
    end = Bubble['Str_Date'].iloc[-1]
    
    color_bubble = 'indigo'
    color_significance = 'firebrick'
    color_SP = 'black'
    
    Title_size = 30
    title_0_size = 20
    title_1_size = 20
    y_ticks_size = 20
    x_ticks_size = 20
    y_label_size = 15
    x_label_size = 20
    ax0_legend_size = 20
    legend_size = 18
    tick_pad = 12
    Sub_Title_Size = 20
    
    fig = plt.figure(figsize = (20, 12), constrained_layout=True)
    
    gs=fig.add_gridspec(2,1)
    
    ax0 = fig.add_subplot(gs[0]) 
    ax0.set_title(stock + ' Bubbles' , fontsize = Title_size)
    ax0.bar(Bubble['Date'], Bubble[sig]*1.4, linewidth = 3, alpha = 1, color = color_bubble, width = 2, label  = 'Bubble')
    ax0.plot(Bubble['Date'], Bubble['S_P'], color_SP, linewidth = 3, label = 'Price ($)', zorder = 2)
    ax0.set_xticks(pd.date_range(start = start, end = end, freq = 'D'))
    ax0.xaxis.set_major_locator(mdates.MonthLocator(bymonth = range(1,13), bymonthday =1, interval =4))
    
    ax0.legend(bbox_to_anchor=(0.75, 1.0), prop = {'size': ax0_legend_size}, frameon = True, ncol = 2,framealpha = 1.0)
    ax0.yaxis.set_tick_params(labelsize=y_ticks_size)
    ax0.xaxis.set_tick_params(labelsize=x_ticks_size)

    st.pyplot(fig)
