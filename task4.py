#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""

def isInteger(x):
  print(type(x))
  if type(x) == str:
    return False
  elif x % 2 == 0 or x % 2 == 1:
    return True
  else: 
    return False

if __name__ == "__main__":
  assert isInteger(9.5) == False
  assert isInteger(-2) == True    
  assert isInteger("hello") == False
  assert isInteger(0) == True
