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

#17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
squarednumbers = [x**2 for x in range(0,30)]
print(squarednumbers[0:5]) #print [0, 1, 4, 9, 16]
print(squarednumbers[5:]) #print [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841]

#18. Write a Python program to generate all permutations of a list in Python.
import itertools
list1234 = [1, 2, 3, 4]
for productpairs in itertools.permutations(list1234, 2):
	print(productpairs,end=";") #print (1, 2);(1, 3);(1, 4);(2, 1);(2, 3);(2, 4);(3, 1);(3, 2);(3, 4);(4, 1);(4, 2);(4, 3);  RM:  prints 1,2 and 2,1
list1234comprehension = [productpairs for productpairs in itertools.permutations([1,2,3,4],2)]
print(list1234comprehension) #print [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]
list1234 = [1, 2, 3, 4]
list1234print = [productpairs for productpairs in itertools.permutations(list1234,2)]
print(list1234print) #print [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

#19. Write a Python program to get the difference between the two lists.
nameslist1 = ["Burt","Mary","Jackie","Bruno","Different1"]
nameslist2 = ["Burt","Mary","Jackie","Bruno","Different2"]
print(set(nameslist1).difference(set(nameslist2))) #print {'Different1'}
print(list(set(nameslist1) - set(nameslist2))) #print ['Different1']
print(list(set(nameslist2) - set(nameslist1))) #print ['Different2']
list1 = [1, 2, 3, 4]
list2 = [1, 2]
print(list(set(list1) - set(list2))) #print [3, 4]
print(list(set(list2) - set(list1))) #print []

#20. Write a Python program access the index of a list.
a = ["foo","bar","baz",'bar','any','much']
print(a.index("bar")) #print 1.  .index() returns only the first element which matches in the list.  ValueError appears if the target is not found.  .index(value, [start, [stop]])
thelist2 = ["foo","bar","baz","bar","bear","cat","nat","bar"]
print(thelist2.index("bar", 4,len(thelist2))) #print 7
thelist3 = ["foo","bar","baz","bar","bear","cat","nat","bar","pin","fan"]
for i, j in enumerate(thelist3): #Useful than index if there are duplicates.  index() only returns the first occurrence, while enumerate returns all occurrences.
	if j == "bar":
		print(i) #print 1\n 3\n 7\n

#21. Write a Python program to convert a list of characters into a string.
mylist = ["spam","ham","eggs"]
print(" ".join(mylist)) #print spam ham eggs
print("".join(mylist)) #print spamhameggs

#22. Write a Python program to find the index of an item in a specified list.
thelist3 = ["foo","bar","baz","bar","bear","cat","nat","bar","pin","fan"]
for i, j in enumerate(thelist3):
	if j == "cat":
		print(i) #print 5
#findcat = [i for (i, j) in enumerate[thelist3] if j == "cat"]
#print(findcat) #error message 'type' object is not subscriptable

#23. Write a Python program to flatten a shallow list.
numberslist = [[1,2], [3,4,5], [6], [7,8,9]]
flatnumberslist = []
for eachnumberslist in numberslist:
	for y in eachnumberslist:
		flatnumberslist.append(y)
print(flatnumberslist) #print [1, 2, 3, 4, 5, 6, 7, 8, 9]
flatnumberslist2 = [y for eachnumberslist in numberslist for y in eachnumberslist]
print(flatnumberslist2) #print [1, 2, 3, 4, 5, 6, 7, 8, 9]
import itertools
flatnumberslist3 = list(itertools.chain(*numberslist))
print(flatnumberslist3) #print [1, 2, 3, 4, 5, 6, 7, 8, 9]

#24. Write a Python program to append a list to the second list.  RM:  take list one and combine with list two to form one list.  Combine two lists to one list.
list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
print(list1+list2) #print [1, 2, 3, 0, 'Red', 'Green', 'Black']

