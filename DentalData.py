import pandas as pd
import numpy as np
import openpyxl
import random
import math
from faker import Faker
from datetime import datetime, timedelta

Gender_makeup = {
    "Female": 269235,
    "Male": 201932,
    "Transgender": 60,
    "Unknown": 31175
}

Race_makeup = {
    "American Indian or Alaska Native": 474,
    "Asian": 6646,
    "Black or African American": 18140,
    "Middle Eastern or North African": 1318,
    "Native Hawaiian or Other Pacific Islander": 131,
    "White": 28468,
    "Some other race, ethnicity, or origin": 7834
}

Ethnicity_makeup = {
    "Hispanic or Latino": 29237,
    "Not Hispanic or Latino": 21884
}

Language_makeup = {
    "Afar": 3,
    "Afrikaans": 1,
    "Albanian": 3,
    "American Sign Language": 9,
    "Amharic": 3,
    "Arabic": 254,
    "Armenian": 4,
    "Aymara": 1,
    "Basque": 1,
    "Belarusian": 1,
    "Bengali": 4,
    "Burmese": 12,
    "Chinese": 336,
    "Czech": 1,
    "Declined to Answer": 3,
    "Maldivian": 1,
    "English": 100961,
    "Esperanto": 4,
    "Estonian": 1,
    "Faroese": 12,
    "French": 27,
    "German": 4,
    "Greek": 5,
    "Guarani": 1,
    "Gujarati": 12,
    "Hebrew": 1,
    "Hindi": 40,
    "Icelandic": 1,
    "Igbo": 5,
    "Italian": 4,
    "Japanese": 59,
    "Javanese": 1,
    "Khmer": 4,
    "Kinyarwanda": 2,
    "Korean": 45,
    "Kurdish": 1,
    "Lao": 2,
    "Latin": 14,
    "Malay": 2,
    "Malayalam": 3,
    "Mongolian": 1,
    "Nepali": 5,
    "Oromo": 1,
    "Pashto": 5,
    "Persian": 45,
    "Polish": 5,
    "Portuguese": 29,
    "Romanian": 1,
    "Romansh": 1,
    "Russian": 24,
    "Serbian": 3,
    "Sinhalese": 2,
    "Somali": 3,
    "Spanish": 19686,
    "Swahili": 7,
    "Swedish": 1,
    "Tagalog": 4,
    "Tamil": 2,
    "Telugu": 3,
    "Thai": 11,
    "Tigrinya": 4,
    "Turkish": 39,
    "Twi": 1,
    "Ukrainian": 8,
    "Unknown": 374645,
    "Urdu": 145,
    "Vietnamese": 341,
    "Yoruba": 3,
}

Age_makeup = {
    "GreatEq9LessEq26": 53360,
    "GreatEq27LessEq45": 63312
}

Insurance_makeup = {
    1: 76326,
    0: 426076
}

Department_makeup = {
    "UTPB": 42406,
    "Mobile Dental Van Patient": 6258,
    "Pediatric Clinic - HMC": 21057,
    "School 0f Dentistry": 300614,
    "Special Patient Clinic": 369,
    "Texas Children's - Greenpoint": 7366,
    "UT Dentists": 19263
}

def makeup_statistics(dictionary):
    total = 0
    for key, value in dictionary.items():
        total += value

    for key, value in dictionary.items():
        probability = value / total
        print(f'The object {key} with a frequency of {value} has probability {probability}.')

#makeup_statistics(Gender_makeup)
#makeup_statistics(Race_makeup)
#makeup_statistics(Ethnicity_makeup)

num_samples = 1000

total = 0

# Define Categories and their probabilities
Categories = []
Probabilities = []

for key, value in Gender_makeup.items():
    total += value
for key, value in Gender_makeup.items():
    probability = value / total
    Categories.append(key)
    Probabilities.append(probability)

# Generation of Synthetic Data

synthetic_data = np.random.choice(Categories, size=num_samples, p=Probabilities)
#print(synthetic_data)

fake = Faker()
Synthetic_Names = [ ]

