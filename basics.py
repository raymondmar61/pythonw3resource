#https://www.w3resource.com/python-exercises/python-basic-exercises.php

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

#2. Write a Python program to get the Python version you are using
import sys
print(sys.version) #print 3.5.2 (default, Nov 17 2016, 17:05:23)\n [GCC 5.4.0 20160609]
print(sys.maxsize) #print 9223372036854775807

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

#7. Write a Python program to accept a filename from the user and print the extension of that.  RM:  skipped accept a filename from the user
import os
filename, fileextension = os.path.splitext("/home/mar/Python/socratica/googlestockdata.csv")
print(filename) #print /home/mar/Python/socratica/googlestockdata
print(fileextension) #print .csv

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

#11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).  RM:  comment out print statements for #11
#print(abs.__doc__)
#print(print.__doc__)
#print(type.__doc__)
#print(dir(__builtins__)) #['ArithmeticError', 'AssertionError', ...,  'type', 'vars', 'zip']
#RM:  https://docs.python.org/3/library/functions.html website has all built-in functions

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

#41. Write a Python program to check whether a file exists.
filename = "temptestmatplotlib.py"
with open(filename) as fileobject:
	reviewopenfile=fileobject.read()
print(reviewopenfile)
filename = "temptestmatplotlib2.py"
try:
	with open(filename) as fileobject:
		contents=fileobject.read()
except FileNotFoundError:
	print(filename+" file doesn't exist.")
else:
	print(contents)

#42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
import ctypes
print(ctypes.sizeof(ctypes.c_voidp)) #print 8.  4 for 32bit or 8 for 64bit
import platform
print(platform.architecture()) #print ('64bit', 'ELF')

#43. Write a Python program to get OS name, platform and release information.
import os
print(os.name) #print posix
import platform
print(platform.system()) #print Linux
print(platform.release()) #print 4.4.0-89-generic

#44. Write a Python program to locate Python site-packages.  site-packages is the location where Python installs its modules.
import sys
print([f for f in sys.path if f.endswith('packages')]) #print ['/home/mar/.local/lib/python3.5/site-packages', '/usr/local/lib/python3.5/dist-packages', '/usr/lib/python3/dist-packages']

#45. Write a python program to call an external command in Python.
#RM:  skip for now.

#46. Write a python program to get the path and name of the file that is currently executing.  RM:  also folder name or directory name. 
import os
print(os.path.basename(__file__)) #print pythonexercises.py
print(os.path.realpath(__file__)) #print /home/mar/Python/w3resource/pythonexercises.py
print(os.path.dirname(os.path.realpath(__file__))) #print /home/mar/Python/w3resource
foldername = os.path.realpath(__file__)
print(os.path.dirname(foldername)) #print /home/mar/Python/w3resource
import sys
print(sys.argv[0]) #print pythonexercises.py
print(sys.argv) #print ['pythonexercises.py']

#47. Write a Python program to find out the number of CPUs using.
import multiprocessing
print(multiprocessing.cpu_count()) #print 2

#48. Write a Python program to parse a string to Float or Integer.
word = 255
print(int(word)) #print 255
print(float(word)) #print 255.0

#49. Write a Python program to list all files in a directory in Python. 
import os
for root, dirs, files in os.walk("."):
    for filename in files:
        print(filename) #prints all file names its extension

#50. Write a Python program to print without newline or space.
wordlist = "abcdef"
for eachwordlist in wordlist:
	print(eachwordlist, end="") #print abcdef in one line
print("\n")

#51. Write a Python program to determine profiling of Python programs. Go to the editor  Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.

#52. Write a Python program to print to stderr.

#53. Write a python program to access environment variables.
import os
print(os.environ)

#54. Write a Python program to get the current username
import getpass
username = getpass.getuser()
print(username)

#55. Write a Python to find local IP addresses using Python's stdlib

#56. Write a Python program to get height and width of the console window.
import os
ts = os.get_terminal_size()
print(ts.lines)
print(ts.columns)

#57. Write a program to get execution time for a Python method.
import time
print(time.time()) #prints number of seconds since Jan 1, 1970
startime = time.time() #prints number of seconds since Jan 1, 1970
#python
endtime = time.time()
print((endtime-startime),"seconds")
print((round(endtime-startime)),"seconds")

import time
startime = time.clock()
#python
endtime = time.clock()
print((endtime-startime),"seconds")
print((round(endtime-startime)),"seconds")

import time
startime = time.time()
#python
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

#63. Write a Python program to get an absolute file path.
import os
print(os.path.abspath(__file__))

#64. Write a Python program to get file creation and modification date/times.
import os, time
print(os.stat(__file__))
print(os.path.getctime(__file__))
print(os.path.getmtime(__file__))
print(time.ctime(os.path.getctime(__file__))+" creation date")
print(time.ctime(os.path.getmtime(__file__))+" modified date")
print("Can't get creation date in Linux FYI.")

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

#70. Write a Python program to sort files by date.  RM:  used sample solution
import glob
import os
files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))
#RM:  First time I saw glob module

#71. Write a Python program to get a directory listing, sorted by creation date.  RM:  used sample solution
from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
#Relative or absolute path to the directory
dir_path = sys.argv[1] if len(sys.argv) == 2 else r'.'
#all entries in the directory w/ stats
data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
data = ((os.stat(path), path) for path in data)
#regular files, insert creation date
data = ((stat[ST_CTIME], path)
           for stat, path in data if S_ISREG(stat[ST_MODE]))
for cdate, path in sorted(data):
    print(time.ctime(cdate), os.path.basename(path))

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