#25. Write a Python program to select an item randomly from a list.
from random import randint
gameslist = ["Settlers Of Catan","Monopoly","Fluxx","Candy Land","Pandemic","Chess","Dixit"]
print(gameslist[randint(0,len(gameslist)-1)]) #print Settlers Of Catan

#26. Write a python program to check whether two lists are circularly identical.
def identicallists(list1, list2):
	if list1==list2:
		print("Identical lists")
	else:
		print("Not identical lists")
identicallists([5, 6, 7],[5, 6, 7]) #print Identical lists
identicallists([100],[200, 500]) #print Not identical lists

#Official solution
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
print('Compare list1 and list2')
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2))) #print True
print('Compare list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2))) #print False

#27.  Write a Python program to find the second smallest number in a list.  RM:  duh sort the list smallest to largest.  No max() and min().
from random import randint
# y = []
# for x in range(0,randint(5,20)):
# 	y.append(randint(1,101))
# print(y)
numberlist = [randint(1,101) for x in range(0,randint(5,20))]
print(numberlist) #print [51, 59, 59, 44, 61, 28, 38, 8, 17]
numberlist.sort()
print(numberlist) #print [8, 17, 28, 38, 44, 51, 59, 59, 61]
print(numberlist[1]) #print 17

#28. Write a Python program to find the second largest number in a list.  RM:  duh sort the list smallest to largest.  No max() and min().
from random import randint
# y = []
# for x in range(0,randint(5,20)):
# 	y.append(randint(1,101))
# print(y)
numberlist = [randint(1,101) for x in range(0,randint(5,20))]
print(numberlist) #print [48, 44, 19, 56, 88, 82, 73, 92]
numberlist.sort()
print(numberlist) #print [19, 44, 48, 56, 73, 82, 88, 92]
print(numberlist[len(numberlist)-2]) #print 88

#29. Write a Python program to get unique values from a list.
from random import randint
from collections import Counter
numberlist = [randint(1,101) for x in range(0,randint(10,40))]
print(numberlist) #print [78, 29, 40, 19, 89, 46, 25, 49, 65, 15, 46, 53, 33, 51, 76, 47, 80, 89, 1, 29, 99, 74, 68, 41, 91, 61, 90, 33, 30, 48, 72, 67, 76]
print(Counter(numberlist)) #print Counter({29: 2, 89: 2, 46: 2, 33: 2, 76: 2, 78: 1, 40: 1, 19: 1, 25: 1, 49: 1, 65: 1, 15: 1, 53: 1, 51: 1, 47: 1, 80: 1, 1: 1, 99: 1, 74: 1, 68: 1, 41: 1, 91: 1, 61: 1, 90: 1, 30: 1, 48: 1, 72: 1, 67: 1})
print(list(set(numberlist))) #print [1, 15, 19, 25, 29, 30, 33, 40, 41, 46, 47, 48, 49, 51, 53, 61, 65, 67, 68, 72, 74, 76, 78, 80, 89, 90, 91, 99]

#30. Write a Python program to get the frequency of the elements in a list.
from random import randint
from collections import Counter
numberlist = [randint(1,101) for x in range(0,randint(10,40))]
print(Counter(numberlist)) #print Counter({12: 2, 30: 2, 91: 2, 4: 2, 45: 2, 46: 2, 22: 2, 96: 1, 80: 1, 34: 1, 49: 1, 40: 1, 41: 1, 98: 1, 78: 1, 52: 1, 21: 1, 47: 1, 25: 1, 42: 1, 23: 1, 44: 1, 2: 1, 32: 1, 48: 1, 89: 1, 55: 1, 67: 1, 11: 1, 9: 1, 70: 1})

#31. Write a Python program to count the number of elements in a list within a specified range.  RM:  count how many items are between two numbers inclusive.
from random import randint
numberlist = [randint(1,101) for x in range(0,randint(10,40))]
minimumrange = 40
maximumrange = 80
count = 0
for eachnumberlist in numberlist:
	if eachnumberlist >= minimumrange and eachnumberlist <=maximumrange:
		count += 1
numberlist.sort()
print(numberlist)
print(count)

#32. Write a Python program to check whether a list contains a sublist.  Function source https://stackoverflow.com/questions/35964155/checking-if-list-is-a-sublist.  RM:  Check two lists.  Does each list have same items in same order from left to right.
def sublist(lst1, lst2):
	sublist1 = []
	sublist2 = []	
	for eachlst1 in lst1:
		if eachlst1 in lst2:
			#print("in lst1 also in lst2",eachlst1)
			sublist1.append(eachlst1)
	for eachlst2 in lst2:
		if eachlst2 in lst1:
			#print("in lst2 also in lst1",eachlst2)
			sublist2.append(eachlst2)
	print(sublist1)
	print(sublist2)
	print(sublist1==sublist2)
   #ls1 = [element for element in lst1 if element in lst2]
   #ls2 = [element for element in lst2 if element in lst1]
   #return ls1 == ls2
a = [2,4,3,5,7]
b = [4,3]
c = [7,3]
d = [1000,100,2]
e = [1,2,3,4]
f = [1,2,5,6,7,8,5,76,4,3]
g = [0,3,2]
sublist(a,b) #print [4,3]\n [4,3]\n True
sublist(a,c) #print [3,7]\n [7,3]\n False
sublist(a,d) #print [2]\n [2]\n True
sublist(d,a) #print [2]\n [2]\n True
sublist(e,f) #print [1, 2, 3, 4]\n [1, 2, 4, 3]\n False
sublist(f,g) #print [2,3]\n [3,2]\n False

#33. Write a Python program to generate all sublists of a list.  RM:  create all possible sublists from mainlist no repeats.
from itertools import combinations
def generatesublists(mainlist):
	newlist = [[]]
	n = 0
	while n <= len(mainlist):
		for eachmainlist in combinations(mainlist,n+1):
			#print(eacha)
			newlist.append(list(eachmainlist))
		n +=1
	print(newlist)
generatesublists(["x","y","z"]) #print [[], ['x'], ['y'], ['z'], ['x', 'y'], ['x', 'z'], ['y', 'z'], ['x', 'y', 'z']]
generatesublists([10, 20, 30, 40]) #print [[], [10], [20], [30], [40], [10, 20], [10, 30], [10, 40], [20, 30], [20, 40], [30, 40], [10, 20, 30], [10, 20, 40], [10, 30, 40], [20, 30, 40], [10, 20, 30, 40]]

#34. Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number.
def checkifprime(n): #n must be greater than one
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	i = 3
	while i * i <= n:
		if n % i == 0:
			return False
		i += 2
	return True
primenumberlistcheckifprime=[]
for number in range(2,101):
	if checkifprime(number) == True:
		primenumberlistcheckifprime.append(number)
print(primenumberlistcheckifprime) #print [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Sample list: ['p', 'q']. n=5. Sample Output: ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5'].
def concatenatenumber(inputlist, number):
	outputlist = [eachinputlist+str(eachn) for eachinputlist in inputlist for eachn in range(1,number+1)]
	print(outputlist)
inputlist = ["p","q"]
n = 5
concatenatenumber(inputlist, n) #return ['p1', 'p2', 'p3', 'p4', 'p5', 'q1', 'q2', 'q3', 'q4', 'q5']

#36. Write a Python program to get variable unique identification number or string.  RM:  I don't understand.  Copied solution.
x = 100
print(format(id(x), 'x')) #print a70680
s = "w3resource"
print(format(id(s), 'x')) #print 7f128e97bef0

#https://www.geeksforgeeks.org/id-function-python/  id(object) returns the identity of an object. This identity has to be unique and constant for this object during the lifetime.  This is random but when running in the same program, it generates unique and same identity.
print(id("geek")) #print 139991246589880
string1 = "geek"
string2 = "geek"
print(id(string1)) #print 139991246589880
print(id(string2)) #print 139991246589880
print(id(string1)==id(string2)) #print True

#37. Write a Python program to find common items from two lists.
firstlist = [0, 1, 2, 3, 4, 5]
secondlist = [200, 100, 1578, 3, 4, 5, 6, -5]
firstlist = set(firstlist)
secondlist = set(secondlist)
print(list(firstlist.intersection(secondlist))) #print [3, 4, 5]
print(", ".join(map(str,list(firstlist.intersection(secondlist))))) #print 3, 4, 5
firstlist = ["Johnson","Operation","X-Men","Bargain","Speakers"]
secondlist = ["X-Men","Johnson","Dixit","Spoons","Rock","Johnson"]
firstlist = set(firstlist)
secondlist = set(secondlist)
print(list(firstlist.intersection(secondlist))) #print ['Johnson', 'X-Men']
print(", ".join(map(str,list(firstlist.intersection(secondlist))))) #print Johnson, X-Men

#38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. Sample list: [0,1,2,3,4,5].  Expected Output: [1, 0, 3, 2, 5, 4].  RM:  copied solution.  New functions from a module.
from itertools import zip_longest, chain, tee
def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))
n = [0,1,2,3,4,5]
print(replace2copy(n)) #print [1, 0, 3, 2, 5, 4]
#RM:  cleaned up code after learning iterables outsidethebook
from itertools import zip_longest, chain
def replace2copy(lst):
    print(lst[1::2]) #print [1, 3, 5]
    print(lst[::2]) #print [0, 2, 4]
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))    
n = [0,1,2,3,4,5]
print(replace2copy(n)) #print [1, 0, 3, 2, 5, 4]

