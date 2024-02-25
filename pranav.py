import streamlit as st
import pandas 
import numpy 
import matplotlib.pyplot as plt

from services.display_histogram import display_histogram
from services.display_barchart import display_barchart

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Database Explorer')

uploaded_file = st.file_uploader('Upload CSV file', type=['csv'])

if uploaded_file is not None:

    df = pandas.read_csv(uploaded_file)

    st.write(df)

    columns_names = df.columns.tolist()

    selected_col = st.selectbox('Select a column', columns_names)

    if pandas.api.types.is_numeric_dtype(df[selected_col]):

        display_histogram(df[selected_col])

    else:

        display_barchart(df[selected_col])