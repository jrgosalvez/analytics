""" 
Numpy and Pandas Data Manipulation
by Rick Gosalvez 050120 
"""

import numpy as np
import pandas as pd

# load data
df = pd.read_csv('cities.csv')

# print shape
print('Data shape')
print(df.shape)

# explore data
print()
print('Data sample')
print (df.head())

# a. The largest and smallest cities in terms of total area
a_large = df.loc[:,['city','area_total_sq_mi']].max()
a_small = df.loc[:,['city','area_total_sq_mi']].min()
print()
print('a.')
print(f'Largest city by Total Area:    {a_large[0]} at {a_large[1]} square miles')
print(f'Smallest city by Total Area:   {a_small[0]} at {a_small[1]} square miles')

# b. The top 10 cities in terms of elevation.
b = df.loc[:,['city','elevation_ft']].sort_values(by='elevation_ft', ascending=False)
print()
print('b. Top 10 cities by elevation')
print(b[:10].to_string(index=False))

# c. Average land area, water area and total area.
c = df.loc[:,['area_total_sq_mi','area_land_sq_mi','area_water_sq_mi']].mean()
print()
print(f'c. Average total area, water, and land for {len(df)} cities.')
print(f'Ave. Total Area: {c[0]:.2f}')
print(f'Ave. Total Area: {c[1]:.2f}')
print(f'Ave. Total Area: {c[2]:.2f}')

# d. Cities between latitude of 36o and 38o and longitude of -120o and -116o.
d = df.loc[(df['latd'] >= 36.0) & (df['latd'] <= 38.0) & (df['longd'] >= -120.0) & (df['longd'] <= -116.0), ['city','latd','longd']]
print()
print(f'd. {len(d):.0f} cities between 36 and 38 degrees latitude and -120 and -116 longitude.')
# print(d)
print(d.to_string(index=False))
#print(d.shape)
#print(len(d))

# e. Cities with total population within the interquartile range.
e = df.loc[:,['population_total']].sort_values(by='population_total', ascending=False)

# define quartile break points
q75, q25 = np.percentile(e, [75 ,25])

# filter by quartile break points
e_q50 = df.loc[(df['population_total'] >= q25) & (df['population_total'] <= q75)].sort_values(by='population_total', ascending=False)
print()
print(f'e. {len(e_q50):.0f} cities and their populations in the interquartile range (q25: {q25:.0f} and q75 {q75:.0f}.')
print(e_q50)