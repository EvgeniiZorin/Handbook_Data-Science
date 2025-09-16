"""
Select a dataset
and create a visualisation
""";

import streamlit as st
from streamlit_option_menu import option_menu
import plotly_express as px
import pandas as pd


st.set_page_config(
    page_title='Multipage App',
    page_icon='👋'
)
# st.sidebar.success('select a page above.')

if "my_input" not in st.session_state:
    st.session_state['my_input'] = ""
my_input = st.text_input('You can input your name here: ', st.session_state['my_input'])
submit = st.button("Submit")
if submit:
    st.session_state['my_input'] = my_input
    st.write('You have entered: ', my_input)

st.write("Welcome to my app! ", my_input)