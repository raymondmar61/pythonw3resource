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
#In Python, strings are immutable, so you have to create a new string.  Existing strings can't be modified.  You must create a new string.  You can convert them to a list which is mutable.  Then convert the list back to a string after changes.  https://stackoverflow.com/questions/3559559/how-to-delete-a-character-from-a-string-using-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
givenstring = "The quick brown fox jumped over the lazy dog"
newgivenstring = ""
for x in range(0,len(givenstring)):
	if x % 2 == 0:
		newgivenstring = newgivenstring + givenstring[x]
print(newgivenstring) #print Teqikbonfxjme vrtelz o
#bonus
examplestring = "examples"
newexamplestring = examplestring.replace("m","")
print(newexamplestring) #print exaples
#delete middle character
examplestringmiddlelength = len(examplestring)//2  #examplestringmiddlelength must be an integer
newexamplestring = examplestring[:examplestringmiddlelength]+examplestring[examplestringmiddlelength+1:]
print(newexamplestring) #print examles

#12. Write a Python program to count the occurrences of each word in a given sentence.
from collections import Counter
givensentence = "The quick brown fox jumped over the lazy dog with brown cat and brown hamster."
words = givensentence.split() #converts each string word into a list of words
counter = Counter(words)
wordsfrequencycount = counter.most_common()
print(wordsfrequencycount) #[('brown', 3), ('jumped', 1), ('dog', 1), ('fox', 1), ('the', 1), ('with', 1), ('lazy', 1), ('and', 1), ('quick', 1), ('The', 1), ('cat', 1), ('hamster.', 1), ('over', 1)]

#13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
def upperlower(word):
	uppercase = word.upper()
	lowercase = word.lower()
	print(uppercase)
	print(lowercase)
upperlower("Speaker") #return SPEAKER\n speaker

#14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically). Sample Words: red, white, black, red, green, black.  Expected Result: black, green, red, white.
def sequenceofwords(samplewords):
	samplewords = list(set(samplewords))
	samplewords.sort()
	print(samplewords) 
sequenceofwords(["red", "white", "black", "red", "green", "black"]) #return ['black', 'green', 'red', 'white']

#15. Write a Python function to create the HTML string with tags around the word(s).  Sample function and result:  add_tags('i', 'Python') -> '<i>Python</i>'.  add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def addtags(html, word):
	print("<{}>{}</{}>".format(html,word,html))
addtags("i","Python") #return <i>Python</i>
addtags("b","Python Tutorial") #return <b>Python Tutorial</b>

#16. Write a Python function to insert a string in the middle of a string. Sample function and result: insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]].  insert_sting_middle('{{}}', 'PHP') -> {{PHP}}.
def insertstringmiddle(insertstring, middlestring):
	if len(insertstring) == 1:
		print("{}{}{}".format(insertstring,middlestring,insertstring))
	else:
		leftinsertstring = insertstring[0:insertstring.rfind(insertstring[0])+1]
		rightinsertstring = insertstring[insertstring.find(insertstring[len(insertstring)-1]):]
		print("{}{}{}".format(leftinsertstring,middlestring,rightinsertstring))
insertstringmiddle("[[[]]]]]]","Python") #return [[[Python]]]]]]
insertstringmiddle("{{}}","PHP") #return {{PHP}} 
insertstringmiddle("=","equal") #return =equal=
#.find() and.rfind()
insertstring = "[[[]]]]]]"
print(insertstring.find(insertstring[0])) #print 0
print(insertstring.rfind(insertstring[0])) #print 2
print(insertstring.find(insertstring[len(insertstring)-1])) #print 3

#17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). Sample function and result: insert_end('Python') -> onononon.  insert_end('Exercises') -> eseseses.
def insertend(fourcopiesstringend):
	if len(fourcopiesstringend) <= 1:
		print("String must be two characters or greater.")
	else:
		print(fourcopiesstringend[len(fourcopiesstringend)-2:]*4)
