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

def makeup_statistics(dictionary):
    total = 0
    for key, value in dictionary.items():
        total += value

    for key, value in dictionary.items():
        probability = value / total
        print(f'The object {key} with a frequency of {value} has probability {probability}.')

makeup_statistics(Gender_makeup)