for item in synthetic_data:
    if item=="Male":
        Synthetic_Names.append(fake.name_male())
    elif item=="Female":
        Synthetic_Names.append(fake.name_female())
    else:
        Synthetic_Names.append(fake.name())

# Creating the Pandas DataFrame with Data
df = pd.DataFrame({"Patient": Synthetic_Names})

df["Gender"] = synthetic_data
#print(df.head(20))


total = 0
Categories = []
Probabilities = []

for key, value in Race_makeup.items():
    total += value
for key, value in Race_makeup.items():
    probability = value / total
    Categories.append(key)
    Probabilities.append(probability)

synthetic_data = np.random.choice(Categories, size=num_samples, p=Probabilities)
df["Race"] = synthetic_data


# Check Ethnicity frequencies

total = 0
Categories = []
Probabilities = []

for key, value in Ethnicity_makeup.items():
    total += value
for key, value in Ethnicity_makeup.items():
    probability = value / total
    Categories.append(key)
    Probabilities.append(probability)

synthetic_data = np.random.choice(Categories, size=num_samples, p=Probabilities)
df["Ethnicity"] = synthetic_data

#print(df.head(20))

# Language
total = 0
Categories = []
Probabilities = []

for key, value in Language_makeup.items():
    total += value
for key, value in Language_makeup.items():
    probability = value / total
    Categories.append(key)
    Probabilities.append(probability)

synthetic_data = np.random.choice(Categories, size=num_samples, p=Probabilities)
df["Language"] = synthetic_data


# Age
Age_Data = [ ]

total_ages = Age_makeup["GreatEq9LessEq26"] + Age_makeup["GreatEq27LessEq45"]

# 9-26 27-45
# Cant be greater than 45
for key, value in Age_makeup.items():
    if key == "GreatEq9LessEq26":
        Ages = [i for i in range(9, 27)]
        Probability = Age_makeup[key] / total_ages
        random_ages = random.choices(Ages, k= round(Probability * num_samples))
        Age_Data = Age_Data + random_ages
    elif key == "GreatEq27LessEq45":
        Ages = [i for i in range(27, 46)]
        Probability = Age_makeup[key] / total_ages
        random_ages = random.choices(Ages, k= round(Probability * num_samples))
        Age_Data = Age_Data + random_ages

random.shuffle(Age_Data)
print(len(Age_Data))
df["Age"] = Age_Data
print(df.head(20))

# Birthdate




#Insurance
total = 0
Categories = []
Probabilities = []

for key, value in Insurance_makeup.items():
    total += value
for key, value in Insurance_makeup.items():
    probability = value / total
    Categories.append(key)
    Probabilities.append(probability)

synthetic_data = np.random.choice(Categories, size=num_samples, p=Probabilities)
df["Insured"] = synthetic_data
#


# Vaccine Group (Group: HPV, Trade Name: Gardasil 9)
Vaccine_Group = []
Vaccine_TradeName = []
for i in range(len(df)):
    Vaccine_Group.append("HPV")
    Vaccine_TradeName.append("Gardasil 9")

df["Vaccine_Group"] = Vaccine_Group
df["Vaccine_TradeName"] = Vaccine_TradeName



# Clinic/Office
total = 0

# Define Categories and their probabilities
Categories = []
Probabilities = []

for key, value in Department_makeup.items():
    total += value
for key, value in Department_makeup.items():
    probability = value / total
    Categories.append(key)
    Probabilities.append(probability)

synthetic_data = np.random.choice(Categories, size=num_samples, p=Probabilities)
df["Clinic/Office"] = synthetic_data

# Date Vaccine Given

