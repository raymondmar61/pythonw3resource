#https://www.w3resource.com/python-exercises/python-basic-exercises.php
#RM 03/22/2018 2022 create a basics.py non Python os, file programs.

#1. Write a Python program to print the following string in a specific format: Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :
"""
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
"""
print("""
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
""")

#3. Write a Python program to display the current date and time.
from datetime import datetime
print(datetime.now()) #print 2017-11-10 20:12:11.688408
currentdate = datetime.now()
print(currentdate.month) #print 11
print(currentdate.year) #print 2017
print(currentdate.day) #print 20
print(currentdate.month,"/",currentdate.day,"/",currentdate.year)
print(currentdate.strftime("%m/%d/%Y")) #print 11/20/2017

#4. Write a Python program which accepts the radius of a circle from the user and compute the area.
from math import pi
def areacircle(radius):
	return pi*(radius**2)
print(areacircle(1.1)) #print 3.8013271108436504

#5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.  RM:  skip input().
firstname = "Raymond"
lastname = "Mar"
name = firstname+" "+lastname
print(name[::-1]) #print raM dnomyaR

#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
sampledata = 3, 5, 7, 23
print(sampledata) #print (3, 5, 7, 23)
# sampledatalist = []
# for eachsampledata in sampledata:
# 	sampledatalist.append(str(eachsampledata))
# print(sampledatalist) #print ['3', '5', '7', '23']
print(tuple(map(str,sampledata))) #print ('3', '5', '7', '23')
print(list(map(str,sampledata))) #print ['3', '5', '7', '23']

#8. Write a Python program to display the first and last colors from the following list. 
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0]) #print Red
print(color_list[-1]) #print Black

#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date exam_st_date = (11, 12, 2014)  Sample Output : The examination will start from : 11 / 12 / 2014
examstartdate = (11, 12, 2014)
print(type(examstartdate)) #print <class 'tuple'>
print(type(examstartdate[0])) #print <class 'int'>
print("The examination will start from:", examstartdate[0],"/",examstartdate[1],"/",examstartdate[2]) #print The examination will start from: 11 / 12 / 2014
# printexamestartdate = datetime.strptime(examstartdate,"%m/%d/%Y")
# print(printexamestartdate) #error TypeError: strptime() argument 1 must be str, not tuple

#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Sample value of n is 5. Expected Result : 615.
n = 5
print(n+(n**2)+(n**3)) #print 155
a = 5
n1 = int( "%s" % a )
print(n1) #print 5
n2 = int( "%s%s" % (a,a) )
print(n2) #print 55
n3 = int( "%s%s%s" % (a,a,a) )
print(n3) #print 555
print(n1+n2+n3) #print 615

#12. Write a Python program to print the calendar of a given month and year.  Note: Use 'calendar' module.
import calendar
c = calendar.TextCalendar(calendar.SUNDAY) #The example configures TextCalendar to start weeks on Sunday, following the American convention. The default is to use the European convention of starting a week on Monday.
c.prmonth(2017, 11) #print the Nov 2017 calendar

