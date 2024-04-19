import pandas as pd
import matplotlib.pyplot as plt 

import numpy as np
import wbgapi as wb   # I use wb as a namespace in all my work


wb_info= wb.source.info() # especially useful for seeing what databases are available

print(wb_info)


df = wb.data.DataFrame('SI.POV.NAHC', time=range(2016, 2022), labels= True)

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


df.loc[pd.isnull(df['YR2020'])] = 0

print('zamenjane vrednosti')
print(df)