import pandas as pd

import pyreadstat

#importing the os module
import os
#to get the current working directory
directory = os.getcwd()
print('tole: ', directory, ' konec')
os.chdir('c:/Users/stebej/OneDriveUL2021/OneDrive - Univerza v Ljubljani/RSF_Odprta_ucna_gradiva_2023/Učna gradiva/RSF_Odprta_Ucna_Gradiva/compendium/code/')
dir1 = os.getcwd()
print('tole 1: ', dir1, ' konec')

# read data file with missing values included, and with numeric values
df, meta = pyreadstat.read_sav('../podatki/popis15c_F1.sav', user_missing=True)

# read data file with missing values as NaN, and with labels instead of values
df_lab, meta_lab = pyreadstat.read_sav('../podatki/popis15c_F1.sav',  apply_value_formats=True)

# inspect the properties of the file
print(type(df),"\n")
print(type(meta),"\n")
print(df.head(),"\n")
print(meta.column_names_to_labels,"\n")
print(meta.variable_value_labels,"\n")

print(type(df))
print(type(meta))
print(type(meta.column_names_to_labels))

 

# absolute frequencies
## my_crosstab = pd.crosstab(index=df["go_pol1"], columns='count',  margins=True)   
m_c = pd.crosstab(index=df["go_pol1"], columns='count',  margins=True)  

## print(my_crosstab)
##m_c=my_crosstab

# intermediate result
print(m_c)
print(m_c.index)
# prepare to include labels in the table of results
print(type(meta.variable_value_labels))
print(meta.variable_value_labels["go_pol1"],"\n")
print(meta.variable_value_labels["go_pol1"].values(),"\n")

# add one element to the labels dict, for the total count
meta.variable_value_labels["go_pol1"].update({4:'All'})
m_c["Labele"] = meta.variable_value_labels["go_pol1"].values() 

# intermediate result
print(type(m_c),"\n")

# the value labels lenght should match the number of rows                  
#meta.variable_value_labels["go_pol1"].values())
print(m_c[['Labele','count','All']])


# columnts percentages, with missing excluded
my_crosstab = pd.crosstab(index=df_lab["go_pol1"], columns='count', normalize='columns', margins=True)  
print(my_crosstab)

# Include row and column totals
# print(my_crosstab)

#find proportions
#m_c=my_crosstab/my_crosstab.sum()

# print(m_c1)

#m_c_1 = pd.DataFrame.from_dict(meta.variable_value_labels["go_pol1"]) 
#m_c["Labele"] = meta.variable_value_labels["go_pol1"]
# print(m_c_1)
# create a crosstab table of gender and education level with visualization
# ct_viz = pd.crosstab(df['gender'], df['education_level'])
# ct_viz.plot(kind='bar', stacked=True)