#39. Write a Python program to convert a list of multiple integers into a single integer.  Sample list: [11, 33, 50] Expected Output: 113350
multipleintegers = [11, 33, 50]
singleinteger = int("".join(map(str,multipleintegers)))
print(singleinteger)  #print 113350
print(type(singleinteger)) #print <class 'int'>

#40. Write a Python program to split a list based on first character of word.  RM:  return the list of words by the first letter for each word.  The answer is not a list.  The answer is words grouped by the first letter for each word.
from itertools import groupby
from operator import itemgetter
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)
"""print
a
ask
b
be
c
call
come
d
do
. . . 
"""

#41. Write a Python program to create multiple lists.  Solution:  https://stackoverflow.com/questions/13520876/how-can-i-make-multiple-empty-lists-in-python
n = 5
multiplelists = [[] for x in range(0,5)]
print(multiplelists) #print [[], [], [], [], []]
#also
samplelist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = len(samplelist)
multiplelists = [[] for x in range(0,n)]
print(multiplelists) #print [[], [], [], [], [], [], [], [], [], [], [], [], [], []]
for eachletter in samplelist:
	multiplelists[samplelist.index(eachletter)].append(eachletter)
print(multiplelists) #print [['a'], ['b'], ['c'], ['d'], ['e'], ['f'], ['g'], ['h'], ['i'], ['j'], ['k'], ['l'], ['m'], ['n']]
#official solution
obj = {}
for i in range(1, 21):
    obj[str(i)] = []
