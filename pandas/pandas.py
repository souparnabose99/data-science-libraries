# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VsfQipvbSXZqWz9JvDtLIxgyfXRa25Cf
"""

import pandas as pd
pd.__version__

pd.set_option("display.max_columns", None)
df = pd.read_csv("/content/nyc_weather.csv")

df

df["Temperature"].max()

df["EST"][df["Events"] == "Rain"]

df["WindSpeedMPH"].mean()

data = pd.read_csv("/content/weather_data.csv")
data.head()

df.shape

data[2:5]

data.columns

data.day

data["day"]

data[["day", "event"]]

data.describe()

data.shape

data[data.temperature == data.temperature.max()]

data.day[data.temperature == data.temperature.max()]

# Install xlrd
df = pd.read_excel("/content/weather_data.xlsx")

df.head()

df.to_csv("sample.csv", index=False)

# Install openpyxl

df.to_excel("sample.xlsx", sheet_name="weather")

df = pd.read_csv("/content/weather_data_cities.csv")
df.shape

df.head()

# Group-by:

gb_data = df.groupby("city")
for city, city_df in gb_data:
  print(city)
  print(city_df)

gb_data.get_group("new york")

gb_data.max()

gb_data.mean()

gb_data.describe()

weather = pd.DataFrame({
    "city": ["a", "b", "c"],
    "temp": [10, 20, 50]
})

weather_2 = pd.DataFrame({
    "city": ["e", "f", "h"],
    "temp": [90, 70, 18]
})

df = pd.concat([weather, weather_2], ignore_index=True)
df

df = pd.concat([weather, weather_2], axis=1)
df

# Merge:

weather_2 = pd.DataFrame({
    "city": ["b", "f", "h"],
    "temp": [90, 70, 18]
})

df = pd.merge(weather, weather_2, on="city", how="outer")
df

df = pd.merge(weather, weather_2, on="city", how="inner")
df

# Indexing:

data.shape

# Use index to access data:
data.loc[0]

# Use row no to access data:
data.iloc[0]

data.iloc[:5]

