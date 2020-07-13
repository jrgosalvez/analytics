""" 
Cities Density by Location
by Rick Gosalvez 051820 
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')     # style

cities = pd.read_csv('cities.csv')     # import data
cities                                 # preview data

# create new dataframe and preview subset of data
print('10 Records of Subset Data Frame')
xs = cities.loc[:,['city','longd','latd','population_total','area_total_sq_mi']].sort_values(by='city', ascending=False)
print(xs[:10].to_string(index=False))
print()

# convert populations to log base 10
print('10 Records of Subset Data Frame with Log 10 of Populations')
xs['population_total'] = np.log10(xs['population_total'])
print(xs[:10].to_string(index=False))

# plot 
x      = xs['longd']
y      = xs['latd']
colors = xs['population_total']   # log base 10 of population
sizes  = 10 * xs['area_total_sq_mi']   # circle sizes based on total area

plt.figure(figsize=(12, 8))

plt.scatter(x, y, 
            c=colors, s=sizes,
            alpha=0.8,         # transparency bx 0 to 1
            cmap='Spectral')

plt.colorbar();  # show color scale on right
plt.title('Cities: Area and Population')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()
