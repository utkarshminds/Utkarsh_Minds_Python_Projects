
import matplotlib.pyplot as plt
import streamlit as st

def display_barchart(dataframe_column):
    dataframe_column.value_counts().plot(kind='bar')
    st.pyplot()