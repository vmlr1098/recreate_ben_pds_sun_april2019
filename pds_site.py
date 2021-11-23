import streamlit as st
import pandas as pd
import plotly.express as px
from ipywidgets import interact

st.title("""
# PDS Attempt N
Level 1B Data Exploration
""")

directory = st.text_input("Enter the directory of your file:", "")
var_names = list((pd.read_csv(directory)).columns)
st.sidebar.title("Make a Selection")
x_axis = st.sidebar.selectbox("Select X-Variable", var_names)
y_axis = st.sidebar.selectbox("Select Y-Variable", var_names)

df = pd.read_csv(directory,
                 usecols=[x_axis, y_axis])
fig = px.scatter(df,
                 x=x_axis, y=y_axis,
                 title=f'Scatterplot of {x_axis} v. {y_axis}'
                 )
st.plotly_chart(fig)


