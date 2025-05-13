#Plot total deaths over time
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("owid_covid_data.csv")
# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

#Plot total deaths over time.
plt.figure(figsize=(12, 6))
for country in ['Kenya', 'USA', 'India']:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)

    plt.xlabel('date')
    plt.ylabel('Total Deaths')
    plt.title('Total COVID-19 Deaths Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()
