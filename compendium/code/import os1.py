import pandas as pd

import pyreadstat

df, meta = pyreadstat.read_sav('./SimData/survey_1.sav')
type(df)
type(meta)
df.head()
