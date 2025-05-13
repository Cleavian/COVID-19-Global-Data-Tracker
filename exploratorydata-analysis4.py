#Calculate the death rate: total_deaths / total_cases.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("owid_covid_data.csv")

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

#Calculate death rate
df['death_rate'] = df['total-deaths'] / df['total_cases']

#Display the results
print(df[['date', 'location', 'death_rate']].dropna())