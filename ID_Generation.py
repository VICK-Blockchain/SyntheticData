import pandas as pd
import math
import numpy as np

df = pd.read_excel('SyntheticData.xlsx')

VICK_ID = {

}

total = 0
j = 0
for i in range(len(df)):
    if df["Patient"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Patient"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Gender"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Gender"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Race"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Race"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value


for i in range(len(df)):
    if df["Ethnicity"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Ethnicity"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Language"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Language"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Age"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Age"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Birth_Date"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Birth_Date"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Insured"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Insured"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Vaccine_Group"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Vaccine_Group"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Vaccine_TradeName"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Vaccine_TradeName"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Clinic/Office"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Clinic/Office"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Date_Vaccine_Given"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Date_Vaccine_Given"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Manufacturer"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Manufacturer"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Vaccine_Administrator"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Vaccine_Administrator"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Has_Child"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Has_Child"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Child_Gender"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Child_Gender"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Child_Name"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Child_Name"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Child_Age"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Child_Age"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Child_Birth_Date"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Child_Birth_Date"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Dose"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Dose"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Address"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Address"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Lot_Number"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Lot_Number"][i]
        value = 'VICK_'+str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Series"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Series"][i]
        value = 'VICK_' + str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Date_VIS_Given"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Date_VIS_Given"][i]
        value = 'VICK_' + str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Site_of_Injection"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Site_of_Injection"][i]
        value = 'VICK_' + str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Route"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Route"][i]
        value = 'VICK_' + str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Telephone"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Telephone"][i]
        value = 'VICK_' + str(j)
        VICK_ID[key] = value

for i in range(len(df)):
    if df["Email"][i] in VICK_ID:
        total += 1
    else:
        j += 1
        key = df["Email"][i]
        value = 'VICK_' + str(j)
        VICK_ID[key] = value

New_VICK_ID = {

}


point = '_'
for key, value in VICK_ID.items():
    index = value.find(point)
    numbers = value[index + len(point):]
    if len(numbers) == 1:
        number = 'VICK_000'+numbers
        New_VICK_ID[key] = number
    elif len(numbers) == 2:
        number = 'VICK_00'+numbers
        New_VICK_ID[key] = number
    elif len(numbers) == 3:
        number = 'VICK_0'+numbers
        New_VICK_ID[key] = number
    else:
        New_VICK_ID[key] = 'VICK_'+numbers

#print(New_VICK_ID)

Complete_ID = {

}

for key, value in New_VICK_ID.items():
    if key == "Male":
        Complete_ID[key] = "PATO_0000384"
    elif key == "Female":
        Complete_ID[key] = "PATO_0000383"
    elif key == "HPV":
        Complete_ID[key] = "NCBITaxon_10566"
    elif key == "Merck & Co":
        Complete_ID[key] = "VO_0000695"
    elif key == "Intramuscular (IM)":
        Complete_ID[key] = "VO_0000340"
    elif key == "English":
        Complete_ID[key] = "OMRSE_00000610"
    elif key== "Spanish":
        Complete_ID[key] = "OMRSE_00000849"
    elif key== "Gardasil 9":
        Complete_ID[key] = "VO_0015037"
    elif key == "White":
        Complete_ID[key] = "OMRSE_00000219"
    elif key == "Black or African American":
        Complete_ID[key] = "OMRSE_00000217"
    elif key == "American Indian or Alaska Native":
        Complete_ID[key] = "OMRSE_00000215"
    elif key == "Asian":
        Complete_ID[key] = "OMRSE_00000216"
    elif key == "Native Hawaiian or Other Pacific Islander":
        Complete_ID[key] = "OMRSE_00000218"
    elif key == "Middle Eastern or North African":
        Complete_ID[key] = "NCIT_C43866"
    elif key == "Hispanic or Latino":
        Complete_ID[key] = "OMRSE_00000207"
    elif key == "Not Hispanic or Latino":
        Complete_ID[key] = "OMRSE_00000208"
    else:
        Complete_ID[key] = value


column_headers = df.columns.tolist()
column_headers.remove("Child_Age")

for header in column_headers:
    data = [

    ]
    for value in df[header]:
        data.append(Complete_ID[value])
    column_index = df.columns.get_loc(header) + 1
    df.insert(column_index, str(header)+'_ID', data)


ChildAgeData = [

]
for item in df["Child_Age"]:
    if item in range(0,50):
        ChildAgeData.append(int(item))
    else:
        ChildAgeData.append(item)
vals = [

]
for item in ChildAgeData:
    if item in range(0,50):
        vals.append(Complete_ID[item])
    else:
        vals.append('VICK_3300')

column_index = df.columns.get_loc("Child_Age") + 1
df.insert(column_index, 'Child_Age_ID', vals)


df.head(10)
df.to_excel("SyntheticData.xlsx", index=False)


