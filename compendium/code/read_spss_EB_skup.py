import pandas as pd

import pyreadstat
import country_converter as coco 
#importing the os module
import os

#change current working directory to 'data'
os.chdir('compendium/podatki')
#dir1 = os.getcwd()

df, meta = pyreadstat.read_sav('ZA7738_v1-0-0.sav')
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
df2.rename(columns={ 1.0 : "SUPPOSE_NATIONAL_GOVERNMENT"}, inplace=True)

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

df2 = df2.assign(SATISFACTION_PANDEMIC_MEASURES=m_c["SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES"])


#df2.rename(columns={ TutorsAssigned : "SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES"}, inplace=True)

print("print df2 ena" , df2)

############ od tu dalje še za ostale spremenljivke. 

my_crosstab = pd.crosstab(index=df["isocntry"], 
                            columns=df["q14"],
                             margins=True)   # Include row and column totals
print(my_crosstab)


#### Get the row proportion
 
m_c= my_crosstab.div(my_crosstab["All"],axis=0)


# vsota dveh spremenljivk 
m_c["LIMITATION_INDIVIDUAL_FREEDOMS-JUSTIFIED"]= m_c[1.0] + m_c[2.0]+ m_c[3.0]
print(m_c)

print("print df2 ena" , df2)

df2 = df2.assign(LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED=m_c["LIMITATION_INDIVIDUAL_FREEDOMS-JUSTIFIED"])

print("print df2 ena" , df2)

############ od tu dalje še za ostale spremenljivke. 

#my_crosstab = pd.crosstab(index=df["isocntry"],                            columns=df["q19"],                             margins=True)   # Include row and column totals
#my_crosstab = pd.crosstab(index=df["isocntry"],                            columns=df["q20t_1"],                             margins=True)   # Include row and column totals

#df2.rename(columns={ df2.columns[1] : "SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES"}, inplace=True)
#isocntry q1 q1r q2 q3 q14 q19  


column_names_to_labels = {'Three_Letter_Country_Code': 'Country abbreviation', 'SUPPOSE_NATIONAL_GOVERNMENT': 'SUPPOSE/OPPOSE NATIONAL GOVERNMENT IN GENERAL',
'SATISFACTION_PANDEMIC_MEASURES': 	'SATISFACTION WITH GOVERNMENT CORONAVIRUS PANDEMIC MEASURES' , 'LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED' : 'LIMITATION OF INDIVID FREEDOM - JUSTIFIED VS OPPOSED'}
#####################################################################################################################


df, meta = pyreadstat.read_sav('ZA7771_v1-0-0.sav')
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

#združene prvi dve kategoriji
m_c[5]= m_c[1.0] + m_c[2.0]
print(m_c)

# vsota dveh spremenljivk 
#m_c["LIMITATION_INDIVIDUAL_FREEDOMS-JUSTIFIED"]= m_c[1.0] + m_c[2.0]+ m_c[3.0]
print(m_c)

print("print df2 ena" , df2)

df2 = df2.assign(Everyone_should_get_vaccinated_it_is_civic_duty=m_c[5])

print("print df2 ena" , df2)




######še ena spremenljivka###########################################################################################

### frequency table using crosstab()function

my_crosstab = pd.crosstab(index=df["isocntry"], 
                            columns=df["q1"],
                             margins=True)   # Include row and column totals
print(my_crosstab)

# 'q1': {1.0: 'As soon as possible', 2.0: 'Some time in 2021', 3.0: 'Later', 4.0: 'Never', 5.0: 'I have already been vaccinated', 998.0: "Don't know", 999.0: 'Prefer not to answer'
# 'q1': 'Q1 When would you like to get vaccinated against COVID-19 (coronavirus)?',
# 'q5_3': 'Q5_3 To what extent do you agree or disagree with each of the following statements? Everyone should get vaccinated against COVID-19, it is a civic duty'
# 'q5_3': {1.0: 'Totally agree', 2.0: 'Tend to agree', 3.0: 'Tend to disagree', 4.0: 'Totally disagree', 998.0: "Don't know"},
#### Get the row proportion 
 
m_c= my_crosstab.div(my_crosstab["All"],axis=0)

print(m_c)

#združene prvi dve kategoriji
m_c[6]= 1 - (m_c[3.0] + m_c[4.0])
print(m_c)

# vsota dveh spremenljivk 
#m_c["LIMITATION_INDIVIDUAL_FREEDOMS-JUSTIFIED"]= m_c[1.0] + m_c[2.0]+ m_c[3.0]
print(m_c)

print("print df2 ena" , df2)

df2 = df2.assign(All_Less_Vaccinated_Later_Never=m_c[6])

print("print df2 ena" , df2)

print(df2)

out_format = "ISO3"

df2['Three_Letter_Country_Code'] = coco.convert(names=df2['Three_Letter_Country_Code'], to=out_format, not_found=None)

print(df2)



#################################################################################################



# creating bool series True for NaN values
# bool_series = pd.isnull(data["Gender"])


# construct new file with a selection of variables
# country_indices = merged_left[["Age", "Sex"]]

# dokumentacija https://github.com/Roche/pyreadstat za oblikovanje definicij spremenljivk
#column_names_to_labels = {'SiteCountry': 'Country name', 'CountryISO': 'Country abbreviation', 'Continent': None}
# https://ofajardo.github.io/pyreadstat_documentation/_build/html/index.html#metadata-object-description 

path = 'Eu_Par_COVID-19_Survey.sav'
pyreadstat.write_sav(df2, path, column_labels=column_names_to_labels)