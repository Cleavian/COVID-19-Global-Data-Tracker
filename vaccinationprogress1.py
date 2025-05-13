#Plot cumulative vaccinations overtime for selected countries
import pandas as pd
import matplotlib.pyplot as plt

# loading dataset
df = pd.read_csv("owid_covid_data.csv")

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Plot cumulative vaccinations using line charts
plt.figure(figsize=(10, 5))
for country in ['Kenya', 'USA', 'India']:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country, marker='o')

plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.title('Cumulative COVID-19 Vaccinations Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
