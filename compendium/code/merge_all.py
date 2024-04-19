import pandas as pd
import matplotlib.pyplot as plt 

import numpy as np
#import wbgapi as wb   # I use wb as a namespace in all my work

import seaborn as sns
import matplotlib.pyplot as plt

import pyreadstat
#importing the os module
import os
#to get the current working directory

directory = os.getcwd()
print('tole: ', directory, ' konec')
# set current working directory
os.chdir('c:/Users/stebej/OneDrive - Univerza v Ljubljani/Collectivism_covid-19_SSD2024/compendium/code/')
dir1 = os.getcwd()
print('tole 1: ', dir1, ' konec')

# read data file with missing values included, and with numeric values

path = '../podatki/Country_measures.sav'
df, meta = pyreadstat.read_sav(path)
print(type(df),"\n")
print(type(meta),"\n")
print(df.head(),"\n")
print(meta.column_names_to_labels,"\n")
print(meta.variable_value_labels,"\n")
print(df)

path = '../podatki/Country_measures_gini.sav'
df1, meta1 = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta1.column_names_to_labels,"\n")
print(meta1.variable_value_labels,"\n")
print(df1)



merged_left = pd.merge(left=df, right=df1, how='left', left_on='Three_Letter_Country_Code', right_on='Three_Letter_Country_Code')

print(merged_left)
merged_left.rename(columns={"Continent_Code_x" : 'Continent_Code' , 'Country_x' : 'Country' }, inplace=True)
print(merged_left)


df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI' ]].copy()

print(df)

#meta["SI_POV_GINI"] = meta1['SI_POV_GINI']
print(meta.column_names_to_labels)
print(meta1.column_names_to_labels)
column_names_to_labels =  meta.column_names_to_labels 
print(column_names_to_labels)


column_names_to_labels["SI_POV_GINI"] = meta1.column_names_to_labels['SI_POV_GINI']

print(column_names_to_labels) 

#*********************next file to merge 1 ********************************************************

path = '../../covid_19_delo/Serban_a/country_level_data/Metanorms_Tightness.sav'
df1, meta1 = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta1.column_names_to_labels,"\n")
print(meta1.variable_value_labels,"\n")
print(df1)



df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI' ]].copy()

merged_left = pd.merge(left=df, right=df1, how='left', left_on='Three_Letter_Country_Code', right_on='Three_Letter_Country_Code')

print(merged_left)
#merged_left.rename(columns={"Continent_Code_x" : 'Continent_Code' , 'Country_x' : 'Country' }, inplace=True)
print(merged_left)

df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI', 
    'Tightness_adjusted_scale' , 'Hofstede_Individualism' ]].copy()

column_names_to_labels["Tightness_adjusted_scale" ] = meta1.column_names_to_labels["Tightness_adjusted_scale" ]
column_names_to_labels["Hofstede_Individualism"] = meta1.column_names_to_labels["Hofstede_Individualism"]


print(column_names_to_labels)

print(df)

#*********************next file to merge 2 ********************************************************

path = '../../covid_19_delo/Serban_a/country_level_data/Uz.sav'
df1, meta1 = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta1.column_names_to_labels,"\n")
print(meta1.variable_value_labels,"\n")
print(df1)


#df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI' ]].copy()

merged_left = pd.merge(left=df, right=df1, how='left', left_on='Three_Letter_Country_Code', right_on='Three_Letter_Country_Code')

print(merged_left)
merged_left.rename(columns={'Country_x' : 'Country' }, inplace=True)
print(merged_left)

merged_left = merged_left.drop([19, 59 , 154, 220, 227])

df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI', 
    'Tightness_adjusted_scale' , 'Hofstede_Individualism', 'CTL_C' ]].copy()

column_names_to_labels["CTL_C" ] = meta1.column_names_to_labels["CTL_C" ]
#column_names_to_labels["Hofstede_Individualism"] = meta1.column_names_to_labels["Hofstede_Individualism"]


print(column_names_to_labels)
print ('tukaj')
print(df)
print(df[df['Continent_Code'] == 'EU'])

#*********************next file to merge 3 ********************************************************

path = '../../covid_19_delo/Serban_a/country_level_data/Hofstede.sav'
df1, meta1 = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta1.column_names_to_labels,"\n")
print(meta1.variable_value_labels,"\n")
print(df1)


#df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI' ]].copy()

merged_left = pd.merge(left=df, right=df1, how='left', left_on='Three_Letter_Country_Code', right_on='Three_Letter_Country_Code')

print(merged_left)


merged_left.rename(columns={'Country_x' : 'Country' }, inplace=True)
print(merged_left)

df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI', 
    'Tightness_adjusted_scale' , 'Hofstede_Individualism', 'CTL_C' ,
    'Power_Distance_Index' , 'Individualism',  'Masculinity' , 'Uncertainty_Avoidance' , 'Long_Term' , 'Indulgence' ]].copy()

