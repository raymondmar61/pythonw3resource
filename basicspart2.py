#https://www.w3resource.com/python-exercises/basic/
#1. Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other.
#RM:  more accurate is a list of integers
from random import randint
def sameordifferent(numberlist):
	uniquelist = []
	duplicatelist = []
	for x in numberlist:
		if x not in uniquelist:
			uniquelist.append(x)
		elif x in duplicatelist:
			pass
		else:
			duplicatelist.append(x)
	if len(duplicatelist) >=1:
		print("There are duplicates: "+str(duplicatelist)[1:-1])
	else:
		print("There are no duplicates: "+str(uniquelist)[1:-1])

#create a list of numbers
sequencelist = []
lengthsequencelist = randint(5,20)
counter = 1
while counter <= lengthsequencelist:
	sequencelist.append(randint(1,20))
	counter +=1
print(sequencelist)
#call function to determine a list of numbers contains duplicates
sameordifferent(sequencelist)
print("Another way remove duplicates use set().")
print(list(set(sequencelist)))

#https://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-whilst-preserving-order
from more_itertools import unique_everseen
print("Using more_itertools.unique_everseen")
print(list(unique_everseen(sequencelist)))

#Official solution
def test_distinct(data):
  count = 0
  for k in data:
    for j in range(1, len(data) - 1):
      if k == j:
        count += 1
        if count == 2:
          return False
          return True
print(test_distinct([2,4,5,7,9]))
print(test_distinct([2,4,5,5,7,9]))

#2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
from itertools import permutations
for eachpossible in permutations(['a','e','i','o','u'],5):
	print("".join(map(str, eachpossible)))