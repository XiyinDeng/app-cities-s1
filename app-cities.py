import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

st.title('World Cities')
df = pd.read_csv('worldcities.csv')

# add a slider (have to give float)
population_filter = st.slider('Minimal Population (Millions):', 0.0, 40.0, 3.6)  # min, max, default

# create a multi select
capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options
     df.capital.unique())  # defaults

# create a input form
form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")


# filter by population
df = df[df.population >= population_filter]

# filter by country
df = df[df.capital.isin(capital_filter)]

if country_filter!='ALL':
    df = df[df.country == country_filter]

# show on map
st.map(df)

# show df
st. write(df)