print(obj) #print {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': [], '12': [], '13': [], '14': [], '15': [], '16': [], '17': [], '18': [], '19': [], '20': []}

#42. Write a Python program to find missing and additional values in two lists. Sample data : Missing values in second list: b,a,c.  Additional values in second list: g,h.
firstlist = ["a", "b", "c", "d", "e", "f"]
secondlist = ["d", "e", "f","g","h"]
print(list(set(firstlist).difference(set(secondlist)))) #print ['a','b','c']
print(list(set(secondlist).difference(set(firstlist)))) #print ['g','h']

#43. Write a Python program to split a list into different variables.  RM:  split a list with tuples technically speaking
gamelist = [("candy land","chutes and ladders","winnie the pooh"),("mystery mansion","silicon valley","bargain hunter"),("settlers of catan","pandemic","dominion")]
gamelist1, gamelist2, gamelist3 = gamelist
print(gamelist1) #print ('candy land', 'chutes and ladders', 'winnie the pooh')
print(gamelist2) #print ('mystery mansion', 'silicon valley', 'bargain hunter')
print(gamelist3) #print ('settlers of catan', 'pandemic', 'dominion')

#44. Write a Python program to generate groups of five consecutive numbers in a list.
from itertools import count
from random import randint
mainlist = []
def groupoffivenumbers():
	randomnumber = randint(1,100)
	counter = 0
	grouplist = []
	for i in count(randomnumber):
		if counter == 5:
			break
		else:
			grouplist.append(i)
			counter += 1
	mainlist.append(grouplist)
