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