column_names_to_labels["Power_Distance_Index" ] = meta1.column_names_to_labels["Power_Distance_Index" ]
column_names_to_labels["Individualism" ] = meta1.column_names_to_labels["Individualism" ]
column_names_to_labels["Masculinity" ] = meta1.column_names_to_labels["Masculinity" ]
column_names_to_labels["Uncertainty_Avoidance" ] = meta1.column_names_to_labels["Uncertainty_Avoidance" ]
column_names_to_labels["Long_Term" ] = meta1.column_names_to_labels["Long_Term" ]
column_names_to_labels["Indulgence" ] = meta1.column_names_to_labels["Indulgence" ]
#column_names_to_labels["Hofstede_Individualism"] = meta1.column_names_to_labels["Hofstede_Individualism"]


print(column_names_to_labels)

print(df)
print(df[df['Continent_Code'] == 'EU'])

# ?????????????????????????
df = df.drop([124, 31 , 32 , 178, 215 , 216])

print(df[df['Continent_Code'] == 'EU'])

#*********************next file to merge 4 ********************************************************

path = '../../covid_19_delo/Serban_a/country_level_data/Eu_Par_COVID-19_Survey.sav'
df1, meta1 = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta1.column_names_to_labels,"\n")
print(meta1.variable_value_labels,"\n")

print('prebrana eb datoteka , "\n')
print(df1)

df2 = df.sort_values('Three_Letter_Country_Code')
print(df2[df2['Continent_Code'] == 'EU'])

#https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/
#df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI' ]].copy()

merged_left = pd.merge(left=df2, right=df1, how='left', left_on='Three_Letter_Country_Code', right_on='Three_Letter_Country_Code')

print(merged_left)

print(merged_left[merged_left['Continent_Code'] == 'EU'])


df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI', 
    'Tightness_adjusted_scale' , 'Hofstede_Individualism', 'CTL_C' ,
    'Power_Distance_Index' , 'Individualism',  'Masculinity' , 'Uncertainty_Avoidance' , 'Long_Term' , 'Indulgence' ,
    'SUPPOSE_NATIONAL_GOVERNMENT'  ,'SATISFACTION_PANDEMIC_MEASURES' , 'LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED' , 'Everyone_should_get_vaccinated_it_is_civic_duty' , 'All_Less_Vaccinated_Later_Never' ]].copy()

column_names_to_labels["SUPPOSE_NATIONAL_GOVERNMENT" ] = meta1.column_names_to_labels["SUPPOSE_NATIONAL_GOVERNMENT" ]
column_names_to_labels["SATISFACTION_PANDEMIC_MEASURES" ] = meta1.column_names_to_labels["SATISFACTION_PANDEMIC_MEASURES" ]
column_names_to_labels["LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED" ] = meta1.column_names_to_labels["LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED" ]
column_names_to_labels["Everyone_should_get_vaccinated_it_is_civic_duty" ] = meta1.column_names_to_labels["Everyone_should_get_vaccinated_it_is_civic_duty" ]
column_names_to_labels["All_Less_Vaccinated_Later_Never" ] = meta1.column_names_to_labels["All_Less_Vaccinated_Later_Never" ]

#column_names_to_labels["Hofstede_Individualism"] = meta1.column_names_to_labels["Hofstede_Individualism"]


print(column_names_to_labels)

print(df)
print(df[df['Continent_Code'] == 'EU'])

#df = df.drop([124, 31 , 32 , 178, 215 , 216])

print(df[df['Continent_Code'] == 'EU'])

#*********************next file to merge 5 ********************************************************

path = '../../covid_19_delo/Serban_a/country_level_data/EB3_Survey.sav'
df1, meta1 = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta1.column_names_to_labels,"\n")
print(meta1.variable_value_labels,"\n")

print('prebrana eb datoteka , "\n')
print(df1)

df2 = df.sort_values('Three_Letter_Country_Code')
print(df2[df2['Continent_Code'] == 'EU'])

#https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/
#df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI' ]].copy()

merged_left = pd.merge(left=df2, right=df1, how='left', left_on='Three_Letter_Country_Code', right_on='Three_Letter_Country_Code')

print(merged_left)

print(merged_left[merged_left['Continent_Code'] == 'EU'])


df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI', 
    'Tightness_adjusted_scale' , 'Hofstede_Individualism', 'CTL_C' ,
    'Power_Distance_Index' , 'Individualism',  'Masculinity' , 'Uncertainty_Avoidance' , 'Long_Term' , 'Indulgence' ,
    'SUPPOSE_NATIONAL_GOVERNMENT'  ,'SATISFACTION_PANDEMIC_MEASURES' , 'LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED' , 'Everyone_should_get_vaccinated_it_is_civic_duty' , 'All_Less_Vaccinated_Later_Never' ,
    'False_Viruses' , 'False_Cancer' , 'False_Climate'  ,'False_Soc_Sci'
    ]].copy()

