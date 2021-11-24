import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path
import os

st.title("""
Recreating Ben's Slides
""")

# directory = 'C:\\Users\\valer\\2019_apr_15_to_19.csv'
directory = st.file_uploader("Drag and drop a file", type=['csv', 'xlsx'])

data = (pd.read_csv(directory, na_values=[-9999])).dropna()
raw_df = data[0:5]

var_names = list(raw_df.columns)
st.sidebar.title("Make a Selection")
x_axis = st.sidebar.selectbox("Select X-Variable", var_names, index=5)
y_axis1 = st.sidebar.selectbox("Select Y-Variable 1 (Blue)", var_names, index=6)
y_axis2 = st.sidebar.selectbox("Select Y-Variable 2 (Red)", var_names, index=7)

################################################################################

yyyy_min = data['yyyy'].min()
yyyy_max = data['yyyy'].max()
y = list(range(yyyy_min, yyyy_max + 1))

mm_min = data['mm'].min()
mm_max = data['mm'].max()
m = list(range(mm_min, mm_max + 1))

dd_min = data['dd'].min()
dd_max = data['dd'].max()
d = list(range(dd_min, dd_max + 1))

hh_min = data['hh'].min()
hh_max = data['hh'].max()
h = list(range(hh_min, hh_max + 1))

year = st.sidebar.selectbox("Select Year", y)
month = st.sidebar.selectbox("Select Month", m)
day = st.sidebar.selectbox("Select Day", d)
hour = st.sidebar.selectbox("Select Hour", h)
#st.write(data.head())

################################################################################

# raw_df2 = (pd.read_csv(directory,
#                        usecols=["yyyy", "mm", "dd", "hh", x_axis, y_axis1, y_axis2],
#                        na_values=[-9999])).dropna()
raw_df2 = data[['yyyy', 'mm', 'dd', 'hh', x_axis, y_axis1, y_axis2]]


subset = data[
    (raw_df2['yyyy'] == year) &
    (raw_df2['mm'] == month) &
    (raw_df2['dd'] == day) &
    (raw_df2['hh'] == hour)
    ]
#st.write(subset.head())

if y_axis1 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis1 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))

if y_axis2 == 'last_az_cmd':
    subset['last_az_cmd'] = (1000 + (3564 * subset['last_az_cmd'] / 360))
elif y_axis2 == 'last_el_cmd':
    subset['last_el_cmd'] = (1000 + (3564 * subset['last_el_cmd'] / 360))

title_var = (str(month) + "-" + str(day) + "-" + str(year) + ", " + str(hour) + "h")
fig = px.line(subset, x=x_axis, y=[y_axis1, y_axis2],
              title=title_var)
st.plotly_chart(fig)
