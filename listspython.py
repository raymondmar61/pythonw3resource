#https://www.w3resource.com/python-exercises/list/

#1. Write a Python program to sum all the items in a list.
numberlist = [x for x in range(1,11)]
print(sum(numberlist)) #print 55

#2. Write a Python program to multiplies all the items in a list.
from random import randint
counter = 1
numberlist = []
while counter <= 10:
	numberlist.append(randint(1,10))
	counter += 1
initial = 1
for eachnumberlist in numberlist:
	initial = initial * eachnumberlist
print(numberlist)
print(initial)

#3. Write a Python program to get the largest number from a list.
from random import randint
counter = 1
numberlist = []
while counter <= 10:
	numberlist.append(randint(1,100))
	counter += 1
initial = 1
print((numberlist))
print(max(numberlist))

#4. Write a Python program to get the smallest number from a list.
from random import randint
counter = 1
numberlist = []
while counter <= 10:
	numberlist.append(randint(1,101))
	counter += 1
initial = 1
print((numberlist))
print(min(numberlist))

#5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Sample List: ['abc', 'xyz', 'aba', '1221'].  Expected Result: 2
def list5(samplelist):
	count = 0
	for eachsamplelist in samplelist:
		if len(eachsamplelist) <= 1:
			pass
		if eachsamplelist[0] == eachsamplelist[-1]:
			count += 1
	print(count)
list5(['abc', 'xyz', 'aba', '1221']) #return 2
list5(['xh', 'uppu', '987789', 'jackkcaj', 'dod', 'snakes', 'waterfall']) #return 5

#6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Sample List: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)].  Expected Result: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
samplelist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(samplelist[0]) #print (2, 5)
print(samplelist[0][1]) #print 5
print(samplelist[3]) #print (2, 3)
print(samplelist[3][0]) #print 2
print(samplelist[3][1]) #print 3
print(sorted(samplelist)) #print [(1, 2), (2, 1), (2, 3), (2, 5), (4, 4)]
secondnumber = lambda samplelist: samplelist[1]
samplelist.sort(key=secondnumber, reverse=False) #print [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
print(samplelist)

#7. Write a Python program to remove duplicates from a list.
duplicatelist = ["apple","banana","pear","apple","grapes"]
duplicatelist = set(duplicatelist)
duplicatelist = list(duplicatelist)
print(duplicatelist) #print ['apple', 'banana', 'pear', 'grapes']

#8. Write a Python program to check a list is empty or not.
#emptylist = ["book","game","music","phone"]
emptylist = []
if emptylist:
	print("list is full")
else:
	print("list is empty")

#9. Write a Python program to clone or copy a list.
copylist = [1, 45, 3, 6, 87, 99, 1000]
copylist2 = copylist[:]
print(copylist2) #print [1, 45, 3, 6, 87, 99, 1000]

#10. Write a Python program to find the list of words that are longer than n from a given list of words.
listofwords = ["monopoly","mystery","bargain","gijoe","xmen","set","life","operation"]
n = 6
for eachlistofwords in listofwords:
	if len(eachlistofwords) > n:
		print(eachlistofwords)

#11. Write a Python function that takes two lists and returns True if they have at least one common member.
def twolists(lista, listb):
	isittrue = set(lista).intersection(set(listb))
	if isittrue:
		return True
	else:
		return False
lista = ["apple","banana","grape"]
listb = ["apple","kiwi","peach","grape"]
print(twolists(lista, listb)) #print True
lista = ["dice","scale","phone"]
listb = ["apple","kiwi","peach","grape"]
print(twolists(lista, listb)) #print False

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List: ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'].  Expected Output: ['Green', 'White', 'Black']
samplelist = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
samplelist.pop(0)
samplelist.pop(3) #Red is deleted, Green is index 0, Pink  is index 3
samplelist.pop(3) #Green is deleted, White is index 0, Yellow is index 3
print(samplelist) #print ['Green', 'White', 'Black']

#13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
firstarray = []
for n in range(0,3):	
	secondarray = []
	for n in range(0,4):
		thirdarray = []
		for n in range(0,6):
			thirdarray.append("*")
		secondarray.append(thirdarray)
	firstarray.append(secondarray)
print(firstarray) #print 
"""
[[['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']],
[['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']], 
[['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*'], ['*', '*', '*', '*', '*', '*']]]
"""

#14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
allnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddnumbersonly = [eachallnumbers for eachallnumbers in allnumbers if eachallnumbers % 2 != 0]
print(oddnumbersonly) #print [1, 3, 5, 7, 9]

#15. Write a Python program to shuffle and print a specified list.
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(shuffle(color)) #print None
shuffle(color)
print(color) #print ['Pink', 'Green', 'Yellow', 'Red', 'Black', 'White']

#16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).  RM: print a list of numbers squared between 1 and 30 inclusive.
squarednumbers = [x**2 for x in range(0,30)]
print(squarednumbers[0:5]) #print [0, 1, 4, 9, 16]
print(squarednumbers[-5:]) #print [625, 676, 729, 784, 841]
print(squarednumbers[-5:].sort(reverse = True)) #print None
backwards = squarednumbers[-5:]
backwards.sort(reverse=True)
print(backwards) #print [841, 784, 729, 676, 625]
print(squarednumbers[0:5]+squarednumbers[-5:]) #print [0, 1, 4, 9, 16, 625, 676, 729, 784, 841]