Dates = [ ]
for age in df["Age"]:
    if age <= 13:
        start_date = datetime(2025, 1, 1)
        end_date = datetime(2025, 6, 26)
        Dates.append(fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d'))
    elif age <= 18:
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2025, 6, 26)
        Dates.append(fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d'))
    elif age <= 25:
        start_date = datetime(2015, 1, 1)
        end_date = datetime(2025, 6, 26)
        Dates.append(fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d'))
    elif age <= 35:
        start_date = datetime(2010, 1, 1)
        end_date = datetime(2025, 6, 26)
        Dates.append(fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d'))
    else:
        start_date = datetime(2005, 1, 1)
        end_date = datetime(2025, 6, 26)
        Dates.append(fake.date_between(start_date=start_date, end_date=end_date).strftime('%Y-%m-%d'))

df["Date_Vaccine_Given"] = Dates

# Vaccine Manufacturer/Lot Number
Manufacturer = [ ]
for i in range(len(df)):
    Manufacturer.append("Merck & Co")

df["Manufacturer"] = Manufacturer



# Vaccine Administrator

Names = [ ]
for i in range(len(df)):
    last_name = fake.last_name()
    Names.append('Dr.' + ' ' + last_name)

df["Vaccine_Administrator"] = Names

# Child + Gender
HasChild = {
    "Under 20": 5.6,
    "20-29": 49.3,
    "30-39": 41.8,
    "40 and older": 3.3
}

HasChild_List = [ ]

for age in df["Age"]:
    if age < 15:
        HasChild_List.append(0)
    elif 15 <= age <= 20:
        Categories = [ 1, 0]
        Probabilities = [0.056, 0.944]
        HasChild_List.append(np.random.choice(Categories, size=1, p=Probabilities)[0])
    elif 20 < age < 30:
        Categories = [ 1, 0]
        Probabilities = [0.549, 0.451]
        HasChild_List.append(np.random.choice(Categories, size=1, p=Probabilities)[0])
    else:
        Categories = [ 1, 0]
        Probabilities = [0.967, 0.033]
        HasChild_List.append(np.random.choice(Categories, size=1, p=Probabilities)[0])

df["Has_Child"] = HasChild_List

ChildGender = [ ]
Categories = ["Male", "Female"]
Probabilities = [0.5, 0.5]
for id in df["Has_Child"]:
    if id == 0:
        ChildGender.append("NA")
    else:
        ChildGender.append(np.random.choice(Categories, size=1, p=Probabilities)[0])

df["Child_Gender"] = ChildGender


#Child Info (Name, Birthdate)

Child_Name = [ ]

for gender in df['Child_Gender']:
    if gender == "Male":
        Child_Name.append(fake.first_name_male()+' '+fake.last_name())
    elif gender == "Female":
        Child_Name.append(fake.first_name_female()+' '+fake.last_name())
    else:
        Child_Name.append("NA")

df["Child_Name"] = Child_Name


# Dose (Random between 1-3)
Dose = [ ]

for i in range(len(df)):
    Dose.append(np.random.choice([1, 2, 3]))

df["Dose"] = Dose

# Address Info

Address = [ ]
for i in range(len(df)):
    Address.append(fake.street_address()+', Houston, TX '+str(np.random.choice([i for i in range(77001, 77533)])))

df["Address"] = Address

# Lot Number (Based on Industry Standards with AA Configuration)

Lot_Numbers = [ ]
for i in range(len(df)):
    lot = 'A'
    numbers = np.random.choice([i for i in range(1,10)], size=5)
    for number in numbers:
        lot = lot + str(number)
    lot = lot+'A'
    Lot_Numbers.append(lot)

df["Lot_Number"] = Lot_Numbers

# Series (Whether it's a 2 or 3 dose series?)
Series = [ ]
for dose in df['Dose']:
    if dose == 3:
        Series.append(3)
    else:
        Series.append(np.random.choice([2, 3]))
df["Series"] = Series


# Date Vaccine Information Statement Given (Same as Date of Vaccine)
Date_VIS = [ ]
for date in df["Date_Vaccine_Given"]:
    Date_VIS.append(date)
df["Date_VIS_Given"] = Date_VIS

# Site of Injection
Site_of_Injection = [ ]
for i in range(len(df)):
    Site_of_Injection.append('Deltoid Upper Arm')
df["Site_of_Injection"] = Site_of_Injection

# Route


# Telephone


# Email



print(df)
df.to_excel("SyntheticData.xlsx", index=False)