numberofgroups = randint(1,11)
counter = 0
while counter <= numberofgroups:
	groupoffivenumbers()
	counter += 1
print(mainlist) #print [[81, 82, 83, 84, 85], [5, 6, 7, 8, 9], [39, 40, 41, 42, 43], [87, 88, 89, 90, 91], [32, 33, 34, 35, 36], [75, 76, 77, 78, 79], [30, 31, 32, 33, 34], [92, 93, 94, 95, 96]]

#45. Write a Python program to convert a pair of values into a sorted unique array.  RM:  a list consisting of tuples.  Two numbers per tuple.  Extract unique numbers.  Sort extracted unique numbers in one list.
from random import randint
tupleslist = []
def twonumbertuple():
	generatetwonumbers = randint(1,100), randint(1,100)
	tupleslist.append(generatetwonumbers)
numberoftuples = randint(20,26)
counter = 0
while counter <= numberoftuples:
	twonumbertuple()
	counter +=1
print(tupleslist) #print [(32, 1), (37, 16), (74, 91), (38, 49), (100, 15), (35, 82), (60, 17), (73, 7), (61, 66), (48, 3), (35, 25), (72, 29), (51, 85), (72, 19), (59, 91), (30, 93), (83, 61), (42, 21), (64, 14), (81, 33), (33, 35)]
print(set().union(*tupleslist)) #print {1, 3, 7, 14, 15, 16, 17, 19, 21, 25, 29, 30, 32, 33, 35, 37, 38, 42, 48, 49, 51, 59, 60, 61, 64, 66, 72, 73, 74, 81, 82, 83, 85, 91, 93, 100}
print(sorted(set().union(*tupleslist))) #print [1, 3, 7, 14, 15, 16, 17, 19, 21, 25, 29, 30, 32, 33, 35, 37, 38, 42, 48, 49, 51, 59, 60, 61, 64, 66, 72, 73, 74, 81, 82, 83, 85, 91, 93, 100]

#create a tuple integers
twonumbers = 5, 6
print(twonumbers) #print (5,6)
print(type(twonumbers)) #print <class 'tuple'>

#46. Write a Python program to select the odd items of a list.
colorlist = ["red","green","blue","white","black","orange","yellow","pink","brown","gold","silver"]
oddcolorlist = [colorlist[n] for n in range(1,len(colorlist)) if n % 2 != 0]
print(oddcolorlist) #print ['green', 'white', 'orange', 'pink', 'gold']

#47. Write a Python program to insert an element before each element of a list.  RM:  my guess is insert an item second most right of a list.
sportslist = ["baseball"]
sportslist.insert(len(sportslist)-1,"football")
print(sportslist) #print ['football', 'baseball']
sportslist.insert(len(sportslist)-1,"basketball")
print(sportslist) #print ['football', 'basketball', 'baseball']
sportslist.insert(len(sportslist)-1,"hockey")
print(sportslist) #print ['football', 'basketball', 'hockey', 'baseball']

