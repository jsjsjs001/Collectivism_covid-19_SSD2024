# Load the data


import pandas as pd

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


import wbgapi as wb   # I use wb as a namespace in all my work

import pyreadstat

import plotly.express as px 
import geopandas as gpd
import matplotlib.pyplot as plt



#%matplotlib inline

path = '../../covid_19_delo/Serban_a/country_level_data/Merge_all_num_SI_imena.sav'
df1, meta = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta.column_names_to_labels,"\n")
print(meta.variable_value_labels,"\n")

print('prebrana eb datoteka , "\n')
print(df1)

#ne vem zakaj še enkrat

#print(df1[df1['Continent_Code'] == 'EU'])

#df2= df1[df1['Continent_Code'] == 'EU']

# absolute frequencies
m_c = pd.crosstab(index=df1["Three_Letter_Country_Code"], columns='count',  margins=True)  

# intermediate result
print(m_c)
print(m_c.index)


# Load the shapefile
shapefile_path = "../../covid_19_delo/Serban_a/Europe/Europe_merged.shp"
gdf = gpd.read_file(shapefile_path)

# Plot the shapefile
gdf.plot()

# Display the plot
plt.show()



print(gdf.head())
print(gdf)
gdf.columns=['Three_Letter_Country_Code', 'COUNTRY', 'geometry']


# absolute frequencies
m_c = pd.crosstab(index=gdf["Three_Letter_Country_Code"], columns='count',  margins=True)  

# intermediate result
print(m_c)
print(m_c.index)

merge=pd.merge(gdf,df1,on='Three_Letter_Country_Code')

print(merge) 

# plot confirmed cases world map 
merge.plot(column='Zadovoljstvo_z_ukrepi', scheme="quantiles", figsize=(25, 20), legend=True,cmap='coolwarm')
#plt.title('2020 Jan-May Confirmed Case Amount in Different Countries',fontsize=25)
# add countries names and numbers 
for i in range(0,10):
    plt.text(float(merge.longitude[i]),float(merge.latitude[i]),"{}\n{}".format(merge.name[i],merge.Confirmed_Cases[i]),size=10)
#plt.show()
# Plot the shapefile
#gdf.plot()
#merge.plot(column='Namera_cepljenja', scheme="quantiles",figsize=(25, 20),legend=True,cmap='coolwarm')
#plt.show()
# Display the plot
#plt.show()




#fig = plt.figure()
#x = df2['Individualizem']
#y = df2['Omejevanje_svobode']


#(((((((((((((())))))))))))))
#colour = np.arctan2(x, y)
#plt.scatter(x, y, s = 50, c = colour, alpha = 0.8)
#plt.colorbar()
#df2['Tightness_adjusted_scale'] = pd.to_numeric(df2['Tightness_adjusted_scale'])




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
