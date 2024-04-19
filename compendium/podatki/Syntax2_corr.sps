* Encoding: UTF-8.

GET 
  FILE='C:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\covid_19_delo\Serban_a\country_level_data\Merge_all_num_SI_imena.sav'. 
DATASET NAME DataSet2 WINDOW=FRONT.

freq 
Zadovoljstvo_z_ukrepi
Cepljenje_dolžnost
Namera_cepljenja
Strogost
Mobilnost
.



DATASET ACTIVATE DataSet2.
*CORRELATIONS
  /VARIABLES=Individualizem Togost Omejevanje_svobode 
    Podpora_vladi Zarota_virusi
  /PRINT=TWOTAIL NOSIG LNODIAG
  /MISSING=PAIRWISE.

* CORRELATIONS
  /VARIABLES=
  Zadovoljstvo_z_ukrepi
  Cepljenje_dolžnost
  Namera_cepljenja
  Mobilnost
  Strogost
    with 
  Individualizem Togost Omejevanje_svobode Podpora_vladi Zarota_virusi
  /PRINT=TWOTAIL NOSIG LNODIAG
  /MISSING=PAIRWISE.
* izločene nezanimive in podvojene spremenljivke. 
 CORRELATIONS
  /VARIABLES=
  Zadovoljstvo_z_ukrepi
  Namera_cepljenja
  Mobilnost
    with 
  Individualizem Togost Omejevanje_svobode Podpora_vladi Zarota_virusi
  /PRINT=TWOTAIL NOSIG LNODIAG
  /MISSING=PAIRWISE.

*save OUTFILE= 'C:\Users\stebej\OneDriveUL2021\OneDrive - Univerza v Ljubljani\covid_19_delo\Serban_a\country_level_data\Merge_all_num_SI_imena.sav'. 

DATASET ACTIVATE DataSet1.
FREQUENCIES VARIABLES=tip_druz go_pol1 vzp_druz star1 sp st_ot_dr roj_st1 akt2 izb2 st_urb1
  /ORDER=ANALYSIS.
