import pandas as pd
df = pd.read_csv('boston-police-department-fio.csv')
df2 = pd.read_csv('fieldcontactforpublic2015.csv')
df2_name = pd.read_csv('fieldcontactnameforpublic2015.csv')
df3 = pd.read_csv('mark43_fieldcontacts_for_public_20192.csv')
df2_full = df2.merge(df2_name, how="outer", right_on=["fc_num"], left_on=["fc_num"])
print(df2_full.columns)
print(df.columns)
print(df2.columns)
print(df3.columns)
print(df['DESCRIPTION'])
df = df.rename(columns={"FIO_ID": "fc_num", "Sex": "sex", "FIO_DATE": 'contact_date', ""})
#df4 = df.merge(df2, left_on="")

#keep FIO_ID, Location, FIO_DATE, BASIS, STOP_REASONS, FIOFS_REASONS, VEH_MAKE, VEH_Color, VEH_Model, VEH_state, Supervisor_id, Supervisor, City, Race, FIO_TIME, Ethnicity, Outcome, Complextion, clothing
#toss FIO_TIme, Clothing, Complexion, fiofs_type, Terrorism
#?