#Compare daily new cases between countries.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("owid_covid_data.csv")
# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

plt.figure(figsize=(12, 6))
for country in ['Kenya', 'USA', 'India']:
     country_data = df[df['location'] == country]
     plt.plot(country_data['date'], country_data['new_cases'], label=country)

     plt.xlabel('Date')
     plt.ylabel('Daily New Cases')
     plt.title('Comparison of Daily New Cases')
     plt.legend()
     plt.xticks(rotation=45)
     plt.show()
