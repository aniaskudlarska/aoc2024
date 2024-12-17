#create two lists
l1 = []
l2 = []
with open("input.txt") as input:
  lineList = input.read().splitlines()

#split lists, map first number to one list, seond number to second list
for item in lineList:
  num1, num2 = map(int,item.split())
  l1.append(num1)
  l2.append(num2)

#cheeky sort  
l1==l1.sort(), l2==l2.sort()

#get distance between list items
totalDistance = 0
for i in range(len(l1)):
  totalDistance += abs(l1[i]-l2[i])

#print(totalDistance)
#part 1 answer - 1110981


#part 2 - similarity score
#add each number in left list after multiplying it by amount of times it occurs in right list
simScore = 0
for item in l1:
  simScore += (item * l2.count(item))
print(simScore)

#part 2 answer - 24869388