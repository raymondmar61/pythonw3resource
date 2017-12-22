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