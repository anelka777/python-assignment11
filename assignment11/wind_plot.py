import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.wind(return_type='pandas')

print("First 10 rows:")
print(df.head(10))
print("\nLast 10 rows:")
print(df.tail(10))

df['strength'] = df['strength'].str.replace(r"[^\d.]", "", regex=True).astype(float)

fig = px.scatter(
    df,
    x='frequency',
    y='strength',
    color='direction',
    title='Wind Strength vs Frequency by Direction',
    labels={'frequency': 'Frequency (%)', 'strength': 'Wind Strength (km/h)'}
)

fig.write_html("wind.html")

fig.show()
