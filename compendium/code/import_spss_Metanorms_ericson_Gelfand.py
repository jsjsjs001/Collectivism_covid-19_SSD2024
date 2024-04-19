import pandas as pd

import pyreadstat

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import country_converter as coco 
#importing the os module
import os

#change current working directory to 'data'
os.chdir('compendium/podatki')
#dir1 = os.getcwd()

df, meta = pyreadstat.read_sav('Metanorms_and_other_country_measures.sav')
print(type(df),"\n")
print(type(meta),"\n")
print(df.head(),"\n")
print(meta.column_names_to_labels,"\n")
print(meta.variable_value_labels,"\n")





#df, meta = pyreadstat.read_sav('../../covid_19_delo/Serban_a/country_level_data/COUNTRY LEVEL DATA.sav')

#np.exp(df['Hofstede_Individualism']).plot(kind='hist')
 
# plotting graph
#df.plot(x="CountryISO", y=["Hofstede_Individualism", "Height(in cm)"], kind="bar")
# Default sort
df2 = df.sort_values('Tightness_adjusted_scale', ascending=False)
df2.plot(x="SiteCountry", y=["Tightness_adjusted_scale"], kind="bar")

plt.show() 

############# test če so vse države veljavne iso3
iso2_codes = coco.convert(names= df2['CountryISO'], to='ISO2')
print(iso2_codes)

#df2['Three_Letter_Country_Code']= iso3_codes
#print(df2) 

df2 = df[['CountryISO','Tightness_adjusted_scale', 'Hofstede_Individualism'  ]].copy()

df2=df2.rename(columns={'CountryISO' :'Three_Letter_Country_Code'})

print(df2)
########### dodaj vmesno za SI
df2.loc[57] = ['SVN',   '1.7433',  '' ]

print(df2)

#####################
#np.exp(data[data['Year']==2018]['Log GDP per capita']).plot(kind='hist')

column_names_to_labels = {'Three_Letter_Country_Code': 'Country abbreviation', 'Tightness_adjusted_scale' : 'Tightness adjusted scale - Gelfand',
    'Hofstede_Individualism' : 'Hofstede_Individualism - limited N of countries' ,
      }

path = 'Metanorms_Tightness.sav'
pyreadstat.write_sav(df2, path, column_labels=column_names_to_labels)
