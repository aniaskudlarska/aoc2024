with open('day2\input.txt') as input:
  lineList = input.read().splitlines()
#print(lineList)

#analyze a list of numbers and return TRUE if numbers are all increasing OR decreasing AND two adjacent numbers only differ by 1,2,3

def checkList(x):
  '''
  return TRUE if list matches conditions of challenge
  false otherwise
  '''
  
def checkDecreasing(x):
  '''
  check if list is in strictly descending order i.e each element is greater than its next element
  '''
  for i in range(len(x) - 1):  # Iterate up to the second-to-last element
        if x[i] <= x[i + 1]:   # Check if current element is NOT greater than the next
          return False
  return True

def checkIncreasing(x):
  '''
  check if list is in descending order
  '''
  for i in range(len(x) - 1):  # Iterate up to the second-to-last element
        if x[i] > x[i + 1]:   # Check if current element is greater than the next
          return False
  return True

def checkRange(x):
  '''
  check if every change between numbers in list is greater than 0, less than 3
  '''
  for i in range(len(x)-1):
    if abs(x[i]-x[i+1]) == 0:
        return False
    if abs(x[i]-x[i+1]) > 3:
        return False
  return True

def checkSafe(x):
  if checkDecreasing(x):
    if not checkRange(x):
      return False
  if checkIncreasing(x):
    if not checkRange(x):
      return False  
  if not checkIncreasing(x) and not checkDecreasing(x):
    return False
  
  return True

def formatInput(x):
  outListFinal = [[int(i) for i in s.split()] for s in x ]
  return outListFinal
    
finalList = (formatInput(lineList))


def countSafe(y):
  safeVal = 0
  for report in y:
    if checkSafe(report):
      safeVal +=1
  return safeVal

print(countSafe(finalList))
#Part 1 answer: 472

#part 2: the same, but can tolerate one issue 
# remove the offending number, and then try again?
def checkIncreasing_Purge(x):
  '''
  check if list is in descending order
  '''
  for i in range(len(x) - 1):  # Iterate up to the second-to-last element
        if x[i] > x[i + 1]:   # Check if current element is greater than the next
          return False
  return True

def checkRange_Purge(x):
  '''
  check if every change between numbers in list is greater than 0, less than 3
  '''
  for i in range(len(x)-1):
    if abs(x[i]-x[i+1]) == 0:
        return False
    if abs(x[i]-x[i+1]) > 3:
        return False
  return True

#come back to this one