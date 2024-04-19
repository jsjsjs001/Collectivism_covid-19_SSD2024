import pandas as pd

import pyreadstat

import country_converter as coco

#dir = ('c:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\covid_19_delo\Serban_a\country_level_data\')

df, meta = pyreadstat.read_sav('../../covid_19_delo/Serban_a/country_level_data/ZA7782_v1-0-0.sav')
print(type(df),"\n")
print(type(meta),"\n")
print(df.head(),"\n")
print(meta.column_names_to_labels,"\n")
print(meta.variable_value_labels,"\n")

print(type(df))
print(type(meta))

print(df.columns)
# Get all names 
#for col_name in df.columns: 
#    print(col_name)

print(df)
    
### frequency table using crosstab()function

my_crosstab = pd.crosstab(index=df["isocntry"], 
                            columns=df["qa20_11"],
                             margins=True)   # Include row and column totals
print(my_crosstab)

#### Get the row proportion
 
m_c= my_crosstab.div(my_crosstab["All"],axis=0)

print(m_c)
###################################
############### prenesi spremenljivko koda države iz indeksa v ustrezno mesto
df_i= m_c.index 
print(df_i)
print('tip spremenljivke')
print(type(df_i))
m_c.assign(Three_Letter_Country_Code  = m_c.index)
data_top = m_c.head() 
m_c['Three_Letter_Country_Code'] = m_c.index
print(df.head) 
print(data_top)
	
####konstrukcija tabele agregiranih vrezdnosti 
df2 = m_c[['Three_Letter_Country_Code', 2  ]].copy()  
df2.rename(columns={ 2.0 : "False_Viruses"}, inplace=True)

#df2.rename(columns={ df2.columns[1] : "SUPPOSE NATIONAL GOVERNMENT IN GENERAL"}, inplace=True)

print(df2)

  
# list(data) or

print(list(df2.columns))

############ od tu dalje še za ostale spremenljivke. 

my_crosstab = pd.crosstab(index=df["isocntry"], 
                            columns=df["qa20_10"],
                             margins=True)   # Include row and column totals
print(my_crosstab)

#### Get the row proportion
 
m_c= my_crosstab.div(my_crosstab["All"],axis=0)

# vsota dveh spremenljivk 
print(m_c)

print("print df2 ena" , df2)

df2 = df2.assign(False_Cancer =m_c[2.0])

#df2.rename(columns={ TutorsAssigned : "SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES"}, inplace=True)

print("print df2 dva" , df2)

############ od tu dalje še za ostale spremenljivke. 

my_crosstab = pd.crosstab(index=df["isocntry"], 
                            columns=df["qa20_9"],
                             margins=True)   # Include row and column totals
print(my_crosstab)

#### Get the row proportion
 
m_c= my_crosstab.div(my_crosstab["All"],axis=0)

# vsota dveh spremenljivk 
print(m_c)

print("print df2 ena" , df2)

df2 = df2.assign(False_Climate =m_c[2.0])

#df2.rename(columns={ TutorsAssigned : "SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES"}, inplace=True)

print("print df2 dva" , df2)

############ od tu dalje še za ostale spremenljivke. 

my_crosstab = pd.crosstab(index=df["isocntry"], 
                            columns=df["qa20_7"],
                             margins=True)   # Include row and column totals
print(my_crosstab)

#### Get the row proportion
 
m_c= my_crosstab.div(my_crosstab["All"],axis=0)

# vsota dveh spremenljivk 
print(m_c)

print("print df2 ena" , df2)

df2 = df2.assign(False_Soc_Sci =m_c[2.0])

#df2.rename(columns={ TutorsAssigned : "SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES"}, inplace=True)

print("print df2 dva" , df2)

column_names_to_labels = {'Three_Letter_Country_Code': 'Country abbreviation', 'False_Viruses' : 'Viruses have been produced in government laboratories to control our freedom',
    'False_Cancer' : 'The cure for cancer exists but is hidden from the public by commercial interests' ,
    'False_Climate' : 'Climate change is for the most part caused by natural cycles rather than human activities' ,
    'False_Soc_Sci' : 'The methods used by the natural sciences and the social sciences are equally scientific'  }
#
##############za DE emd eno in drugo 
df2.loc['DE'] = ['DE',     0.7073278 ,	0.5719452 ,	0.7000762 ,	0.2776268 ]


df2 = df2.sort_index()
print(df2)



iso3_codes = coco.convert(names= df2['Three_Letter_Country_Code'], to='ISO3')
print(iso3_codes)

df2['Three_Letter_Country_Code']= iso3_codes
print(df2) 

path = '../../covid_19_delo/Serban_a/country_level_data/EB3_Survey.sav'
pyreadstat.write_sav(df2, path, column_labels=column_names_to_labels)



# https://github.com/owid/covid-19-data/tree/master/public/data glej za cepljenje!
   