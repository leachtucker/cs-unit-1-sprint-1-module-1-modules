"""
Import the "math" module. Then, print an alphabetically sorted list of all the functions available in the "math" module that start with the letters "is".
"""
# YOUR CODE HERE
import math

def startsWithIs(string):
  try:
    if (string.index('is') == 0):
      return True
    else:
      return False
  except ValueError:
    # IF the string index method throws an error, that means 'is' is not in the string at all
    return False

myLst = list(filter(startsWithIs, dir(math)))

print(myLst)