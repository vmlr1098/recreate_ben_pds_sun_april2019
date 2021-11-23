import pandas as pd
import plotly.express as px
import streamlit as st
from pathlib import Path
import os

st.title("""
Recreating Ben's Slides
""")

#directory = 'C:\\Users\\valer\\2019_apr_15_to_19.csv'
#directory = st.text_input("Enter the directory of your file:", "")
#directory = Path(dir).parents[1] / dir
directory = st.text_input('Enter a file path:')
try:
    with open(filename) as input:
        st.text(input.read())
except FileNotFoundError:
    st.error('File not found.')

raw_df = pd.read_csv(directory, nrows=3)

var_names = list(raw_df.columns)
st.sidebar.title("Make a Selection")
x_axis = st.sidebar.selectbox("Select X-Variable", var_names)
y_axis1 = st.sidebar.selectbox("Select Y-Variable 1 (Blue)", var_names)
y_axis2 = st.sidebar.selectbox("Select Y-Variable 2 (Red)", var_names)


yyyy_min = (pd.read_csv(directory, usecols=["yyyy"])).min()
yyyy_max = (pd.read_csv(directory, usecols=["yyyy"])).max()
y = list(range(yyyy_min['yyyy'], yyyy_max['yyyy'] + 1))

mm_min = (pd.read_csv(directory, usecols=["mm"])).min()
mm_max = (pd.read_csv(directory, usecols=["mm"])).max()
m = list(range(mm_min['mm'], mm_max['mm'] + 1))

dd_min = (pd.read_csv(directory, usecols=["dd"])).min()
dd_max = (pd.read_csv(directory, usecols=["dd"])).max()
d = list(range(dd_min['dd'], dd_max['dd'] + 1))

hh_min = (pd.read_csv(directory, usecols=["hh"])).min()
hh_max = (pd.read_csv(directory, usecols=["hh"])).max()
h = list(range(hh_min['hh'], hh_max['hh'] + 1))

year = st.sidebar.selectbox("Select Year", y)
month = st.sidebar.selectbox("Select Month", m)
day = st.sidebar.selectbox("Select Day", d)
hour = st.sidebar.selectbox("Select Hour", h)

raw_df2 = (pd.read_csv(directory,
                       usecols=["yyyy", "mm", "dd", "hh", x_axis, y_axis1, y_axis2],
                       na_values=[-9999])).dropna()

subset = raw_df2[
    (raw_df2['yyyy'] == year) &
    (raw_df2['mm'] == month) &
    (raw_df2['dd'] == day) &
    (raw_df2['hh'] == hour)
    ]

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