#75. Write a Python program to get the copyright information.
#RM:  used sample solution. i.e. print the Python Copyrights
import sys
print("Python Copyright Information")
print(sys.copyright)

#76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script.
#RM:  used sample solution.
import sys
print("This is the name/path of the script:"),sys.argv[0]
print("Number of arguments:",len(sys.argv))
print("Argument List:",str(sys.argv))

#77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.
#RM:  used sample solution.
import sys
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")

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

#79. Write a Python program to get the size of an object in bytes.
import sys
x = 2
print(sys.getsizeof(x)) #print 28
print(sys.getsizeof("this also")) #print 58

#80. Write a Python program to get the current value of the recursion limit.
#RM:  used sample solution.
import sys
print("Current value of the recursion limit:")
print(sys.getrecursionlimit())

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

#85. Write a Python program to check if a file path is a file or a directory.
#RM copied solution
import os  
path="abc.txt" #print It is a special file (socket, FIFO, device file)
#path = "pythonexercises.py" #print It is a normal file
#path = "/home/mar/Python/w3resource" #print It is a directory
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
print()

#86. Write a Python program to get the ASCII value of a character.
character = "A"
print(ord(character)) #print 65
asciinumber = 65
print(chr(asciinumber)) #print A
character = "@"
print(ord(character)) #print 65
asciinumber = 64
print(chr(asciinumber)) #print @

#87. Write a Python program to get the size of a file (or file size filesize)
'''
1 Byte = 8 Bit
1 Kilobyte = 1,024 Bytes
1 Megabyte = 1,048,576 Bytes
1 Gigabyte = 1,073,741,824 Bytes
1 Terabyte = 1,099,511,627,776 Bytes
'''
import os
statinfo = os.stat("pythonexercises.py")
print(statinfo) #print os.stat_result(st_mode=33204, st_ino=524627, st_dev=2049, st_nlink=1, st_uid=1000, st_gid=1000, st_size=739, st_atime=1519783679, st_mtime=1519783678, st_ctime=1519783678)
print(statinfo.st_size) #print 739
print(statinfo.st_size/1048576,"mb")
print(statinfo.st_size/1073741824,"gb")
print(statinfo.st_size/1099511627776,"tb")

from pathlib import Path
file = Path() / 'pythonexercises.py'  # or Path('./doc.txt')
size = file.stat().st_size
print(size) #print 739

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

#90. Write a Python program to create a copy of its own source code.
#RM:  copied solution.  WTH?!?
print((lambda str='print(lambda str=%r: (str %% str))()': (str % str))()) #print print(lambda str='print(lambda str=%r: (str %% str))()': (str % str))()

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

#93. Write a Python program to get the identity of an object.
#RM:  copied solution
obj1 = object()
obj1_address = id(obj1)
print(obj1_address) #print 140671348023456

#94. Write a Python program to convert a byte string to a list of integers.
import sys
xstring = "abcdefghijklmnopqrstuvwyz"
bytestring = sys.getsizeof(xstring)
print(bytestring) #print 74
bytestring = str(bytestring)
listintegers = []
for eachbytestring in bytestring:
	listintegers.append(eachbytestring)
listintegers = list(map(int,listintegers))
print(listintegers) #print [7,4]

#bonus random generator string
from random import randint, choice
numberstrings = randint(1,101)
xstring = []
counter = 1
while counter < numberstrings:
	asciinumber = choice([randint(65,90),randint(97,122)])
	xstring.append(chr(asciinumber))
	counter += 1
print("".join(map(str,xstring)))
bytestring = sys.getsizeof(xstring)
print(bytestring)
bytestring = str(bytestring)
listintegers = []
for eachbytestring in bytestring:
	listintegers.append(eachbytestring)
listintegers = list(map(int,listintegers))
print(listintegers)

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

#96. Write a Python program to print the current call stack.
#source: https://stackoverflow.com/questions/1156023/print-current-call-stack-from-a-method-in-python-code
import traceback
def f():
    g()
def g():
    for line in traceback.format_stack():
        print(line.strip())
f()
#solution
import traceback
def f1():return abc()
def abc():traceback.print_stack()
f1()
#RM:  what's current call stack?

#97. Write a Python program to list the special variables used within the language.  
#Python comes with a number of special variables and methods whose name is preceeded and followed by __.
#RM:  copied solution
s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )

#98. Write a Python program to get the system time.
import datetime
print(datetime.datetime.now().time()) #print 19:55:29.995253
print(datetime.datetime.today()) #print 2018-03-02 19:55:29.995320

#99. Write a Python program to clear the screen or terminal.
import os
#os.system('cls')  # For Windows
os.system('clear')  # For Linux/OS X

#100. Write a Python program to get the name of the host on which the routine is running.
import socket
print(socket.gethostname()) #print mar-VirtualBox
import os
myhost = os.uname()[1]
print(myhost) #print mar-VirtualBox

#101. Write a Python program to access and print a URL's content to the console.
import urllib.request
contents = urllib.request.urlopen("http://www.google.com").read()
print(contents)
print("\n")

#solution
from http.client import HTTPConnection
conn = HTTPConnection("www.google.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)

#102. Write a Python program to get system command output.
#RM:  copied solution
import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)
#RM:  printed all the files in present directory

#103. Write a Python program to extract the filename from a given path.
#solution
import os
print(os.path.basename("/home/mar/Python/w3resource/basics.py")) #print basics.py

#better because it prints all files in a list from present directory
from os import walk
filenameslist = []
for (dirpath, dirnames, filenames) in walk("/home/mar/Python/w3resource"):
    filenameslist.extend(filenames)   
    break
print(filenameslist)

#104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process. Note: Availability: Unix.

