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
x = df2['SUPPOSE_NATIONAL_GOVERNMENT']
y = df2['StringencyIndex_Average_FD_do_6_22']


#(((((((((((((())))))))))))))
#colour = np.arctan2(x, y)
#plt.scatter(x, y, s = 50, c = colour, alpha = 0.8)
#plt.colorbar()
df2['Tightness_adjusted_scale'] = pd.to_numeric(df2['Tightness_adjusted_scale'])

fig = px.scatter(df2, x="CTL_C", 
y="False_Viruses", text="Country",  size_max=100, 
trendline="ols", color="SUPPOSE_NATIONAL_GOVERNMENT")
fig.update_traces(textposition='top center')
fig.update_layout(title_text='Conspiracy by Cultural Tightness and Looseness - Combination Index (Uz, CTL_C) (0= Most Tight)', title_x=0.5)
fig.show()

#{'Continent_Code': None, 'Three_Letter_Country_Code': 'Country abbreviation', 
# 'Country': 'Country name', 
# 'SI_POV_NAHC': 'Poverty headcount ratio at national poverty lines (% of population)', 
# 'SI_POV_GINI': 'The Gini index measures the extent to which the distribution of income or consumption among individuals or households within an economy deviates from a perfectly equal distribution.', 
# 'Tightness_adjusted_scale': 'Tightness adjusted scale - Gelfand', 
# 'Hofstede_Individualism': 'Hofstede_Individualism - limited N of countries',
#  'CTL_C': 'Cultural Tightness and Looseness - Combination Index (Uz, CTL_C) (0= Most Tight)', 
# 'Power_Distance_Index': 'Power Distance Index (PDI)', 'Individualism': 'Individualism Index (IDV)', 
# 'Masculinity': 'Masculinity Index (MAS)', 'Uncertainty_Avoidance': 'Uncertainty Avoidance Index (UAI)', 
# 'Long_Term': 'Long Term Orientation Index (LTO)', 'Indulgence': 'Indulgence versus Restraint Index (IVR)', 
# 'SUPPOSE_NATIONAL_GOVERNMENT': 'SUPPOSE/OPPOSE NATIONAL GOVERNMENT IN GENERAL', 
# 'SATISFACTION_PANDEMIC_MEASURES': 'SATISFACTION WITH 
#GOVERNMENT CORONAVIRUS PANDEMIC MEASURES', '
# LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED': 'LIMITATION OF INDIVID FREEDOM - JUSTIFIED VS OPPOSED', 
# 'Everyone_should_get_vaccinated_it_is_civic_duty': None, 
# 'All_Less_Vaccinated_Later_Never': None, 
# 'False_Viruses': 'Viruses have been produced in government laboratories to control our freedom', 
# 'False_Cancer': 'The cure for cancer exists but is hidden from the public by commercial interests', 
# 'False_Climate': 'Climate change is for the most part caused by natural cycles rather than human activities',
#  'False_Soc_Sci': 'The methods used by the natural sciences and the social sciences are equally scientific',
#  'StringencyIndex_Average_FD_do_6_22': 'Stringency Index Average FD_do_6_22', 
# 'StringencyIndex_Average_FD_po_6_22': 'Stringency Index Average FD po 6_22', 
# 'Mobility_Total': 'retail and recreation  grocery and pharmacy  parks  transit stations  workplaces  residential'}
#plt.show()

#plt.show() 

#https://towardsdatascience.com/two-dimensional-histograms-and-three-variable-scatterplots-making-map-like-visualisations-in-7f413955747