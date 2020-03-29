import matplotlib.pyplot as plt
import pandas as pd
import os
import plotly.plotly as py
import plotly.figure_factory as ff
import plotly
import geopandas
import shapely

plotly.tools.set_credentials_file(username='ameyxd', api_key='BAEriF4kIYIK9OaznqUi')


c = pd.read_csv(os.getcwd() + "/data/" + "us-counties.csv")
s = pd.read_csv(os.getcwd() + "/data/" + "us-states.csv")
c.fillna(0, inplace=True)
s.fillna(0, inplace=True)

texas_c = c[c.state == 'Texas']

date = '2020-03-20'

us_day = c[c.date == date]
us_day = us_day[us_day.fips.notna()]
fips = us_day.fips.tolist()
values = us_day.cases.tolist()

colorscale = [
    'rgb(193, 193, 193)',
    'rgb(239,239,239)',
    'rgb(195, 196, 222)',
    'rgb(144,148,194)',
    'rgb(101,104,168)',
    'rgb(65, 53, 132)'
]

fig = ff.create_choropleth(fips=fips, values=values, binning_endpoints=[1, 10, 30, 60, 100],
                           colorscale=colorscale, county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
                           round_legend_values=True, legend_title='COVID-19 cases on March 3rd 2020',
                           title='United States Counties')

py.plot(fig, filename='united_states_outlines')
