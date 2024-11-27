# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 14:13:17 2024

@author: ManishArora
"""

import streamlit as st
import pandas as pd

st.write("First Attempt: Create Table")


option = st.selectbox('Contact', ('Email', 'Phone'), ('marora6899@gmail.com', '+44 0 7476720446'))
st.write('You selected:', option)


