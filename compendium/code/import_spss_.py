import pandas as pd

import pyreadstat

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import country_converter as coco 

#dir = ('c:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\covid_19_delo\Serban_a\country_level_data\')

df, meta = pyreadstat.read_sav('../../covid_19_delo/Serban_a/country_level_data/Metanorms_and_other_country_measures.sav')
print(type(df),"\n")
print(type(meta),"\n")
print(df.head(),"\n")
print(meta.column_names_to_labels,"\n")
print(meta.variable_value_labels,"\n")

print(type(df))


print(type(meta))


#df, meta = pyreadstat.read_sav('../../covid_19_delo/Serban_a/country_level_data/COUNTRY LEVEL DATA.sav')

#np.exp(df['Hofstede_Individualism']).plot(kind='hist')
 
# plotting graph
#df.plot(x="CountryISO", y=["Hofstede_Individualism", "Height(in cm)"], kind="bar")
# Default sort
df2 = df.sort_values('Hofstede_Individualism', ascending=False)
#df2.plot(x="CountryISO", y=["Hofstede_Individualism"], kind="bar")

#plt.show() 



#####################
#np.exp(data[data['Year']==2018]['Log GDP per capita']).plot(kind='hist')
