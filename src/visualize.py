import matplotlib.pyplot as plt
import pandas as pd
import os
import plotly.plotly as py
import plotly.figure_factory as ff
import geopandas
import shapely


c = pd.read_csv(os.getcwd() + "/data/" + "us-counties.csv")
s = pd.read_csv(os.getcwd() + "/data/" + "us-states.csv")

texas_c = c[c.state == 'Texas']

date = '2020-03-04'

us_day = c[c.date == date]
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

fig = ff.create_choropleth(fips=fips, values=values, binning_endpoints=[1, 10, 30, 60, 100, 150],
                           colorscale=colorscale, county_outline={'color': 'rgb(255,255,255)', 'width': 0.5},
                           round_legend_values=True, legend_title='COVID-19 cases ono March 3rd 2020',
                           title='United States Counties')

py.iplot(fig, filename='united_states_outlines')
