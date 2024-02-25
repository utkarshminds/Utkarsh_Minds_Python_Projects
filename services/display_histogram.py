
import matplotlib.pyplot as plt
import streamlit as st

def display_histogram(dataframe_column):
    plt.hist(dataframe_column, edgecolor='b', bins=10)
    st.pyplot()