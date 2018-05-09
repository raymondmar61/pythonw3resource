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

#2. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
from itertools import permutations
for eachpossible in permutations(['a','e','i','o','u'],5):
	print("".join(map(str, eachpossible)))

#3. Write a Python program to remove and print every third number from a list of numbers until the list becomes empty.
from random import randint
numberlistlength = randint(2,29)
numberlist = []
counter = 0
while counter <= numberlistlength:
	numberlist.append(randint(1,20))
	counter +=1
print(numberlist) #print [5, 10, 14, 12, 20, 3, 5, 13, 20, 15, 7, 13, 13, 8]
print(numberlist[2::3]) #print [14, 3, 20, 13]

#4. Write a Python program to find unique triplets whose three elements gives the sum of zero from an array of n integers.
def threeintegerssumzero(input):
	for everythree in range(0,len(integerslist)-2):
		if integerslist[everythree]+integerslist[everythree+1]+integerslist[everythree+2] == 0:
			print("We have a zero",integerslist[everythree],integerslist[everythree+1],integerslist[everythree+2])
from random import randint
integerslistlength = randint(10,30)*3
integerslist = []
counter = 1
while counter <= integerslistlength:
	integerslist.append(randint(-20,20))
	counter +=1
print(integerslist) #print [1, -15, -17, -17, 13, 13, 20, 12, -16, -8, 19, 2, -2, -19, 18, -16, 9, -19, 18, -2, 6, 8, 13, 10, 2, 17, 10, -6, -4, -12]
threeintegerssumzero(integerslist) #print We have a zero 10 -6 -4

#5. Write a Python program to create the combinations of 3 digit combo.
from random import randint
from itertools import combinations
combinationlist = []
counter = 1
while counter <6:
	combinationlist.append(randint(1,10))
	counter +=1
print(combinationlist) #print [4, 5, 9, 2, 1]
print(list(combinations(combinationlist,3))) #print [(4, 5, 9), (4, 5, 2), (4, 5, 1), (4, 9, 2), (4, 9, 1), (4, 2, 1), (5, 9, 2), (5, 9, 1), (5, 2, 1), (9, 2, 1)]

#6. Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies.
from collections import Counter
#text file contains the text
filename = "declarationofindependence.txt"
with open(filename) as fileobject:
	lines = fileobject.read() #read() prints the text file as-is.
words = lines.split() #takes each string goes into a list words
counter = Counter(words)
wordsfrequencycount = counter.most_common()
print(wordsfrequencycount) #print [('the', 49), ('of', 30), ('and', 15), ('in', 13), ('to', 12), ('Declaration', 12), ('a', 10), ('on', 9), ('The', 9), ('was', 8), ('that', 8), ('by', 8), ('July', 7), ('Congress', 6), ('which', 6), ('States', 6), ('Independence', 6), . . . ,('across', 1), ('may', 1), ('pursuit', 1), ('Netherlands', 1), ('sentence:', 1)]

#7. Write a Python program to count the number of each character of a given text of a text file.
#open text file, convert string to uppercase, convert file to a list of characters
filename = "declarationofindependence.txt"
with open(filename) as fileobject:
	lines = fileobject.read().upper()
eachcharacter = list(lines)
#print the counter in a dictionary format defaultdict
from collections import defaultdict
countlist = defaultdict(int)
for eacheachcharacter in eachcharacter:
	countlist[eacheachcharacter] += 1
print(dict(countlist)) #print {'1': 6, 'C': 117, 'X': 4, 'G': 61, 'T': 290, '"': 6, '8': 2, '3': 1, 'N': 277, ' ': 616, '–': 1, ',': 34, 'Y': 54, 'F': 72, 'I': 236, '2': 3, ')': 5, '.': 28, 'E': 425, 'V': 25, 'L': 128, 'U': 79, 'O': 212, 'A': 277, 'K': 8, 'H': 159, 'J': 17, '5': 1, 'B': 46, '6': 3, '7': 5, '[': 1, '4': 3, 'D': 168, '(': 5, '\n': 17, "'": 3, 'M': 61, 'W': 45, 'Z': 1, ':': 2, ']': 1, '-': 5, 'R': 184, '9': 3, 'S': 196, 'Q': 3, 'P': 68}

#8. Write a Python program to get the top stories from Google news.

#9. Write a Python program to get a list of locally installed Python modules.
print(help('modules'))
#At the command-line, type-->pydoc modules
#At the command-line for pip modules such as numpy and matplotlib, type-->pip list

#10. Write a Python program to display some information about the OS where the script is running

#11. Write a Python program to check the sum of three elements (each from an array) from three arrays is equal to a target value. Print all those three-element combinations. Go to the editor
# Sample data:
# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# target = 70
from itertools import combinations
x = [10, 20, 20, 20]
y = [10, 20, 30, 40]
z = [10, 30, 40, 20]
combinationelement = 3
target = 70
#function sum target value 70 from three-element combinations
def targetfunction(numberlist):
	targetlist = []
	findtarget = list(combinations(numberlist,combinationelement))
	for eachfindtarget in findtarget:
		if sum(eachfindtarget) == target:
			targetlist.append(eachfindtarget)
	print(targetlist)
# targetfunction(x)
# targetfunction(y)
# targetfunction(z) #incorrect, combine three lists into one array
#combine three lists to one list or one array
xyz = x + y + z
targetfunction(xyz)


