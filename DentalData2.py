import pandas as pd
import numpy as np
import openpyxl

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
df = pd.DataFrame({"Gender": synthetic_data})
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


# Age


df.to_excel("SyntheticData2.xlsx", index=False)