column_names_to_labels["False_Viruses" ] = meta1.column_names_to_labels["False_Viruses" ]
column_names_to_labels["False_Cancer" ] = meta1.column_names_to_labels["False_Cancer" ]
column_names_to_labels["False_Climate" ] = meta1.column_names_to_labels["False_Climate" ]
column_names_to_labels["False_Soc_Sci" ] = meta1.column_names_to_labels["False_Soc_Sci" ]

#column_names_to_labels["Hofstede_Individualism"] = meta1.column_names_to_labels["Hofstede_Individualism"]


print(column_names_to_labels)

print(df)
print(df[df['Continent_Code'] == 'EU'])

#df = df.drop([124, 31 , 32 , 178, 215 , 216])



#*********************next file to merge 6 ********************************************************

path = '../../covid_19_delo/Serban_a/country_level_data/OxCGRT_nat.sav'
df1, meta1 = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta1.column_names_to_labels,"\n")
print(meta1.variable_value_labels,"\n")

print('prebrana eb datoteka , "\n')
print(df1)

df2 = df.sort_values('Three_Letter_Country_Code')
print(df2[df2['Continent_Code'] == 'EU'])

merged_left = pd.merge(left=df2, right=df1, how='left', left_on='Three_Letter_Country_Code', right_on='Three_Letter_Country_Code')

print(merged_left)

print(merged_left[merged_left['Continent_Code'] == 'EU'])


df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI', 
    'Tightness_adjusted_scale' , 'Hofstede_Individualism', 'CTL_C' ,
    'Power_Distance_Index' , 'Individualism',  'Masculinity' , 'Uncertainty_Avoidance' , 'Long_Term' , 'Indulgence' ,
    'SUPPOSE_NATIONAL_GOVERNMENT'  ,'SATISFACTION_PANDEMIC_MEASURES' , 'LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED' , 'Everyone_should_get_vaccinated_it_is_civic_duty' , 'All_Less_Vaccinated_Later_Never' ,
    'False_Viruses' , 'False_Cancer' , 'False_Climate'  ,'False_Soc_Sci' ,
     'StringencyIndex_Average_FD_do_6_22' , 'StringencyIndex_Average_FD_po_6_22'
    ]].copy()

column_names_to_labels["StringencyIndex_Average_FD_do_6_22" ] = meta1.column_names_to_labels["StringencyIndex_Average_FD_do_6_22" ]
column_names_to_labels["StringencyIndex_Average_FD_po_6_22" ] = meta1.column_names_to_labels["StringencyIndex_Average_FD_po_6_22" ]


#column_names_to_labels["Hofstede_Individualism"] = meta1.column_names_to_labels["Hofstede_Individualism"]


print(column_names_to_labels)

print(df)
print(df[df['Continent_Code'] == 'EU'])

#df = df.drop([124, 31 , 32 , 178, 215 , 216])

#*********************next file to merge 6 ********************************************************

path = '../../covid_19_delo/Serban_a/country_level_data/Goo_nat.sav'
df1, meta1 = pyreadstat.read_sav(path)
print(type(df1),"\n")
print(type(meta),"\n")
print(df1.head(),"\n")
print(meta1.column_names_to_labels,"\n")
print(meta1.variable_value_labels,"\n")

print('prebrana eb datoteka , "\n')
print(df1)

df2 = df.sort_values('Three_Letter_Country_Code')
print(df2[df2['Continent_Code'] == 'EU'])

merged_left = pd.merge(left=df2, right=df1, how='left', left_on='Three_Letter_Country_Code', right_on='Three_Letter_Country_Code')

print(merged_left)

print(merged_left[merged_left['Continent_Code'] == 'EU'])

merged_left.rename(columns={'Country_x' : 'Country' }, inplace=True)
print(merged_left)


df= merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country' , 'SI_POV_NAHC' , 'SI_POV_GINI', 
    'Tightness_adjusted_scale' , 'Hofstede_Individualism', 'CTL_C' ,
    'Power_Distance_Index' , 'Individualism',  'Masculinity' , 'Uncertainty_Avoidance' , 'Long_Term' , 'Indulgence' ,
    'SUPPOSE_NATIONAL_GOVERNMENT'  ,'SATISFACTION_PANDEMIC_MEASURES' , 'LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED' , 'Everyone_should_get_vaccinated_it_is_civic_duty' , 'All_Less_Vaccinated_Later_Never' ,
    'False_Viruses' , 'False_Cancer' , 'False_Climate'  ,'False_Soc_Sci' ,
     'StringencyIndex_Average_FD_do_6_22' , 'StringencyIndex_Average_FD_po_6_22',
     'Mobility_Total'
    ]].copy()

column_names_to_labels["Mobility_Total" ] = meta1.column_names_to_labels["Mobility_Total" ]

#column_names_to_labels["Hofstede_Individualism"] = meta1.column_names_to_labels["Hofstede_Individualism"]


print(column_names_to_labels)

print(df)
print(df[df['Continent_Code'] == 'EU'])


path = '../../covid_19_delo/Serban_a/country_level_data/Merge_all.sav'
pyreadstat.write_sav(df, path, column_labels=column_names_to_labels)

