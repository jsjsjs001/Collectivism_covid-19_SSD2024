import pandas as pd

import pyreadstat

#dir = ('c:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\covid_19_delo\Serban_a\country_level_data\')

df, meta = pyreadstat.read_sav('../../covid_19_delo/Serban_a/country_level_data/ZA7738_v1-0-0.sav')
print(type(df),"\n")
print(type(meta),"\n")
print(df.head(),"\n")
print(meta.column_names_to_labels,"\n")
print(meta.variable_value_labels,"\n")

print(type(df))
print(type(meta))

print(df)
	
### frequency table using crosstab()function
 
import pandas as pd
my_crosstab = pd.crosstab(index=df["isocntry"], 
                            columns=df["q1r"],
                             margins=True)   # Include row and column totals
print(my_crosstab)


#### Get the row proportion
 
m_c= my_crosstab.div(my_crosstab["All"],axis=0)

print(m_c)


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
df2 = m_c[['Three_Letter_Country_Code', 1  ]].copy()  
df2.rename(columns={ 1.0 : "SUPPOSE NATIONAL GOVERNMENT IN GENERAL"}, inplace=True)

#df2.rename(columns={ df2.columns[1] : "SUPPOSE NATIONAL GOVERNMENT IN GENERAL"}, inplace=True)

print(df2)

  
# list(data) or

print(list(df2.columns))

############ od tu dalje še za ostale spremenljivke. 

my_crosstab = pd.crosstab(index=df["isocntry"], 
                            columns=df["q2"],
                             margins=True)   # Include row and column totals
print(my_crosstab)


#### Get the row proportion
 
m_c= my_crosstab.div(my_crosstab["All"],axis=0)

# vsota dveh spremenljivk 
m_c["SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES"]= m_c[1.0] + m_c[2.0]
print(m_c)

print("print df2 ena" , df2)

df2 = df2.assign("SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES=m_c["SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES"])

print("print df2 ena" , df2)


# df2.rename(columns={ df2.columns[1] : "SUPPOSE NATIONAL GOVERNMENT IN GENERAL"}, inplace=True)


#df2.rename(columns={ df2.columns[1] : "SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES"}, inplace=True)
#isocntry q1 q1r q2 q3 q14 q19  