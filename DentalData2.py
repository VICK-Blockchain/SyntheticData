import pandas as pd
import numpy as np
import openpyxl
import random
import math
from faker import Faker

# Data pulled from BigMouth Repositories
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
    "Yoruba": 3
}

Age_makeup = {
    "Less than 25": 63007,
    "Equal to 25": 3708,
    "Greater than 25": 172758
}

patients = 502402

def makeup_statistics(dictionary):
    for key, value in dictionary.items():
        probability = value / patients
        print(f'The object {key} with a frequency of {value} has probability {probability}.')


# makeup_statistics(Gender_makeup)
# makeup_statistics(Race_makeup)
# makeup_statistics(Ethnicity_makeup)

num_samples = 1000

fake = Faker()
Synthetic_Names = [ ]

for i in range(0, num_samples):
    Synthetic_Names.append(fake.name())

df = pd.DataFrame({"Patient": Synthetic_Names})

# Define Categories and their probabilities
Categories = []
Probabilities = []

for key, value in Gender_makeup.items():
    probability = value / patients
    Categories.append(key)
    Probabilities.append(probability)

null_prob = 1 - sum(Probabilities)
Probabilities.append(null_prob)
Categories.append("NaN")

# Generation of Synthetic Data
num_samples = 1000

synthetic_data = np.random.choice(Categories, size=num_samples, p=Probabilities)

# Creating the Pandas DataFrame with Data
df["Gender"] = synthetic_data
# print(df.head(20))


Categories = []
Probabilities = []

for key, value in Race_makeup.items():
    probability = value / patients
    Categories.append(key)
    Probabilities.append(probability)

null_prob = 1 - sum(Probabilities)
Probabilities.append(null_prob)
Categories.append("NaN")

num_samples = 1000

synthetic_data = np.random.choice(Categories, size=num_samples, p=Probabilities)
df["Race"] = synthetic_data

# print(df.head(20))


Categories = []
Probabilities = []

for key, value in Ethnicity_makeup.items():
    probability = value / patients
    Categories.append(key)
    Probabilities.append(probability)

null_prob = 1 - sum(Probabilities)
Probabilities.append(null_prob)
Categories.append("NaN")

num_samples = 1000

synthetic_data = np.random.choice(Categories, size=num_samples, p=Probabilities)
df["Ethnicity"] = synthetic_data

print(df.head(20))

# Language
Categories = []
Probabilities = []

for key, value in Language_makeup.items():
    probability = value / patients
    Categories.append(key)
    Probabilities.append(probability)

null_prob = 1 - sum(Probabilities)
Probabilities.append(null_prob)
Categories.append("NaN")

# Generation of Synthetic Data
num_samples = 1000

synthetic_data = np.random.choice(Categories, size=num_samples, p=Probabilities)

# Creating the Pandas DataFrame with Data
df["Language"] = synthetic_data

# Age
Age_Data = [ ]

total_ages = 239473

for key, value in Age_makeup.items():
    if key == "Less than 25":
        Ages = [i for i in range(1, 25)]
        Probability = Age_makeup[key] / total_ages
        random_ages = random.choices(Ages, k= math.floor(Probability * num_samples))
        Age_Data = Age_Data + random_ages
    elif key == "Equal to 25":
        Ages = [25]
        Probability = Age_makeup[key] / total_ages
        random_ages = random.choices(Ages, k= math.ceil(Probability * num_samples))
        Age_Data = Age_Data + random_ages
    elif key == "Greater than 25":
        Ages = [i for i in range(25, 90)]
        Probability = Age_makeup[key] / total_ages
        random_ages = random.choices(Ages, k=math.floor(Probability * num_samples))
        Age_Data = Age_Data + random_ages

random.shuffle(Age_Data)
#print(len(Age_Data))
df["Age"] = Age_Data
#print(df.head(20))


df.to_excel("SyntheticData2.xlsx", index=False)