#48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
nestedlists = [[81, 82, 83, 84, 85], [5, 6, 7, 8, 9], [39, 40, 41, 42, 43], [87, 88, 89, 90, 91], [32, 33, 34, 35, 36], [75, 76, 77, 78, 79], [30, 31, 32, 33, 34], [92, 93, 94, 95, 96]]
for eachlist in range(0,len(nestedlists)):
	print(nestedlists[eachlist][:]) #print [81, 82, 83, 84, 85]\n . . . [30, 31, 32, 33, 34]\n [92, 93, 94, 95, 96]

#49. Write a Python program to convert list to list of dictionaries. Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"].  Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
samplelistcolor = ["Black", "Red", "Maroon", "Yellow"]
samplelisthtml = ["#000000", "#FF0000", "#800000", "#FFFF00"]
expectedoutput = []
listcolorhtml = list(zip(samplelistcolor,samplelisthtml))
for eachlistcolorhtml in listcolorhtml:
	expectedoutputdictionary = {}
	expectedoutputdictionary["color_name"] = eachlistcolorhtml[0]
	expectedoutputdictionary["color_code"] = eachlistcolorhtml[1]
	expectedoutput.append(expectedoutputdictionary)
print(expectedoutput) #print [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

#50. Write a Python program to sort a list of nested dictionaries.
stocks = {"GOOG": 520.54, "FB": 76.45, "YHOO": 39.28, "AMZN": 305.21, "AAPL": 99.76}
print(sorted(zip(stocks.values(), stocks.keys()))) #print [(39.28, 'YHOO'), (76.45, 'FB'), (99.76, 'AAPL'), (305.21, 'AMZN'), (520.54, 'GOOG')] values sorted smallest to largest
print(sorted(zip(stocks.keys(), stocks.values()))) #print [('AAPL', 99.76), ('AMZN', 305.21), ('FB', 76.45), ('GOOG', 520.54), ('YHOO', 39.28)] keys sorted smallest to largest

#official solution
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original List: ")
print(my_list) #print [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("Sorted List: ")
print(my_list) #print [{'key': {'subkey': 10}}, {'key': {'subkey': 5}}, {'key': {'subkey': 1}}]

#51. Write a Python program to split a list every Nth element. Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'].  Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
samplelist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n = 3
multiplelists = [[] for x in range(0,n)]
print(multiplelists) #print [[], [], []]
counter = 0
for eachletter in samplelist:
	if counter == 0:
		multiplelists[0].append(eachletter)
	elif counter == 1:
		multiplelists[1].append(eachletter)
	elif counter == 2:
		multiplelists[2].append(eachletter)
	counter += 1
	if counter == 3:
		counter = 0
print(multiplelists) #print [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
#official solution
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C,3)) #print [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

#52. Write a Python program to compute the similarity between two lists. Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"].  Expected Output: Color1-Color2: ['white', 'orange', 'red'] Color2-Color1: ['black', 'yellow']
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]
#print(color1-color2)  #error message
color1set = set(color1)
color2set = set(color2)
print(list(color1set-color2set)) #print ['white', 'orange', 'red']
print(list(color2set-color1set)) #print ['yellow', 'black']

#53. Write a Python program to create a list with infinite elements.  Source:  https://stackoverflow.com/questions/13910259/list-with-infinite-elments
def infinitenumbers():
	infiniteelementslist = []
	count = 0
	while True:
		infiniteelementslist.append(count)
		if count % 100 == 0:
			print(infiniteelementslist)
		count += 1
		if count == 1000:
			break
infinitenumbers()
from itertools import count, islice
for i in islice(count(10),100):
	print(i) #print 10\n 11\n 12\n . . . 107\n 108\n 109
#official solution
import itertools
c = itertools.count()
print(next(c)) #print 0
print(next(c)) #print 1
print(next(c)) #print 2
print(next(c)) #print 3
print(next(c)) #print 4

