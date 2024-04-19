import pandas as pd
import matplotlib.pyplot as plt 

import numpy as np
import wbgapi as wb   # I use wb as a namespace in all my work

import pyreadstat

wb_info= wb.source.info() # especially useful for seeing what databases are available

print(wb_info)


df = wb.data.DataFrame('SI.POV.NAHC', time=range(2015, 2021), labels= True)

data_top = df.head() 
df.sort_values('Country')
    
# display 
print(data_top, '/n') 
print(df) 

# The scope of these changes made to
# pandas settings are local to with statement.
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df)



#https://gist.github.com/stevewithington/20a69c0b6d2ff846ea5d35e5fc47f26c#file-country-and-continent-codes-list-csv-csv

url = "https://gist.github.com/stevewithington/20a69c0b6d2ff846ea5d35e5fc47f26c/raw/13716ceb2f22b5643ce5e7039643c86a0e0c6da6/country-and-continent-codes-list-csv.csv"
df1 = pd.read_csv(url)
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df1)

print(df1) 
df.info()
df1.info()

# Select first column of the dataframe as a series
fc= first_column = df.iloc[:, 0]
print (fc)

df_i= df.index 
print(df_i)
print('tip spremenljivke')
print(type(df_i))
df.assign(Three_Letter_Country_Code  = df.index)
data_top = df.head() 
df.sort_values('Country')
    
# display 
print(data_top, '/n') 
print(df) 
df['Three_Letter_Country_Code'] = 'USA'
df['Three_Letter_Country_Code'] = df.index
print(df.head(5))

#https://stackoverflow.com/questions/37697195/how-to-merge-two-data-frames-based-on-particular-column-in-pandas-python 
##### izbor samo Evropskih držav. 
merged_left = pd.merge(left=df, right=df1, how='left', left_on='Three_Letter_Country_Code', right_on='Three_Letter_Country_Code')
print(merged_left)
print(merged_left[merged_left['Continent_Code'] == 'EU'])

df2 = merged_left[['Continent_Code','Three_Letter_Country_Code', 'Country'  ]].copy()

print(df2)
# kako izračunati povprečje nemanjkajočih vrednosti.... 
print(merged_left.iloc[:,1:7])

df2= df2.assign(SI_POV_NAHC=merged_left.iloc[:,1:7].mean(axis=1))

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df2)

    
print(df2)


column_names_to_labels = {'Continent_Code' : None,'Three_Letter_Country_Code': 'Country abbreviation', 
'Country': 'Country name', 'SI_POV_NAHC': 	'Poverty headcount ratio at national poverty lines (% of population) (last three years)'}


# creating bool series True for NaN values
# bool_series = pd.isnull(data["Gender"])


# construct new file with a selection of variables
# country_indices = merged_left[["Age", "Sex"]]

# dokumentacija https://github.com/Roche/pyreadstat za oblikovanje definicij spremenljivk
#column_names_to_labels = {'SiteCountry': 'Country name', 'CountryISO': 'Country abbreviation', 'Continent': None}
# https://ofajardo.github.io/pyreadstat_documentation/_build/html/index.html#metadata-object-description 

path = '../../covid_19_delo/Serban_a/country_level_data/Country_measures.sav'
pyreadstat.write_sav(df2, path, column_labels=column_names_to_labels)

#itanic["Age"] > 35


#df.info()
#print(df.)


# 
#  Convert the whole dataframe as a string and display

#display(df.to_string())

#print(file_rda)


#df, meta = pyreadstat.read_dta(dtafile)

#df, meta = pyreadstat.read_sav('../../covid_19_delo/Serban_a/country_level_data/Metanorms_and_other_country_measures.sav')



#https://github.com/ofajardo/pyreadr#basic-usage--reading-files
#https://pypi.org/project/pyreadr/ 
