import pandas as pd

import pyreadstat

import pyreadr


#dtafile = '../../covid_19_delo/Serban_a/country_level_data/swiid9_3.dta'
rdafile = '../../covid_19_delo/Serban_a/country_level_data/swiid9_3.rda'



file_rda = pyreadr.read_r(rdafile)

#print(file_rda)


#df, meta = pyreadstat.read_dta(dtafile)

#df, meta = pyreadstat.read_sav('../../covid_19_delo/Serban_a/country_level_data/Metanorms_and_other_country_measures.sav')



#https://github.com/ofajardo/pyreadr#basic-usage--reading-files
#https://pypi.org/project/pyreadr/ 
