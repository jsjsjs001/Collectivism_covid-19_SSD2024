import pandas as pd
import matplotlib.pyplot as plt 

import numpy as np
import wbgapi as wb   # I use wb as a namespace in all my work

import seaborn as sns
import matplotlib.pyplot as plt

import pyreadstat
import country_converter as coco 

# https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md 
#https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md#codebook-for-the-oxford-covid-19-government-response-tracker#
# Codebook for the Oxford Covid-19 Government Response Tracker
#url = "https://github.com/OxCGRT/covid-policy-tracker/blob/18eb781dcb3427e63c5b756852a3b66be38e6efc/data/OxCGRT_nat_latest.csv"
#url = "https://github.com/OxCGRT/covid-policy-tracker/blob/master/data/OxCGRT_nat_latest.csv"
url = "../../covid_19_delo/Serban_a/country_level_data/6-dimensions-for-website-2015-12-08-0-100.csv"
df1 = pd.read_csv(url, sep = ';')

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df1)

# calling head() method  
# storing in new variable 
data_top = df1.head() 
    
# display 
print(data_top ) 

my_list = list(df1)

print (my_list)
print (type(my_list))

print(type(df1),"\n")


df= df1.replace('#NULL!', '0')

print('df tzpres', df.dtypes,"\n") 
df[['pdi'    , 'idv'   ,  'mas'   ,  'uai'  ,'ltowvs'   ,  'ivr']] = df[['pdi'    , 'idv'   ,  'mas'   ,  'uai'  ,'ltowvs'   ,  'ivr']].astype(str).astype(int)
df1= df.replace( 0, np.nan)

#df.replace(np.nan, 0)

out_format = "ISO3"

df2 = df1[['ctr'  ,              'country'    , 'pdi'    , 'idv'   ,  'mas'   ,  'uai'  ,'ltowvs'   ,  'ivr']].copy()

print(df2)

df2['Three_Letter_Country_Code'] = coco.convert(names=df1['country'], to=out_format, not_found=None)


df2=df2.rename(columns={'pdi' : 'Power_Distance_Index'   , 'idv' : 'Individualism'   ,  'mas' : 'Masculinity' ,  'uai' : 'Uncertainty_Avoidance','ltowvs'  : 'Long_Term',  'ivr' : 'Indulgence'})

print('Rezultat je..... čččččččččččččččččččČČČČ::::::::::::::::')
print(df2)


df = df2.sort_values('Individualism', ascending=False)
df.plot(x="country", y=["Individualism"], kind="bar")

#plt.show() 

column_names_to_labels = { 'Power_Distance_Index' : 'Power Distance Index (PDI)',  'Individualism' : 'Individualism Index (IDV)',  
    'Masculinity' : 'Masculinity Index (MAS)',  'Uncertainty_Avoidance' : 'Uncertainty Avoidance Index (UAI)',  
    'Long_Term' : 'Long Term Orientation Index (LTO)',  'Indulgence' : 'Indulgence versus Restraint Index (IVR)'   }

path = '../../covid_19_delo/Serban_a/country_level_data/Hofstede.sav'
pyreadstat.write_sav(df2, path, column_labels=column_names_to_labels)