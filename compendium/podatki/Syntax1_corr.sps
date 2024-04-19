* Encoding: UTF-8.

GET 
  FILE='C:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\covid_19_delo\Serban_a\country_level_data\Merge_all_num.sav'. 
DATASET NAME DataSet2 WINDOW=FRONT.
FREQUENCIES VARIABLES=Tightness_adjusted_scale
  /ORDER=ANALYSIS.

RENAME VARIABLES Tightness_adjusted_scale = Togost.
RENAME VARIABLES Individualism = Individualizem.
RENAME VARIABLES SUPPOSE_NATIONAL_GOVERNMENT = Podpora_vladi.
RENAME VARIABLES SATISFACTION_PANDEMIC_MEASURES = Zadovoljstvo_z_ukrepi.
RENAME VARIABLES LIMITATION_INDIVIDUAL_FREEDOMS_JUSTIFIED = Omejevanje_svobode.
RENAME VARIABLES Everyone_should_get_vaccinated_it_is_civic_duty = Cepljenje_dolžnost.
RENAME VARIABLES All_Less_Vaccinated_Later_Never = Namera_cepljenja.
RENAME VARIABLES False_Viruses = Zarota_virusi.
RENAME VARIABLES StringencyIndex_Average_FD_do_6_22 = Strogost.
RENAME VARIABLES Mobility_Total = Mobilnost.

freq 
Togost
Individualizem
Podpora_vladi
Zadovoljstvo_z_ukrepi
Omejevanje_svobode
Cepljenje_dolžnost
Namera_cepljenja
Zarota_virusi
Strogost
Mobilnost.


DATASET ACTIVATE DataSet2.
CORRELATIONS
  /VARIABLES=Individualizem Togost Omejevanje_svobode 
    Podpora_vladi Zarota_virusi
  /PRINT=TWOTAIL NOSIG LNODIAG
  /MISSING=PAIRWISE.

save OUTFILE= 'C:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\covid_19_delo\Serban_a\country_level_data\Merge_all_num_SI_imena.sav'. 
