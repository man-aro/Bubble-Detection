# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:13:17 2024

@author: ManishArora
"""

import streamlit as st
import pandas as pd

st.write("First Attempt: Create Table")

st.write(pd.DataFrame({'1st Column': [1, 2, 3, 4],
                      '2nd Column': [10, 20, 30, 40]}))


option = st.selectbox('Contact', ('Email', 'Phone'))
st.write('You selected:', option)

st.markdown("Source: <https://bubbledetection_MRA.com")
