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

# Default sort
#df1 = df2.sort_values('LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED', ascending=False)
#df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] = df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] * 100
#df1.plot(x="Country", y=["LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED", "Individualism"], kind="bar")


df1 = df2.sort_values('StringencyIndex_Average_FD_do_6_22', ascending=False)
#df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] = df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] * 100
df1.plot(x="Country", y=["StringencyIndex_Average_FD_do_6_22", "StringencyIndex_Average_FD_po_6_22"], kind="bar")

plt.show() 


#plt.show() 

#https://towardsdatascience.com/two-dimensional-histograms-and-three-variable-scatterplots-making-map-like-visualisations-in-7f413955747