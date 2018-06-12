#https://www.w3resource.com/python-exercises/string/

#1. Write a Python program to calculate the length of a string.
def calculatestringlength(x):
	print(len(x))
calculatestringlength("How long is this string") #return 23

#2. Write a Python program to count the number of characters (character frequency) in a string. Sample String: google.com.  Expected Result: {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
from collections import Counter
text = "google.com"
print(list(text)) #print ['g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm']
splittext= list(text)
counter = Counter(splittext)
print(counter) #print Counter({'o': 3, 'g': 2, 'l': 1, 'e': 1, '.': 1, 'm': 1, 'c': 1})

#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string. Sample String: 'w3resource' Expected Result: 'w3ce'. Sample String: 'w3' Expected Result: 'w3w3'. Sample String: ' w' Expected Result: Empty String.
def first2last2(x):
	if len(x) > 4:
		print("{0:.2}{1:}".format(x,x[len(x)-2:len(x)]))
	elif len(x) == 4:
		print(x)
	elif len(x) == 3:
		print("{0:}".format(x))
	elif len(x) == 2:
		print("{0:}{0:}".format(x))
	else:
		print("*empty string*")
first2last2("w3resource") #print w3c3
first2last2("w3") #print w3w3
first2last2("w39") #print w39
first2last2("w3re") #print w3re
first2last2("w") #print *empty string*
first2last2("raymond") #print rand

#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself. Sample String: 'restart' Expected Result: 'resta$t'.
def dollarsign(x):
	letterchange = x[0]
	finalx = letterchange+""
	for eachx in x[1:]:
		if eachx == letterchange:
			eachx = "$"
		finalx = finalx + eachx
	print(finalx)
dollarsign("restart") #print resta$t
dollarsign("smississippi") #print smi$$i$$ippi
string4 = "restart"
string5 = string4[1:].replace(string4[0],"$")
print(string4[0]+string5)  #print resta$t

#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Sample String: 'abc', 'xyz' Expected Result: 'xyc abz'.
#RM:  iterate and enumerate
#swap the first character in each string
twostrings = ["abc", "xyz"]
swapfirst = twostrings[0][0]
swapsecond = twostrings[1][0]
for index, eachtwostrings in enumerate(twostrings):
	print(index, eachtwostrings)
	if index == 0:
		twostrings[index] = eachtwostrings.replace(eachtwostrings[0],swapsecond)
	if index == 1:
		twostrings[index] = eachtwostrings.replace(eachtwostrings[0],swapfirst)
onestring = " ".join(twostrings)
print(onestring) #print xbc ayz
#swap the second character in each string
twostrings = ["abc", "xyz"]
swapfirst = twostrings[0][0]+twostrings[0][1]
swapsecond = twostrings[1][0]+twostrings[1][1]
for index, eachtwostrings in enumerate(twostrings):
	print(index, eachtwostrings)
	if index == 0:
		twostrings[index] = eachtwostrings.replace(eachtwostrings[0:2],swapsecond)
	if index == 1:
		twostrings[index] = eachtwostrings.replace(eachtwostrings[0:2],swapfirst)
threestring = " ".join(twostrings)
print(threestring) #print xyc abz
#swap the second character in each string user input
twostrings = input("Enter two strings separated by a space ")
twostrings = twostrings.split()
swapfirst = twostrings[0][0]+twostrings[0][1]
swapsecond = twostrings[1][0]+twostrings[1][1]
for index, eachtwostrings in enumerate(twostrings):
	print(index, eachtwostrings)
	if index == 0:
		twostrings[index] = eachtwostrings.replace(eachtwostrings[0:2],swapsecond)
	if index == 1:
		twostrings[index] = eachtwostrings.replace(eachtwostrings[0:2],swapfirst)
threestring = " ".join(twostrings)
print(threestring)