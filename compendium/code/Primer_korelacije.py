# Load the data


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


import wbgapi as wb   # I use wb as a namespace in all my work

import pyreadstat

import plotly.express as px 

#importing the os module
import os

#change current working directory to 'data'
os.chdir('compendium/podatki')
#dir1 = os.getcwd()

path = 'Merge_all.sav'
df1, meta = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta.column_names_to_labels,"\n")
print(meta.variable_value_labels,"\n")

for col in df1.columns:
    print(' "',col,'" ,')
#(meta.column_names_to_labels,"\n")

print('prebrana eb datoteka , "\n')
print(df1)

print(df1[df1['Continent_Code'] == 'EU'])

df2= df1[df1['Continent_Code'] == 'EU']

# Default sort
df1 = df2.sort_values('False_Viruses', ascending=False)

#print(type(df1['Tightness_adjusted_scale']))

df1['Tightness_adjusted_scale'] = pd.to_numeric(df1['Tightness_adjusted_scale'])
#print(type(df1['Tightness_adjusted_scale']))

#df1['Tightness_adjusted_scale']=  (df1['Tightness_adjusted_scale']/5) * 100
#df1 = df2.sort_values('LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED', ascending=False)
#df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] = df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] * 100
#df1.plot(x="Three_Letter_Country_Code", y=["False_Viruses" , 'False_Climate' , 'False_Cancer' , 'False_Soc_Sci' ], kind="bar")

data= df1[['SI_POV_GINI', 'Tightness_adjusted_scale', 'CTL_C',    'Individualism',    
'SUPPOSE_NATIONAL_GOVERNMENT',  'LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED',  
'Everyone_should_get_vaccinated_it_is_civic_duty' , 'SATISFACTION_PANDEMIC_MEASURES',
'False_Viruses',
'All_Less_Vaccinated_Later_Never',
'StringencyIndex_Average_FD_do_6_22',
'StringencyIndex_Average_FD_po_6_22',
'Mobility_Total']]

#pd.set_option('max_columns', None)
print(data.corr())
corr_data= data.corr()

# determining the name of the file
path = 'korelacije.xlsx'
  
# saving the excel
corr_data.to_excel(path)
#df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] = df1['LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED'] * 100
#df1.plot(x="Three_Letter_Country_Code", y=["Mobility_Total"], kind="bar")

#plt.show() 

#plt.show() 

#https://towardsdatascience.com/two-dimensional-histograms-and-three-variable-scatterplots-making-map-like-visualisations-in-7f413955747