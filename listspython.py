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

#10. Write a Python program to find the list of words that are longer than n from a given list of words.listofwords = ["monopoly","mystery","bargain","gijoe","xmen","set","life","operation"]
n = 6
for eachlistofwords in listofwords:
	if len(eachlistofwords) > n:
		print(eachlistofwords)