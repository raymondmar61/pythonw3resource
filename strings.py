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

#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Sample String: 'abc' Expected Result: 'abcing'. Sample String: 'string' Expected Result: 'stringly'
def ingly(word):
	if len(word) <= 2:
		return word
	elif word[len(word)-3:] == "ing":
		return word+"ly"
	else:
		return word+"ing"
print(ingly("abc")) #print abcing
print(ingly("string")) #print stringingly
print(ingly("up")) #print up

#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Sample String: 'The lyrics is not that poor!' Expected Result: 'The lyrics is good!'
samplestring = "The lyrics is not that poor!"
print(samplestring.find("not")) #print 14
print(samplestring.find("poor")) #print 23
print(samplestring.replace(samplestring[samplestring.find("not"):samplestring.find("poor")+len("poor")],"good")) #print The lyrics is good!
samplestring = "The lyrics is not really absolutely confidently poor."
print(samplestring.replace(samplestring[samplestring.find("not"):samplestring.find("poor")+len("poor")],"good")) #print The lyrics is good.

#8. Write a Python function that takes a list of words and returns the length of the longest one.
listofwords = ["Down", "at", "the", "train", "they", "go", "to", "Independence", "every", "day", "But", "anywhere", "else", "now", "seems", "like", "a", "million", "miles", "away", "xmenmarvelvscapcomstreetfighter", "And", "I", "must", "have", "been", "high", "to", "believe", "that", "i", "would", "ever", "leave", "Now", "I'm", "just", "a", "flat", "fine", "line", "like", "the", "Wichita", "Skyline", "longestwordever"]
longestone = 0
for eachlistofwords in listofwords:
	if len(eachlistofwords) > longestone:
		longestone = len(eachlistofwords)
print(longestone)

#9. Write a Python program to remove the nth index character from a nonempty string.
nonemptystring = "The quick brown fox jumped over the lazy dog."
print(nonemptystring.replace(nonemptystring[5],"")) #print The qick brown fox jmped over the lazy dog.
print(nonemptystring.replace(nonemptystring[3],"")) #print Thequickbrownfoxjumpedoverthelazydog.
print(nonemptystring.replace(nonemptystring[3],"",1)) #print Thequick brown fox jumped over the lazy dog.
print(nonemptystring.replace(nonemptystring[3],"",2)) #print Thequickbrown fox jumped over the lazy dog.
print(nonemptystring.replace(nonemptystring[3],"",3)) #print Thequickbrownfox jumped over the lazy dog.

#10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
givenstring = "The quick brown fox jumped over the lazy dog"
print(givenstring[len(givenstring)-1]+givenstring[1:len(givenstring)-1]+givenstring[0]) #print ghe quick brown fox jumped over the lazy doT

#11. Write a Python program to remove the characters which have odd index values of a given string.
#In Python, strings are immutable, so you have to create a new string.  https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
givenstring = "The quick brown fox jumped over the lazy dog"
newgivenstring = ""
for x in range(0,len(givenstring)):
	if x % 2 == 0:
		newgivenstring = newgivenstring + givenstring[x]
print(newgivenstring) #print Teqikbonfxjme vrtelz o

#12. Write a Python program to count the occurrences of each word in a given sentence.
from collections import Counter
givensentence = "The quick brown fox jumped over the lazy dog with brown cat and brown hamster."
words = givensentence.split() #converts each string word into a list of words
counter = Counter(words)
wordsfrequencycount = counter.most_common()
print(wordsfrequencycount) #[('brown', 3), ('jumped', 1), ('dog', 1), ('fox', 1), ('the', 1), ('with', 1), ('lazy', 1), ('and', 1), ('quick', 1), ('The', 1), ('cat', 1), ('hamster.', 1), ('over', 1)]