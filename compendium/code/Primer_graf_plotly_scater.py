# Load the data


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


import wbgapi as wb   # I use wb as a namespace in all my work

import pyreadstat

import plotly.express as px 



#%matplotlib inline

path = '../../covid_19_delo/Serban_a/country_level_data/Merge_all.sav'
df1, meta = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta.column_names_to_labels,"\n")
print(meta.variable_value_labels,"\n")

print('prebrana eb datoteka , "\n')
print(df1)

print(df1[df1['Continent_Code'] == 'EU'])

df2= df1[df1['Continent_Code'] == 'EU']
fig = plt.figure()
x = df2['Individualism']
y = df2['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED']


#(((((((((((((())))))))))))))
#colour = np.arctan2(x, y)
#plt.scatter(x, y, s = 50, c = colour, alpha = 0.8)
#plt.colorbar()

fig = px.scatter(df2, x="Individualism", y="LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED", text="Three_Letter_Country_Code", log_x=True, size_max=100, color="All_Less_Vaccinated_Later_Never")
fig.update_traces(textposition='top center')
fig.update_layout(title_text='LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED', title_x=0.5)
fig.show()
#plt.show()

#plt.show() 

#https://towardsdatascience.com/two-dimensional-histograms-and-three-variable-scatterplots-making-map-like-visualisations-in-7f413955747