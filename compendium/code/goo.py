import pandas as pd
import matplotlib.pyplot as plt 

import numpy as np
import wbgapi as wb   # I use wb as a namespace in all my work

import seaborn as sns
import matplotlib.pyplot as plt
import country_converter as coco 

import pyreadstat

# https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md 
#https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md#codebook-for-the-oxford-covid-19-government-response-tracker#
# Codebook for the Oxford Covid-19 Government Response Tracker
#url = "https://github.com/OxCGRT/covid-policy-tracker/blob/18eb781dcb3427e63c5b756852a3b66be38e6efc/data/OxCGRT_nat_latest.csv"
#url = "https://github.com/OxCGRT/covid-policy-tracker/blob/master/data/OxCGRT_nat_latest.csv"
url = "../../covid_19_delo/Serban_a/country_level_data/mobility_report_countries_2021.xlsx"
df1 = pd.read_excel(url)

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df1)

print(df1)
# calling head() method  
# storing in new variable 
data_top = df1.head() 
    
# display 
print(data_top ) 

my_list = list(df1)

print (my_list)
print (type(my_list))

pov_str= df1.loc[(df1['region'] == 'Total' )].groupby('country')['retail and recreation' , 'grocery and pharmacy' , 'parks' , 'transit stations' , 'workplaces' , 'residential'].mean()

print(pov_str)

df2= pd.DataFrame(pov_str)

df2['Country'] = df2.index

out_format = "ISO3"


print(df2)

df2['Three_Letter_Country_Code'] = coco.convert(names=df2['Country'], to=out_format, not_found=None)

print(df2)

df2 = df2.assign(Mobility_Total =(df2['retail and recreation'] + df2['grocery and pharmacy'] + df2['parks'] + df2['transit stations'] + df2['workplaces'] + df2['residential']) / 5 )

df2=df2.rename(columns={"retail and recreation" : 'retail_recreation'  , 'grocery and pharmacy' : 'grocery_pharmacy',  'transit stations' : 'transit_stations' , 'CountryISO' :'Three_Letter_Country_Code'})

column_names_to_labels = {'Continent_Code' : None,'Three_Letter_Country_Code': 'Country abbreviation', 'Country': 'Country name', 
 "Mobility_Total" : "retail and recreation  grocery and pharmacy  parks  transit stations  workplaces  residential"}


print(df2)

path = '../../covid_19_delo/Serban_a/country_level_data/Goo_nat.sav'
pyreadstat.write_sav(df2, path, column_labels=column_names_to_labels)

#df1[df1['CountryCode'] == 'FRA'].set_index('Date')['PopulationVaccinated'].plot(kind='line', figsize=(12,8))

#df1[df1['CountryCode'] == 'SVN'].set_index('Date')['PopulationVaccinated'].plot(kind='line',figsize=(12,8))

#df1[df1['CountryCode'] == 'FRA'].set_index('Date')['StringencyIndex_Average_ForDisplay'].plot(
#    kind='line',
#    figsize=(12,8)

#plt.show() 