#13. Write a Python program to print the following here document. Go to the editor Sample string :
"""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
print("""
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
""")

#14. Write a Python program to calculate number of days between two dates.  Sample dates : (2014, 7, 2), (2014, 7, 11)  Expected output : 9 days 
import datetime
firstdate = datetime.date(2014, 7, 2)
secondate = datetime.date(2014, 7, 11)
print((secondate - firstdate).days) #print 9

#15. Write a Python program to get the volume of a sphere with radius 6.
from math import pi
def volumesphere(radius):
	return (4/3)*pi*(radius**3)
print(volumesphere(6)) #print 904.7786842338603
	
#16. Write a Python program to get the difference between a given number and 17, if the [given] number is greater than 17 return double the absolute difference.
givennumber = 14
constant = 17
if givennumber <= constant:
	print(constant - givennumber) #print 3
else:
	print((givennumber - constant)*2)

#17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
givennumber = 999
if givennumber >=900 or givennumber <=1100:
	print(givennumber,"Given number is within 1000 +/- 100") #print 999 Given number is within 1000 +/- 100	
elif givennumber >=1900 or givennumber <=2100:
	print(givennumber,"Given number is within 2000 +/- 100")
else:
	print("Given number is not within 1000 +/100 or 2000 +/-100")

#18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
def sumthreenumbers(a, b, c):
	if a == b and b ==c:
		return(3*(a+b+c))
	else:
		return a + b + c
print(sumthreenumbers(5, 10, 15)) #print 30
print(sumthreenumbers(50, 50, 50)) #print 450

#19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
def newstring(newstring):
	if newstring[0] == "I" and newstring[1] == "s":
		print(newstring)
	else:
		print("Is"+newstring)
newstring("Isokay") #retrn Isokay
newstring("okayis") #retrn Isokayis

#20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.
n = 5
givenstring = "The quick brown fox jumped over the lazy dog"
print(givenstring*5) #print The quick brown fox jumped over the lazy dogThe quick brown fox jumped over the lazy dogThe quick brown fox jumped over the lazy dogThe quick brown fox jumped over the lazy dogThe quick brown fox jumped over the lazy dog

#21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.
def evenorodd(n):
	if n % 2 == 0:
		print(n,"is even")
	else:
		print(n,"is odd")
evenorodd(10) #return 10 is even
evenorodd(17) #return 17 is odd

#22. Write a Python program to count the number 4 in a given list.
import random
numberlist = []
count = 1
while count < 11:
	numberlist.append(random.randint(1,5))
	count +=1
print(numberlist)
count = 0
for eachnumberlist in numberlist:
	if eachnumberlist == 4:
		count += 1
print("There are",count,"four's in the list.")

#23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2
def copy2characters(string,n):
	if len(string) < 2:
		return string*n
	else:
		return (string[0]+string[1])*n
print(copy2characters("Parker Brothers",5)) #print PaPaPaPaPa
print(copy2characters("S",15)) #print SSSSSSSSSSSSSSS

#24. Write a Python program to test whether a passed letter is a vowel or not.
vowel = ["a","e","i","o","u"]
def lettercheck(letter):
	if letter in vowel:
		print(letter+" is a vowel")
	else:
		print(letter+" is a consonant")
lettercheck("e") #return e is a vowel
lettercheck("t") #return t is a consonant

#25. Write a Python program to check whether a specified value is contained in a group of values.  Test Data :  3 -> [1, 5, 8, 3] : True -1 -> [1, 5, 8, 3] : False
def valuecheck(n):
	testdata = [1, 5, 8, 3]
	if n in testdata:
		return True
	else:
		return False
print(valuecheck(3)) #print True
print(valuecheck(-1)) #print False

#26. Write a Python program to create a histogram from a given list of integers.
import matplotlib.pyplot as plt
xpopulationages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
ybins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
plt.hist(xpopulationages,ybins, label="labelhistogram", histtype="bar", rwidth=1.0)
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("Title")
plt.legend()
#plt.show() #comment out plt.show() to avoid displaying histogram

#27. Write a Python program to concatenate all elements in a list into a string and return it.
def liststring(liststring):
	print(" ".join(liststring))
	print(", ".join(liststring))
wordlist = ["Let","It","Snow","Jingle","Bells","Silver","Spirit","Christmas"]
liststring(wordlist) #print Let It Snow Jingle Bells Silver Spirit Christmas\n Let, It, Snow, Jingle, Bells, Silver, Spirit, Christmas

#28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.
def evennumber237(listnumber):
	numbersfinal = []
	for eachlistnumber in listnumber:		
		if eachlistnumber == 237:
			break
		elif eachlistnumber % 2 == 0:
			numbersfinal.append(eachlistnumber)
	print(numbersfinal)		
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 100000, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 743, 527]
evennumber237(numbers) #return [386, 462, 418, 344, 236, 566, 978, 328, 162, 758, 918, 100000]

#29. Write a Python program to print out a set containing all the colors from colorlist1 which are not present in colorlist2.
"""
Test Data : 
colorlist1 = set(["White", "Black", "Red"]) 
colorlist2 = set(["Red", "Green"])
Expected Output : {'Black', 'White'}
"""
colorlist1 = set(["White", "Black", "Red"]) 
colorlist2 = set(["Red", "Green"])
print(colorlist1.union(colorlist2)) #print {'Green', 'Red', 'White', 'Black'}
print(colorlist1.intersection(colorlist2)) #print {'Red'}
print(colorlist1.difference(colorlist2)) #print {'Black', 'White'}
print(colorlist2.difference(colorlist1)) #print {'Green'}
#source: https://www.python-course.eu/sets_frozensets.php
"""
RM:  long way
colorlist1 = list(colorlist1)
colorlist2 = list(colorlist2)
print(colorlist1) #print ['Red', 'Black', 'White']
print(colorlist2) #print ['Green', 'Red']
colorlist3 = []
for eachcolorlist1 in colorlist1:
	if eachcolorlist1 not in colorlist2:
		colorlist3.append(eachcolorlist1)
