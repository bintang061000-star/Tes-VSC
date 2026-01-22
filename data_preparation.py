import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#IMPORT FILE
df = pd.read_csv('New International_Education_Costs.csv')

#UPDATE DATA
update_city = {
    'MIT' : 'Boston'
}

update_university = {
    'Massachusetts' : 'MIT'
}

update_level = {
    'Bachelor' : 1,
    'Master' : 2,
    'PhD' : 3
}

updated_living_costs = {
    #Australia
    'Brisbane': 69.13,
    'Canberra': 69.18,
    'Melbourne': 72.62,
    'Sydney': 74.45,

    #Austria
    'Vienna': 72.95,

    #Belgium
    'Brussels': 72.15,

    #Canada
    'Montreal': 66.42,
    'Sherbrooke': 58.37,

    #China
    'Beijing': 51.57,

    #Egypt
    'Cairo': 35.10,

    #France
    'Lille': 68.37,
    'Lyon': 73.23,
    'Nice': 74.07,
    'Paris': 79.45,
    'Toulouse': 69.70,

    #Germany
    'Berlin': 67.67,
    'Hamburg': 70.27,
    'Munich': 71.17,

    #Greece
    'Athens': 62.13,

    #Netherlands
    'Amsterdam': 75.97,

    #New Zeeland
    'Auckland': 76.27,

    #Singapore
    'Singapore': 82.02,

    #South Korea'
    'Busan': 69.60,
    'Daejeon': 72.90,
    'Seoul': 82.37,

    #Spain
    'Barcelona': 69.87,

    #Switzerland
    'Basel': 96.80,
    'Lugano': 96.70,

    #UK
    'Bristol': 70.26,
    'Cambridge': 74.10,
    'Edinburgh': 69.70,
    'Leeds': 65.32,
    'London': 78.44,
    'Manchester': 67.34,

    #USA
    'Austin': 70.38,
    'Boston': 82.32,
    'Madison': 70.35
}

#APPEND YEARLY COST COLUMNS
rent_yearly = df['Rent_Yearly'] = df['Rent_USD'] * 12
tuition_yearly = df['Tuition_Yearly'] = df['Tuition_USD'] * 2

#MARKET PRICE
baseline_index_price = 1650