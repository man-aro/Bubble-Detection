# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:13:17 2024

@author: ManishArora
"""

import streamlit as st
import pandas as pd

st.write("Bubble Detection")


window_size = st.number_input('Window Size', min_value = 30, max_value = 180, step = 30)
st.write('Current Window Size is ', window_size)