print(set(colorlist3)) #print {'Black', 'White'}
"""

#30. Write a Python program that will accept the base and height of a triangle and compute the area
def areatriangle(base, height):
	return base*height*0.5
# baseheight = input("Enter the base and height of a triangle separated by a space ")
# baseheight = baseheight.split(" ")
# print(areatriangle(float(baseheight[0]),float(baseheight[1])))
print(areatriangle(5,4.5)) #print 11.25

#31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.  RM:  function from Barry Brown
def gcd(a, b):
	"""Return the greatest common divisor of a and b.  gcd(10, 5) is 5, (14, 21) is 7, (80, 30) is 10, (7, 15) is 1, (9, 0) is 9 """
	if b == 0:
		return a
	else:
		return gcd(b, a % b) #recursion
print(gcd(20,10)) #return 10

#32.  Write a Python program to get the least common multiple (LCM) of two positive integers.  Official solution: https://www.w3resource.com/python-exercises/python-basic-exercise-32.php
def isprime(n):
	if n == 1:
		return False #1 is not a prime number
	for d in range(2, n):
		if n % d == 0:
			return False
	return True
#number1 and number2 are the two positive integers
number1 = 3000
number2 = 45550
prime1 = isprime(number1)
prime2 = isprime(number2)
#a pair of prime numbers the LCM is their product
if prime1 == True and prime2 == True:
	print(number1*number2,"is the lowest common multiple")
else:
	set1 = set()
	set2 = set()
	eachnumber = 1
	while True:
		try:
			#create two sets of number1 multiples and number2 multiples
			set1.add(eachnumber*number1)
			set2.add(eachnumber*number2)
			min(set1.intersection(set2))
		#no value for min(set1.intersection(set2)) add 1 to eachnumber and continue addting multiples to the two sets
		except ValueError:
			eachnumber +=1
			continue
		else:
			print(min(set1.intersection(set2)),"is the lowest common multiple",number1,"and",number2)
			break

#33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
def sumthreeintegers(x,y,z):
	"""Returns the sum of three different integers.  Press q to exit."""
	if x<0 or y<0 or z<0:
		positivenumbers = abs(x)+abs(y)+abs(z)
		print("I converted all numbers to positive:",positivenumbers)		
	elif (x==y) or (y==z) or (x==z):
		print(0)
	else:
		print(x+y+z)
def sumthreeintegers2(x,y,z):
	"""Returns the sum of three different integers.  Press q to exit."""
	if x<0 or y<0 or z<0:
		positivenumbers = abs(x)+abs(y)+abs(z)
		convert = "I converted all numbers to positive:",str(positivenumbers)
		return " ".join(convert)
	elif (x==y) or (y==z) or (x==z):
		return 0
	else:
		return x+y+z
#three given integers.  I modified problem to positive integers only.
x=10
y=-15
z=100
sumthreeintegers(x,y,z)
print(sumthreeintegers2(x,y,z))
#RM:  reminder help for a function.
#print(help(sumthreeintegers)) #print Help on function sumthreeintegers in module __main__: sumthreeintegers(x, y, z) Returns the sum of three different integers.  Press q to exit.

#34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
def sumtwointegers(x,y):
	if ((x+y) >=15) and ((x+y) <=20):
		return 20
	else:
		return x+y
#two given integers
print(sumtwointegers(20,12))
print(sumtwointegers(4,12))
print(sumtwointegers(12,4))
print(sumtwointegers(20,-3))

#35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
def givenintegers(a,b):
	if (a == b) or (abs(a)-abs(b)==5) or (abs(b)-abs(a)==5):
		return True
	else:
		return False
print(givenintegers(505,-500))
print(givenintegers(1000,1000))
print(givenintegers(-33,10))

#36. Write a Python program to add two objects if both objects are an integer type.
object1 = 5
object2 = 6
if isinstance(object1, int) is True and isinstance(object2, int) is True:
	print(object1 + object2)
if type(object1) is int and type(object2) is int:
	print(object1 + object2)

#37. Write a Python program to display your details like name, age, address in three different lines.
description = ["Name","Age","Address"]
yourdetails = input("Enter your first name, age, address separated by a ! ")
yourdetails = yourdetails.split("!")
n=0
for eachyourdetails in yourdetails:
	print(description[n]+": "+eachyourdetails)
	n+=1

#38. Write a Python program to solve (x + y) * (x + y).  Test Data : x = 4, y = 3 Expected Output : (4 + 3) ^ 2) = 49
def xy(x,y,power):
	print(pow((x+y),power))
xy(4,3,2)

#39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years. Test Data : amt = 10000, int = 3.5, years = 7 Expected Output : 12722.79
#RM: Compounded Annual Interest.  Interest rate applied to each year's cumulative account balance.  FV=I*((1+R)^T) or future value = principal*((1+interest rate per year)^number of years)) #https://www.investopedia.com/terms/f/futurevalue.asp
def futurevalue(principal, interestrate, years):
	return (principal*((1+interestrate)**years))
print(round(futurevalue(10000,.035,7),2))

#40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
#We use the Pythagoras Theorem to derive a formula for finding the distance between two points in 2- and 3- dimensional space.  Let P = (x1,y1) and Q = (x2,y2) be two points on the Cartesian plane.  Then from the Pythagoras Theorem we find that the distance between P and Q is PQ = (((x2-x1)**2)+((y2-y1)**2))**.5
#http://mathsfirst.massey.ac.nz/Al gebra/PythagorasTheorem/pythapp.htm
import matplotlib.pyplot as plt
from math import sqrt
def distance(x1,y1,x2,y2):
	return sqrt(((x2-x1)**2)+((y2-y1)**2))
firstpoint = input("Enter x and y for first point separated by a space ")
secondpoint = input("Enter x and y for second point separated by a space ")
firstpoint = firstpoint.split(" ")
secondpoint = secondpoint.split(" ")
x1=float(firstpoint[0])
y1=float(firstpoint[1])
x2=float(secondpoint[0])
y2=float(secondpoint[1])
p=[x1,y1]
q=[x2,y2]
plt.plot(p,q, label="firstlineforlegend")
plt.xlabel("xlabel")
plt.ylabel("ylabel")
plt.title("title\ntitlenewline")
plt.legend()
plt.show()
print(distance(x1,y1,x2,y2))

#48. Write a Python program to parse a string to Float or Integer.
word = "255"
print(int(word)) #print 255
print(float(word)) #print 255.0

#50. Write a Python program to print without newline or space.
wordlist = "abcdef"
for eachwordlist in wordlist:
	print(eachwordlist, end="") #print abcdef in one line
print("\n")

#57. Write a program to get execution time for a Python method.
import time
print(time.time()) #prints number of seconds since Jan 1, 1970
startime = time.time() #prints number of seconds since Jan 1, 1970
#python code
endtime = time.time()
print((endtime-startime),"seconds")
print((round(endtime-startime)),"seconds")

import time
startime = time.clock()
#python code
endtime = time.clock()
print((endtime-startime),"seconds")
print((round(endtime-startime)),"seconds")

import time
startime = time.time()
#python code
endtime = time.time()
timetaken = endtime - startime # time_taken is in seconds
hours, rest = divmod(timetaken,3600)
minutes, seconds = divmod(rest, 60)
print(timetaken)
print(hours, rest, minutes, seconds)

#58. Write a python program to sum of the first n positive integers.
n = 100
sumn = 0
for eachnumber in range(1,n+1):
	sumn = sumn + eachnumber
print(sumn)

#59. Write a Python program to convert height (in feet and inches) to centimeters.
height = input("Enter height in feet and inches separate feet and inches with a space.  I convert to centimeters. ")
heightsplit = height.split()
print(int(heightsplit[0])*30.48+(int(heightsplit[1])*2.54))

#60. Write a Python program to calculate the hypotenuse of a right angled triangle.
legs = input("Enter the two legs of the right triangle separate the two lengths with a space.  I calculate the hypotenuse. ")
legssplit = legs.split()
print(legssplit)
print(int(legssplit[0])**2+(int(legssplit[1])**2))

#61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.
import math
feettomiles = 0.0001894
feettoinches = 12
feettoyards = 0.333
milestoinches = 63360
milestofeet = 5280.0
distancefeet = float(input("Enter the distance in feet "))
print(distancefeet*feettoyards,"yards")
print(distancefeet*feettoinches,"inches")
print(distancefeet*feettomiles,"miles")

#Bonus answer.  Convert decimal miles to feet.
miles = distancefeet * feettomiles
math.modf(miles)
print(math.modf(miles))
decimalmiles, integermiles = math.modf(miles)
print(integermiles,"miles")
if 0 < decimalmiles < 1.0000:	
	print(round(decimalmiles*milestofeet,4),"feet")
else:
	pass
#Another way separate math.modf() tuple
# modftuple = math.modf(miles)
# print(modftuple[0])
# print(modftuple[1])

#62. Write a Python program to convert all units of time into seconds.
inputtime = input("Enter the hours and minutes separated by a space ")
inputtimelist = inputtime.split()
print(int(inputtimelist[0])*60*60+int(inputtimelist[1])*60,"seconds")

#65. Write a Python program to convert seconds to day, hour, minutes and seconds.  RM:  used sample solution
time = float(input("Input time in seconds: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))

#66. Write a Python program to calculate body mass index.
weight = int(input("Enter weight in pounds "))
height = input("Enter height in feet and inches separated by a space ")
height = height.split(" ")
height = (int(height[0])*12)+(int(height[1]))
bodymassindex = (weight/height**2)*703
print("Your body mass index is",round(bodymassindex,2))

#67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

#68. Write a Python program to calculate the sum of the digits in an integer.
integerinput = 123456789
integerinputsum = 0
for eachintegerinput in str(integerinput):
	integerinputsum = integerinputsum + int(eachintegerinput)
print(integerinputsum)

#69. Write a Python program to sort three integers without using conditional statements and loops.
threeintegers = input("Enter three integers separated by a space ")
threeintegers = threeintegers.split(" ")
threeintegers = list(map(int,threeintegers)) #convert list string to list integers
threeintegers.sort()
print(str(threeintegers).strip("[]")) #extract integers out of list to string with commas

#72. Write a Python program to get the details of math module.
import math
print(dir(math))

#73. Write a Python program to calculate midpoints of a line.
def midpoint(x1,y1,x2,y2):
	answer = (round(((x1+x2)/2),2),round(((y1+y2)/2),2))
	print(answer)
firstpoint = input("Enter x and y for first point separated by a space ")
secondpoint = input("Enter x and y for second point separated by a space ")
firstpoint = firstpoint.split(" ")
secondpoint = secondpoint.split(" ")
x1=float(firstpoint[0])
y1=float(firstpoint[1])
x2=float(secondpoint[0])
y2=float(secondpoint[1])
midpoint(x1,y1,x2,y2)

#74. Write a Python program to hash a word. 
#first python code is sample solution
soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
print(len(soundex))
word=input("Input the word be hashed: ") 
word=word.upper() 
coded=word[0] 
for a in word[1:len(word)]:
    i=65-ord(a)
    coded=coded+str(soundex[i])
print("The coded word is: "+coded)
#Source: https://www.pythoncentral.io/hashing-strings-with-python/
import hashlib
print(hashlib.algorithms_available)
print(hashlib.algorithms_guaranteed)
hash_object = hashlib.sha1(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig) #print 0a4d55a8d778e5022fab701977c5d840bbc486d0
hash_object = hashlib.sha224(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig) #print c4890faffdb0105d991a461e668e276685401b02eab1ef4372795047

#78. Write a Python program to find the available built-in modules.
#RM:  used sample solution.
import sys
print(sys.builtin_module_names) #print ('_ast', '_bisect', '_codecs', '_collections', '_datetime', '_elementtree', '_functools', '_heapq', '_imp', '_io', '_locale', '_md5', '_operator', '_pickle', '_posixsubprocess', '_random', '_sha1', '_sha256', '_sha512', '_signal', '_socket', '_sre', '_stat', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', 'array', 'atexit', 'binascii', 'builtins', 'errno', 'faulthandler', 'fcntl', 'gc', 'grp', 'itertools', 'marshal', 'math', 'posix', 'pwd', 'pyexpat', 'select', 'spwd', 'sys', 'syslog', 'time', 'unicodedata', 'xxsubtype', 'zipimport', 'zlib')
import math
print(dir(math))
import select
print(dir(select))
import pwd
print(dir(pwd))

#81. Write a Python program to concatenate N strings.
def liststring(liststring):
	print(" ".join(liststring))	
userinput = ""
stringconcatenate = []
while userinput != "q":
	userinput = str(input("Enter a string to concatenate.  Type q to quit. "))
	if userinput == "q":
		break
	stringconcatenate.append(userinput)
	liststring(stringconcatenate)

#82. Write a Python program to calculate the sum over a container.
import random
numberslist = []
count = random.randint(1,101)
for i in range(1,count):
	addnumber = random.randint(1,101)
	numberslist.append(addnumber)
print(numberslist)
print(sum(numberslist))

#83. Write a Python program to test if a certain number is greater than all numbers of a list.
import random
def greaterallinlist(testcertainnumber):
	#create number list
	numberslist = []
	count = random.randint(5,11)
	for i in range(1,count):
		addnumber = random.randint(1,51)
		numberslist.append(addnumber)
	numberslist.sort()
	print(numberslist)
	#check testcertainnumber greater than all numbers in number list
	for j in range(len(numberslist)-1,-1,-1):
		print(numberslist[j])
		if testcertainnumber > numberslist[j]:
			print("testcertainnumber "+str(testcertainnumber)+" is greater than all numbers in list")
			break
		else:
			print("testcertainnumber "+str(testcertainnumber)+" is not greater than all numbers in list")
			break
greaterallinlist(40)

#84. Write a Python program to count the number occurrence of a specific character in a string.
stringinput = "The quick brown fox jumped over the lazy dog"
characterinput = "e"
counter = 0
for eachstringinput in stringinput:
	if eachstringinput == characterinput:
		counter += 1
print(counter) #print 4 RM:  yes there are four e's

#86. Write a Python program to get the ASCII value of a character.
character = "A"
print(ord(character)) #print 65
asciinumber = 65
print(chr(asciinumber)) #print A
character = "@"
print(ord(character)) #print 65
asciinumber = 64
print(chr(asciinumber)) #print @

#88. Given variables x=30 and y=20, write a Python program to print t "30+20=50".
x = 30
y = 20
print("%s+%s=50"%(x,y)) #print 30+20=50

#89. Write a Python program to perform an action if a condition is true. Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
variablename = 1
if variablename == 1:
	print("First day of a Month!")
else:
	pass

#91. Write a Python program to swap two variables.
variable1 = "abc"
variable2 = "def"
print(variable1) #print abc
print(variable2) #print def
variable3 = variable2
variable2 = variable1
variable1 = variable3
print(variable1) #print def
print(variable2) #print abc

#92. Write a Python program to define a string containing special characters in various forms.  RM:  copied solution.  I didn't understand the question.
print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')

#95. Write a Python program to check if a string is numeric.
stringcheck = 55
print(type(stringcheck))
if type(stringcheck) is str:
	print("String is string")
elif type(stringcheck) is int:
	print("String is integer")
else:
	print("String is something else.  Float?")

#solution
#stringcheck2 = 55
stringcheck2 = "a55"
try:
	i = float(stringcheck2)
except (ValueError, TypeError):
	print("Not a number")

#98. Write a Python program to get the system time.
import datetime
print(datetime.datetime.now().time()) #print 19:55:29.995253
print(datetime.datetime.today()) #print 2018-03-02 19:55:29.995320

#109. Write a Python program to check if a number is positive, negative or zero.
def check(n):
	if n == 0:
		print("zero")
	elif n > 0:
		print("positive")
	else:
		print("negative")
check(0) #print zero
check(0.000001) #print positive
check(-0.000001) #print negative

#110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.
listnumbers = [15,30,100,151,5000,4500,79,81,697,1236879]
list15 = []
def divisible15(n):
	for eachn in n:
		if eachn % 15 == 0:
			list15.append(eachn)
divisible15(listnumbers)
print(list15) #print [15, 30, 4500]

#112. Write a Python program to remove the first item from a specified list.
thelist = ["apple","orange","grape","tangerine"]
thelist.pop(0)
print(thelist)

#113. Write a Python program to input a number, if it is not a number generate an error message.
#RM:  solution is integers
#Source: https://www.tutorialspoint.com/python/python_strings.htm
pretenduserinput = "5000000"
if pretenduserinput.isdigit() == True:
	print("It's a number")

try:
	#userinput = int(input("Enter a number "))
	userinput = int("a$")
except ValueError:
	print("You didn't enter a number")
else:
	print(userinput,"is a number")

#114. Write a Python program to filter the positive numbers from a list.
wantpositivenumbers = [-987,-963,992,545,82,-556,649,-342,402,-606,-762,-59,-401,-297]
gotpositivenumbers = []
for eachwantpositivenumbers in wantpositivenumbers:
	if eachwantpositivenumbers > 0:
		gotpositivenumbers.append(eachwantpositivenumbers)
print(gotpositivenumbers) #print [992, 545, 82, 649, 402]
print(list(map(lambda x: x>0,wantpositivenumbers))) #print [False, False, True, True, True, False, True, False, True, False, False, False, False, False]
print(list(filter(lambda x: x>0,wantpositivenumbers))) #print [992, 545, 82, 649, 402]

#115. Write a Python program to compute the product of a list of integers (without using for loop).
from functools import reduce
productlist = [9,6,10,5,10,4,1,8,1,6,1,8,2,1]
print(reduce(lambda x,y: x*y,productlist)) #print 82944000
#import numpy as np
#print(np.prod(np.array(productlist))) #takes longer

#118. Write a Python program to create a bytearray from a list.  RM:  I don'tunderstand.  Copied solution.
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)

#119. Write a Python program to display a floating number in specified numbers.
floatingnumber = 1123.5678
specifieddigits = 2
print(round(floatingnumber,specifieddigits)) #print 1123.57
print("{0:.2f}".format(floatingnumber)) #print 1123.57
stringfloatingnumber = str(floatingnumber)
decimalindex = stringfloatingnumber.find(".")
print(stringfloatingnumber[0:decimalindex+specifieddigits+1]) #print 1123.56

#120. Write a Python program to format a specified string to limit the number of characters to 6.
formatstring = "the quickbrown fox jumped over the lazy dog"
print(formatstring[0:6]) #print the qu

#121. Write a Python program to determine if variable is defined or not.
#error message below SyntaxError: invalid syntax
# try:
# 	definedvariable = ""
# except SyntaxError:
# 	print("definedvariable is not defined")
# else:
# 	print(definedvariable)
#RM:  solution
try:
	definedvariable
except NameError:
	print("definedvariable is not defined") #print the except
else:
	print("definedvariable is defined"+definedvariable)

#122. Write a Python program to empty a variable without destroying it.  RM:  copied solution
n = 20
d = {"x":200}
l = [1,3,5]
t= (5,7,8)
print(type(n)()) #print 0
print(type(d)()) #print {}
print(type(l)()) #print []
print(type(t)()) #print ()

#123. Write a Python program to determine the largest and smallest integers, longs, floats.  RM:  Python 3x use integers for longs.
def maxmin(inputlist):
	print(max(inputlist))
	print(min(inputlist))
integerslist = [1,2,3,4,5,6,7,8,9,10]
maxmin(integerslist) #return 10\n 1
floatslist = [1.2,5.5,6.7,6.9,5.75]
maxmin(floatslist) #return 6.9\n 1.2

#124. Write a Python program to check if multiple variables have the same value.
x=1
y=1
z=1
if x==y==z:
	print("x y z multiple variables have the same value.")

#125. Write a Python program to sum of all counts in a collections?  RM:  What are collections?  Answer is a module import collections.  https://pymotw.com/3/collections/counter.html  I used collections for Project Euler #39 Integer Right Triangles
import collections
numberlist = [2,2,4,6,6,8,6,10,4]
print(sum(numberlist)) #print 48
print(collections.Counter(numberlist)) #print Counter({6: 3, 2: 2, 4: 2, 8: 1, 10: 1})
print(sum(collections.Counter(numberlist).values())) #print 9.   9 is correct.  We want the sum of the counts, not sum of the numbers in numberlist.

#126. Write a Python program to get the actual module object for a given object.  RM:  copied solution
from inspect import getmodule
from math import sqrt
print(getmodule(sqrt)) #print <module 'math' (built-in)>

#127. Write a Python program to check if an integer fits in 64 bits.  RM:  copied solution
int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length()) #print 64
    print((2 ** 63).bit_length()) #print 64

#128. Write a Python program to check if lowercase letters exist in a string.
astring = "THE QUICK BROWN FOX JUMPEd OVeR THE LAZY DOG"
for eachastring in astring:
	if eachastring == " ":
		continue
	lowercase = eachastring.lower()
	if eachastring == lowercase:
		print("There is a lowercase letter "+eachastring) #print There is a lowercase letter d\n There is a lowercase letter e

#129. Write a Python program to add leading zeroes to a string.
astring = "THE QUICK BROWN FOX JUMPEd OVeR THE LAZY DOG"
azero = "0"
numberofzeros = 5
print((azero*numberofzeros)+astring) #print 00000THE QUICK BROWN FOX JUMPEd OVeR THE LAZY DOG

#130. Write a Python program to use double quotes to display strings.
astring = "THE QUICK BROWN FOX JUMPEd OVeR THE LAZY DOG"
doublequotes = "\""
print(doublequotes+astring+doublequotes) #print "THE QUICK BROWN FOX JUMPEd OVeR THE LAZY DOG"

#131. Write a Python program to split a variable length string into variables.  RM:  https://stackoverflow.com/questions/19300174/python-assign-each-element-of-a-list-to-a-separate-variable says not a good idea.  In other words, don't create dynamic variables.  Another opinion https://stackoverflow.com/questions/20688324/python-assign-values-to-list-elements-in-loop
var_list = ['a', 'b', 'c']
x, y, z = (var_list + [None] * 3)[:3]
print(x, y, z) #print a b c
print(x) #print a
print(y) #print b
print(z) #print c
var_list2 = [100, 20.25]
x, y = (var_list2 + [None] * 2)[:2]
print(x, y) #print 100 20.25
print(x) #print 100
print(y) #print 20.25

#133. Write a Python program to calculate the time runs (difference between start and current time) of a program.
import time
startime = time.time()
endtime = time.time()
print((endtime-startime),"seconds")
print((round(endtime-startime)),"seconds")
#also
from timeit import default_timer
start = default_timer()
print(default_timer()-start)
print(round(default_timer()-start),"seconds")

#134. Write a Python program to input two integers in a single line.
twointegers = input("Enter two integers ")
print(twointegers,end="")
#RM: official solution doesn't work on 3.5; however, user input correct
x, y = [int(x) for x in input("numbers: ").split()]
print("The value of x & y are: ",x,y)

#135. Write a Python program to print a variable without spaces between values. Sample value: x=30 Expected output: Value of x is "30"
x=30
print("Value of x is \""+str(x)+"\"") #print Value of x is "30"
print("Value of x is ""\""+str(x)+"\"") #print Value of x is "30"
#RM:  Official solution
x = 30
print('Value of x is "{}"'.format(x))

#137. Write a Python program to extract single key-value pair of a dictionary in variables.
stocks = {"GOOG": 434,"AAPL": 325,"FB": 54,"AMZN": 623,"F": 32,"MSFT": 549,}
for key, value in stocks.items():
	print(key, value) #print AMZN 623\n FB 54\n GOOG 434\n MSFT 549\n AAPL 325\n F 32

#138. Write a Python program to convert true to 1 and false to 0.
#RM:  Official solution
numbertrue = True
numberfalse = False
print(int(numbertrue))
print(int(numberfalse))

#140. Write a Python program to convert an integer to binary keep leading zeros.  Sample data : 50.  Expected output : 00001100, 0000001100
integerconvert = 50
print(bin(integerconvert)) #print 0b110011
print("{0:b}".format(integerconvert)) #print 110010
print("{0:010b}".format(integerconvert)) #print 0000110010
print("{0:012b}".format(integerconvert)) #print 000000110010

#141. Write a python program to convert decimal to hexadecimal. Go to the editor Sample decimal number: 30, 4.  Expected output: 1e, 04.
print(hex(30)) #print 0x1e
print("{0:x}".format(30)) #print 1e
print(hex(4)) #print 0x4
print("{0:x}".format(4)) #print 4
print(hex(15)) #print 0xf
print("{0:x}".format(15)) #print f

#144. Write a Python program to check if variable is of integer or string.
stringvariable = "paper"
print(type(stringvariable)) #print class 'str'>
integervariable = 55
print(type(integervariable)) #print class 'int'>

#147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.
def quotientzero(dividend, divisor):
	if dividend % divisor == 0:
		print(dividend,"is divisible by",divisor)
	else:
		print(dividend,"is not divisible by",str(divisor)+".  The quotent is %.2f." % (dividend/divisor))
division = input("Enter the dividend and the divisor separated by a space.  Dividend is the number to be divided.  Divisor is the number by.  e.g. 20/5 20 is the dividend and 5 is the divisor to get the quotient 4.  ")
divisionnumbers = division.split()
quotientzero(int(divisionnumbers[0]),int(divisionnumbers[1]))

#148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers. Note: Do not use built-in functions.
inputsequence = input("Enter integers separated by a space ")
inputsequencelist = inputsequence.split()
resultsinteger = list(map(int,inputsequencelist))
print(resultsinteger)
maximum = 0
minimum = 0
for eachnumber in resultsinteger:
	if eachnumber > 0:
		maximum = eachnumber
	if eachnumber < 0:
		minimum = eachnumber
print(maximum)
print(minimum)

#149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number.
def sumcube(positiveinteger):
	sumcube = 0
	for eachnumber in range(1,positiveinteger):	
		sumcube = sumcube + pow(eachnumber,3)
	print(sumcube)
sumcube(12)

#150. Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values.
from random import randint
from itertools import combinations
start = randint(1,50)
sequencelength = randint(5,25)
sequencelist = list(range(start,start+sequencelength))
print(sequencelist)
for combopairs in combinations(sequencelist, 2):
	if combopairs[0]*combopairs[1] % 2 != 0:
		print((combopairs[0]*combopairs[1]),(combopairs))