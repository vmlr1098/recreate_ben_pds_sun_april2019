import streamlit as st
import pandas as pd
import plotly.express as px

# READ IN DATA
#df = pd.read_csv('C:\\Users\\valer\\OneDrive\\Desktop\\PDS_sun\\luna7\\apr01_2019.csv')
df = pd.read_csv('C:\\Users\\valer\\2019_apr_15_to_19.csv')

# MAKE TITLES
st.title("""
# PDS Attempt 3
Level 1B Data Exploration
""")


# DISPLAY RAW DATA
#st.write(df3.head())
#st.write(df3) <- crashes the site
st.write(df.head(100))


# CREATE NEW VARIABLES FOR DROP DOWN
var_names = list(df.columns)


# CREATE SIDEBAR DROP-DOWN MENUS
st.sidebar.title("Make a Selection")
x_axis = st.sidebar.selectbox("Select X-Variable",
             (var_names))
y_axis = st.sidebar.selectbox("Select Y-Variable",
             (var_names))
st.sidebar.selectbox("Select Plot Type",
             ("Scatterplot", "Will", "Be", "The", "Plot Options"))


# PLOTTING
fig = px.scatter(df,
                 x=x_axis, y=y_axis,
                 title=f'Scatterplot of {x_axis} v. {y_axis}'
                 )
st.plotly_chart(fig)

# tell Mark the var of interest and he can