insertend("Python") #print onononon
insertend("Exercises") #print eseseses

#18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.  Sample function and result: first_three('ipy') -> ipy. first_three('python') -> pyt.
def firstthree(stringword):
	if len(stringword) < 3:
		return stringword
	else:
		return stringword[0:3]
print(firstthree("ipy")) #print ipy
print(firstthree("python")) #print pyt
print(firstthree("id")) #print id

#19. Write a Python program to get the last part of a string before a specified character.  https://www.w3resource.com/python-exercises  https://www.w3resource.com/python
thestring = "https://www.w3resource.com/python-exercises"
thecharacter = thestring.find("-")
print(thecharacter) #print 33
print(thestring[0:thecharacter]) #print https://www.w3resource.com/python

#20. Write a Python function to reverses a string if it's length is a multiple of 4.
def multiple4string(word):
	if len(word) % 4 == 0:
		print(word[::-1])
	else:
		print(word)
multiple4string("abcdefgh") #return hgfedcba
multiple4string("operation") #return operation
multiple4string("candylandgameset") #return tesemagdnalydnac

#21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
def uppercase(word):
	count = 0
	for n in range(0,4):
		if word[n] == word[n].upper():
			count = count+1
	if count >=2:
		print(word.upper())
uppercase("AlUmni") #return ALUMNI
uppercase("PHONe") #return PHONE
uppercase("nocapitalletters") #return nothing
#bonus
print("rancore".upper()) #print RANCORE

#22.Write a Python program to sort a string lexicographically.
def lexicographicsorted(string):
	answer = sorted(sorted(string), key=len)
	return "".join(answer)
print(lexicographicsorted("w3resource")) #print 3ceeorrsuw
print(lexicographicsorted("quickbrown")) #print bciknoqruw
print(lexicographicsorted("RaymonD")) #print DRamnoy
print(lexicographicsorted("RaymonD.5hZ=")) #print .5=DRZahmnoy
#bonus
string1 = "aAaBbcCdE"
string1 = list(string1)
string1.sort()
print("".join(string1)) #print ABCEaabcd

#23. Write a Python program to remove a newline in Python.
#RM:  copied solution for which it's partially correct
str1='Python Exercises\n'
print(str1) #print Python Exercises\n
print(str1.rstrip()) #print Python Exercises
str1='Python Exercises\nokay'
print(str1) #print Python Exercises\nokay
print(str1.rstrip()) #print Python Exercises\nokay

#24. Write a Python program to check whether a string starts with specified characters.
def check(checkstring, startscharacters):
	if checkstring.find(startscharacters,0,len(startscharacters)) == 0:
		print("{} starts with {}.".format(checkstring,startscharacters))
	else:
		print("No match")
check("scrabble","scra") #return scrabble starts with scra.
check("scrabble","cra") #return No match
check("9874","9874") #return 9874 starts with 9874.
check("a","b") #return No match
check("a","a") #return a starts with a.
#bonus
checkscrabble = "scrabble"
startscharacters = "scra"
print(checkscrabble.find(startscharacters,0,len(startscharacters))) #print 0
#RM:  prints -1 if false.  .find() returns an integer.

#25. Write a Python program to create a Caesar encryption.
#reference https://stackoverflow.com/questions/15784590/how-can-you-print-a-key-given-a-value-in-a-dictionary-for-python
originalword = "Blue horseshoe loves Bluestar Airlines"

#create alphabet dictionary and encryption dictionary
alphabet = {}
encryption = {}
#lowercase letters a is 1 z is 26
x = 1
for n in range(97,123):
	alphabet[chr(n)] = x
	encryption[chr(n)] = x
	x = x + 1
#uppercase letters A is 27 Z is 52
x = 27
for n in range(65,91):
	alphabet[chr(n)] = x
	encryption[chr(n)] = x
	x = x + 1

