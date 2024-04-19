import pandas as pd
import matplotlib.pyplot as plt 

import numpy as np
import wbgapi as wb   # I use wb as a namespace in all my work

import seaborn as sns
import matplotlib.pyplot as plt

import pyreadstat
import country_converter as coco 

#importing the os module
import os

#change current working directory to 'data'
os.chdir('compendium/podatki')
#dir1 = os.getcwd()

# https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md 
#https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md#codebook-for-the-oxford-covid-19-government-response-tracker#
# Codebook for the Oxford Covid-19 Government Response Tracker
#url = "https://github.com/OxCGRT/covid-policy-tracker/blob/18eb781dcb3427e63c5b756852a3b66be38e6efc/data/OxCGRT_nat_latest.csv"
#url = "https://github.com/OxCGRT/covid-policy-tracker/blob/master/data/OxCGRT_nat_latest.csv"
url = "Uz_tight_out.csv"
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

df = df1.replace(',','.', regex=True)

print(df)

df[['CTL_DS', 'CTL_DG' ,'CTL_C']] = df[['CTL_DS', 'CTL_DG' ,'CTL_C']].astype(str).astype(float)

print(type(df),"\n")
print('df tzpres', df.dtypes,"\n") 

df2 = df[[            'Country'    , 'CTL_C' ]].copy()

print(df2)
out_format = "ISO3"

df2['Three_Letter_Country_Code'] = coco.convert(names=df1['Country'], to=out_format, not_found=None)

print(df2)

df = df2.sort_values('CTL_C', ascending=False)
df.plot(x="Country", y=["CTL_C"], kind="bar")

plt.show() 

column_names_to_labels = { 'CTL_C' : 'Cultural Tightness and Looseness - Combination Index (Uz, CTL_C) (0= Most Tight)'   }

path = 'country_level_data/Uz.sav'
pyreadstat.write_sav(df2, path, column_labels=column_names_to_labels)
