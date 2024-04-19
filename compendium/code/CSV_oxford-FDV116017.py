import pandas as pd
import matplotlib.pyplot as plt 

import numpy as np
import wbgapi as wb   # I use wb as a namespace in all my work

import seaborn as sns
import matplotlib.pyplot as plt

import pyreadstat

# https://github.com/OxCGRT/covid-policy-tracker/blob/master/documentation/codebook.md 
# Codebook for the Oxford Covid-19 Government Response Tracker
#url = "https://github.com/OxCGRT/covid-policy-tracker/blob/18eb781dcb3427e63c5b756852a3b66be38e6efc/data/OxCGRT_nat_latest.csv"
#url = "https://github.com/OxCGRT/covid-policy-tracker/blob/master/data/OxCGRT_nat_latest.csv"
url = "https://raw.githubusercontent.com/OxCGRT/covid-policy-tracker/master/data/OxCGRT_nat_latest.csv"
df1 = pd.read_csv(url)

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

#print(df1[df1['CountryCode'] == 'SVN'   & (df1['CountryCode'] == 'FRA')])

#df1[df1['CountryCode'] == 'SVN'].set_index('Date')['StringencyIndex_Average_ForDisplay'].plot(
#    kind='line',
#    figsize=(12,8)
#)

#profili držav

df1[df1['CountryCode'] == 'SVN'].set_index('Date')['StringencyIndex_Average_ForDisplay'].plot(
    kind='line',
    figsize=(12,8)
)

df1[df1['CountryCode'] == 'FRA'].set_index('Date')['StringencyIndex_Average_ForDisplay'].plot(
    kind='line',
    figsize=(12,8)
)


#plt.show() 

# 2021-03-30


#print((df1[(df1['date'] > '2021-03-30' ) & (df1'CountryCode' == 'SVN')] )
print('omejen datum:')
print(df1.dtypes)


print(df1['Date'].value_counts())

print((df1['Date'] > 20220601 ) & (df1['CountryCode'] == 'SVN'))
#print((df['age'] < 35) & ~(df['state'] == 'NY'))
#zgled iz https://note.nkmk.me/en/python-pandas-multiple-conditions/

#df2= df2.assign(SI_POV_GINI=merged_left.iloc[:,1:7].mean(axis=1))

#df2 = merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country'  ]].copy()

#pov_str= df1.groupby('CountryCode')['StringencyIndex_Average_ForDisplay'].mean()
pov_str= df1.loc[(df1['Date'] < 20220601 )].groupby('CountryCode')['StringencyIndex_Average_ForDisplay'].mean()
pov_str1= df1.loc[(df1['Date'] > 20220601 )].groupby('CountryCode')['StringencyIndex_Average_ForDisplay'].mean()
# primer, izbor samo po in pred datumeom kot ozačen df2.loc[df2["year"]<"1998"].groupby('country')[['value']]

#s.to_frame()
df2= pd.DataFrame(pov_str)
df2['Three_Letter_Country_Code'] = df2.index
df2.rename(columns={"StringencyIndex_Average_ForDisplay": "StringencyIndex_Average_FD_do_6_22"})
df2= pd.DataFrame(pov_str1)

print (df2) 

#df2= df2.assign(SI_POV_NAHC=merged_left.iloc[:,1:7].mean(axis=1))

#print(pov_str)
#print('//////////////////////')
#print(type(pov_str))

#df2 = pd.DataFrame(pov_str, columns=['Three_Letter_Country_Code', 'StringencyIndex_Average'])

#print(df2)

# https://www.statology.org/summary-statistics-pandas/

#Viri: 
#https://linuxhint.com/plot-data-pandas-python/ 
#https://note.nkmk.me/en/python-pandas-multiple-conditions/
#https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html 
# https://github.com/Roche/pyreadstat
#https://ofajardo.github.io/pyreadstat_documentation/_build/html/index.html
# https://ofajardo.github.io/pyreadstat_documentation/_build/html/index.html#metadata-object-description 
# https://github.com/Roche/pyreadstat 
#https://www.marsja.se/how-to-read-write-spss-files-in-python-pandas/
# https://www.marsja.se/how-to-read-stata-files-in-python-with-pandas/ 
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html
# https://www.geeksforgeeks.org/working-with-missing-data-in-pandas/
# https://datagy.io/pandas-select-assign/ 
# https://www.tutorialspoint.com/python/python_variable_types.htm
#https://stackoverflow.com/questions/37697195/how-to-merge-two-data-frames-based-on-particular-column-in-pandas-python
#  https://linuxhint.com/plot-data-pandas-python/
# https://towardsdatascience.com/plotting-with-python-c2561b8c0f1f 
# https://datatofish.com/list-column-names-pandas-dataframe/
# https://towardsdatascience.com/plotting-with-python-c2561b8c0f1fž
# https://linuxhint.com/plot-data-pandas-python/
# https://nbviewer.org/github/tgherzog/wbgapi/blob/master/examples/wbgapi-cookbook.ipynb 
# https://pythonguides.com/python-plot-multiple-lines/
# https://martakolczynska.com/post/participation-inequality-indices/#freedom-house-excel-file-with-by-year-sheets
# https://github.com/fsolt/swiid/tree/master/data
# https://martakolczynska.com/post/participation-inequality-indices/#the-standardized-world-income-inequality-database-swiid-plain-csv-file
# https://databank.worldbank.org/metadataglossary/all/series?search=gini
# https://www.geeksforgeeks.org/how-to-get-column-names-in-pandas-dataframe/
# https://blogs.worldbank.org/opendata/introducing-wbgapi-new-python-package-accessing-world-bank-data
# https://gist.github.com/stevewithington/20a69c0b6d2ff846ea5d35e5fc47f26c
# #
# #
# #
# #
# #
# #