#create encryption dictionary
caesarsaysnumber = 3  #positive number moves alphabet numbers to the right; negative number moves alphabet numbers to the left
for letter, number in encryption.items():
	if (caesarsaysnumber < 0):
		encryption[letter] = encryption[letter] + abs(caesarsaysnumber)
		if (encryption[letter] >= 53):
			encryption[letter] = encryption[letter] - 52
	elif (caesarsaysnumber > 0):
		encryption[letter] = encryption[letter] - caesarsaysnumber
		if encryption[letter] <= 0:
			encryption[letter] = encryption[letter] + 52
print(sorted(zip(alphabet.values(), alphabet.keys()))) #alphabet dictionary sorted
print(sorted(zip(encryption.values(), encryption.keys()))) #encrypted dictionary sorted

#get original word alphabet numbers
originalwordnumbers = []
for letter in originalword:
	if letter in alphabet.keys():
		originalwordnumbers.append(alphabet[letter])
#encrypt original word matching alphabet numbers dictionary with encrypted numbers dictionary
encryptedword = []
for eachoriginalwordnumbers in originalwordnumbers:	
	for key, value in encryption.items():
		if eachoriginalwordnumbers == value:			
			encryptedword.append(key)
print(originalword) #original word
print("".join(encryptedword)) #encrypted original word

#26. Write a Python program to display formatted text (width=50) as output.
import textwrap
sampletext = '''Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java.'''
print(textwrap.fill(sampletext, width=50)) 
'''print
Python is a widely used high-level, general-
purpose, interpreted, dynamic programming
language. Its design philosophy emphasizes code
readability, and its syntax allows programmers to
express concepts in fewer lines of code than
possible in languages such as C++ or Java.
'''

#27. Write a Python program to remove existing indentation from all of the lines in a given text.
import textwrap
sampletext = '''
	Python is a widely used high-level, general-purpose, interpreted,
	dynamic programming language. Its design philosophy emphasizes
	code readability, and its syntax allows programmers to express
	concepts in fewer lines of code than possible in languages such
	as C++ or Java.
'''
text_without_Indentation = textwrap.dedent(sampletext)
print(text_without_Indentation)
''' print
Python is a widely used high-level, general-purpose, interpreted,
dynamic programming language. Its design philosophy emphasizes
code readability, and its syntax allows programmers to express
concepts in fewer lines of code than possible in languages such
as C++ or Java.
'''

#28. Write a Python program to add a prefix text to all of the lines in a string.
import textwrap
sampletext = '''
	Python is a widely used high-level, general-purpose, interpreted,
	dynamic programming language. Its design philosophy emphasizes
	code readability, and its syntax allows programmers to express
	concepts in fewer lines of code than possible in languages such
	as C++ or Java.
'''
textwithoutindention = textwrap.dedent(sampletext)
wrapped = textwrap.fill(textwithoutindention, width=50)
finalresult = textwrap.indent(wrapped, '> ')
print(finalresult)
''' print
>  Python is a widely used high-level, general-
> purpose, interpreted, dynamic programming
> language. Its design philosophy emphasizes code
> readability, and its syntax allows programmers to
> express concepts in fewer lines of code than
> possible in languages such as C++ or Java.
'''

#29. Write a Python program to set the indentation of the first line.
import textwrap
sampletext = '''
	Python is a widely used high-level, general-purpose, interpreted,
	dynamic programming language. Its design philosophy emphasizes
	code readability, and its syntax allows programmers to express
	concepts in fewer lines of code than possible in languages such
	as C++ or Java.
'''
text1 =  textwrap.dedent(sampletext).strip()
print(textwrap.fill(text1, initial_indent='', subsequent_indent=' ' * 4, width=80,))
''' print
Python is a widely used high-level, general-purpose, interpreted, dynamic
    programming language. Its design philosophy emphasizes code readability, and
    its syntax allows programmers to express concepts in fewer lines of code
    than possible in languages such as C++ or Java.
'''

