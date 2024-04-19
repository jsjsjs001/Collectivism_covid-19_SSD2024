# Load the data


import pandas as pd

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# import wbgapi as wb   # I use wb as a namespace in all my work

import pyreadstat

import plotly.express as px 
# import geopandas as gpd
import matplotlib.pyplot as plt
#importing the os module
import os

#change current working directory to 'data'
os.chdir('compendium/podatki')
#dir1 = os.getcwd()

path = 'Merge_all_num_SI_imena.sav'
df2, meta = pyreadstat.read_sav(path)


print('prebrana eb datoteka , "\n')
print(df2)

print(df2.columns )

# Default sort
df1 = df2.sort_values('Namera_cepljenja', ascending=False)

#set the scale to percent
df1['Namera_cepljenja']=  (df1['Namera_cepljenja']) * 100

df1['Omejevanje_svobode']=  (df1['Omejevanje_svobode']) * 100

# select if not NaN

df1 = df1[~df1['Namera_cepljenja'].isna()]

#df1 = df2.sort_values('LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED', ascending=False)
#df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] = df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] * 100
#df1.plot(x="Three_Letter_Country_Code", y=["Namera_cepljenja" , "Omejevanje_svobode"], kind="bar")
#df1.plot(x="Three_Letter_Country_Code", y=["Namera_cepljenja"], kind="bar")
#df1.plot(x="Three_Letter_Country_Code", y=["Omejevanje_svobode"], kind="scatter")
#df1['Individualizem'].plot(kind='bar', color='black',  alpha=0.3)
#df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] = df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] * 100
#df1.plot(x="Three_Letter_Country_Code", y=["Mobility_Total"], kind="bar")
fig, ax = plt.subplots()
ax.bar(df1['Three_Letter_Country_Code'], df1['Namera_cepljenja'], label="Namera cepljenja", alpha=0.3)
ax.scatter(df1['Three_Letter_Country_Code'], df1['Omejevanje_svobode'], color='black', marker='_', label="Omejevanje svoboščin (upravičeno)", s=250, alpha=0.8)
ax.plot(df1['Three_Letter_Country_Code'], df1['Individualizem'],  color='orange' , label="Individualizem", alpha=0.9)
ax.legend()
plt.ylabel("Vrednost na indeksu / procent podpore")
ax.set_axisbelow(True)
ax.grid(axis='y')
ax.tick_params(axis='x', size=11 )
plt.show() 

# Save plot to file (high resolution, PDF)
plt.savefig("bar-plot-hi-res1.jpg", dpi=400)

#print(df1['Tightness_adjusted_scale'])
#plt.show() 

#https://towardsdatascience.com/two-dimensional-histograms-and-three-variable-scatterplots-making-map-like-visualisations-in-7f413955747

