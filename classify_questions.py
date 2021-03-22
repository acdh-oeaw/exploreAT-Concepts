# streamlit run classify_questions.py

import streamlit as st
import numpy as np
import pandas as pd
pd.set_option('display.max_colwidth', 120)

st.title('Semi-automatic Question Classification Tool')


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Loading data
questions = pd.read_pickle('./questions_class.pickle')

# Notify the reader that the data was successfully loaded.
#data_load_state.text('Loading data...done!')


if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    #st.write(questions)
    st.table(questions)