#30. Write a Python program to print the following floating numbers up to 2 decimal places.
floatnumber = 5.69123456789
print("{:.2f}".format(floatnumber)) #print 5.69
floatnumber = 5.756123456789
print("{:.2f}".format(floatnumber)) #print 5.76

#31. Write a Python program to print the following floating numbers up to 2 decimal places with a sign.
def withasign(floatnumber):
	if floatnumber > 0:
		sign = "+"
	else:
		sign = ""
	print(sign+"{:.2f}".format(floatnumber))
withasign(5.69123456789) #print +5.69
withasign(-5.756123456789) #print -5.76
withasign(0) #print 0.00

#32. Write a Python program to print the following floating numbers with no decimal places
def nodecimal(floatnumber):
	floatnumber = str(floatnumber)
	solution = []
	for eachfloatnumber in floatnumber:
		if eachfloatnumber == ".":
			continue
		else:
			solution.append(eachfloatnumber)
	print("".join(map(str, solution)))
nodecimal(5.69123456789) #print 569123456789
nodecimal(5.756123456789) #print 5756123456789

#33. Write a Python program to print the following integers with zeros on the left of specified width.
def leftzeroes(number):
	numberlength = len(str(number))
	if numberlength >= 10:
		print(number)
	else:
		numberofzeros = 10 - numberlength
		print(("0"*numberofzeros)+str(number))
leftzeroes(123456) #print 0000123456
leftzeroes(123456789) #print 0123456789
leftzeroes(98765432111) #print 98765432111

#34. Write a Python program to print the following integers with zeros on the left of specified width.
def rightasterik(number):
	numberlength = len(str(number))
	if numberlength >= 10:
		print(number)
	else:
		numberofasterik = 10 - numberlength
		print(str(number)+("*"*numberofasterik))
rightasterik(123456) #print 123456****
rightasterik(123456789) #print 123456789*
rightasterik(98765432111) #print 98765432111

#35. Write a Python program to display a number with a comma separator.
print("{:,}".format(1000000)) #print 1,000,000
print("{:,}".format(123456789)) #print 123,456,789
print("{:,}".format(-987654321)) #print -987,654,321

#36. Write a Python program to format a number with a percentage.
half = 1/2
print("Percentage: {}%".format(half)) #print Percentage: 0.5%
third = 1/3
print("Percentage: {}%".format(third)) #print Percentage: 0.3333333333333333%

#37. Write a Python program to display a number in left, right and center aligned of width 10.
number = 123456
print("{:>10}" .format(str(number))) #print    123456 align right.
print("{:<10}" .format(str(number))) #print 123456    align left.
print("{:^10}" .format(str(number))) #print   123456   align center.

#38. Write a Python program to count occurrences of a substring in a string.  RM:  count the number of something in a string.
def countsomething(thestring,something):
	thestring = thestring.lower()
	something = something.lower()
	print(thestring.count(something))
countsomething("Paris in the the string","the") #return 2
countsomething("Finished files are the result of years of scientific study combined with the experience of years.","f") #return 6

#39. Write a Python program to reverse a string.
astring = "The quick brown fox jumped over the lazy dog."
print(astring[::-1]) #print .god yzal eht revo depmuj xof nworb kciuq ehT

#40. Write a Python program to reverse words in a string.
text = "We hope to one day become the world's leader in free, education resources.  We are constantly " \
"discovering and adding more free content to the website everyday.  There is already an enormous " \
"amount of resoruces online that can be accessed for free by anyone in the world, the main issue " \
"right now is that very little of it is organized or structured in any way.  We want to be the " \
"solution to that problem."
words = text.split()
print(" ".join(map(str, words[::-1]))) #print problem. that to solution the be to want We way. any in structured or organized is it of little very that is now right issue main the world, the in anyone by free for accessed be can that online resoruces of amount enormous an already is There everyday. website the to content free more adding and discovering constantly are We resources. education free, in leader world's the become day one to hope We