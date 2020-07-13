""" 
Linear equation solver.
by Rick Gosalvez 050120 
"""

import numpy as np
import pandas as pd
import re

def file_name():
  """ check for, open, and load csv matrix. """
  count = 0
  while count == 0:
    f = input('Enter csv file name: ')
    try:
      postfix = re.findall('.[cC][sS][vV]', f)
      if postfix[0] == '.csv':
        try:
          open_f = pd.read_csv(f, header=None)
          count = 1
          return open_f
        except:
          print('File does not exist.')
    except:
    	print('Not a csv.')

def solveable(A,b):
  """ 
  Sovle using np.linalg.solve - "Solves the linear equation set a * x = b 
  for the unknown x for square a matrix."
  Requires x to be square, if x not square, will be 'no solution'.
  Quit if no solution. 
  https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.solve.html
  """
  try:
    calc = np.linalg.solve(A, b)
    return calc
  except:
    print()
    print('No Solution')
    quit()

df = file_name()

print()
print('Length of Array')
df_len = len(df.columns)-1
print(df_len)

print()
print('Matrix Array')
print(df.head())

# convert pandas to numpy array
np_arr = df.to_numpy()

# slice x values (independent data)
x = np_arr[:, :df_len] 
print()
print('x values (data / independent variables)')
print(x)
 
# slice y values (dependent data)
y = np_arr[:, df_len:]
print()
print('y values (target / dependent variables)')
print(y)

# rename to match linear algebra convention and solve
A = x
b = y

solved = solveable(A,b)

print()
print('Beta values for linear equation')
print(solved)

print()
print('Solution check')

# Use solved betas to make predictions
for data, actual in zip(A, b):
  x = np.array([data])
  prediction = np.dot(x, solved[:,0])
  if prediction == actual:
    match = 'match'
  else:
    match = 'does not match'
  print(f'predicted number = {prediction} | {actual} = actual number | {match}')
