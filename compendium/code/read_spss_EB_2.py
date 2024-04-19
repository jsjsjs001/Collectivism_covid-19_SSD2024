import pandas as pd

import pyreadstat

#dir = ('c:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\covid_19_delo\Serban_a\country_level_data\')

df, meta = pyreadstat.read_sav('../../covid_19_delo/Serban_a/country_level_data/ZA7771_v1-0-0.sav')
print(type(df),"\n")
print(type(meta),"\n")
print(df.head(),"\n")
print(meta.column_names_to_labels,"\n")
print(meta.variable_value_labels,"\n")

print(type(df))
print(type(meta))

print(df)
	
### frequency table using crosstab()function

my_crosstab = pd.crosstab(index=df["isocntry"], 
                            columns=df["q5_3"],
                             margins=True)   # Include row and column totals
print(my_crosstab)

# 'q1': {1.0: 'As soon as possible', 2.0: 'Some time in 2021', 3.0: 'Later', 4.0: 'Never', 5.0: 'I have already been vaccinated', 998.0: "Don't know", 999.0: 'Prefer not to answer'
# 'q1': 'Q1 When would you like to get vaccinated against COVID-19 (coronavirus)?',
# 'q5_3': 'Q5_3 To what extent do you agree or disagree with each of the following statements? Everyone should get vaccinated against COVID-19, it is a civic duty'
# 'q5_3': {1.0: 'Totally agree', 2.0: 'Tend to agree', 3.0: 'Tend to disagree', 4.0: 'Totally disagree', 998.0: "Don't know"},
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

#združene prvi dve kategoriji
m_c[5]= m_c[1.0] + m_c[2.0]
print(m_c)
	
####konstrukcija tabele agregiranih vrezdnosti 
df2 = m_c[['Three_Letter_Country_Code', 4  ]].copy()  
df2.rename(columns={ 5 : "Everyone_should_get_vaccinated_it_is_civic_duty"}, inplace=True)
# Everyone should get vaccinated against COVID-19, it is a civic duty
#df2.rename(columns={ df2.columns[1] : "SUPPOSE NATIONAL GOVERNMENT IN GENERAL"}, inplace=True)

print(df2)

  
# list(data) or

print(list(df2.columns))

