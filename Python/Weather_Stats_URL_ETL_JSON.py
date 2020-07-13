""""
Weather Stats JSON Document Creator
Get public data from URL, filter, sort, analyze 72 records per day, and output as JSON document.
by Rick Gosalvez 031320 
"""

import urllib.request
import json

cum_data = []
year     = 2020           # 2020
month    = 2              # Feb
days     = range(1,30)		# number of days in month
day_dict = {}

# loop through API for month of Feb and save data
for day in days:
  with urllib.request.urlopen(f"https://www.metaweather.com/api/location/2487956/{year}/{month}/{day}") as response:
    data = response.read()
    weather_dict = json.loads(data.decode("utf-8"))
    cum_data.append(weather_dict)

# loop through nested data to extract only relevant dates where applicable_date = created
for entry in cum_data:
  day_temps = []
  day_stats = []
  for i in entry:
    if i['created'][:10] == i['applicable_date']:
      day_temps.append(i['the_temp'])

  # calc max, min, ave for each day
  day_stats.append(max(day_temps))
  day_stats.append(min(day_temps))
  day_stats.append(sum(day_temps)/len(day_temps))
  day_dict[i['applicable_date']] = day_stats

# serialize to JSON
json_string = json.dumps(day_dict, sort_keys=True, indent=5)
print(f'{json_string}\n')

filename = 'temp_stats.json'

print(f'{filename} JSON document created for {month} {year}.')

# write to temp_stats.json file
with open(filename, 'w') as f:
	json.dump(json_string, f)