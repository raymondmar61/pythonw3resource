#https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

#1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
numbers = []
for n in range(1500,2701):	
	if (n % 7 == 0) and (n % 5 == 0):
		numbers.append(n)
print(numbers) #print [1505, 1540, 1575, 1610, 1645, 1680, 1715, 1750, 1785, 1820, 1855, 1890, 1925, 1960, 1995, 2030, 2065, 2100, 2135, 2170, 2205, 2240, 2275, 2310, 2345, 2380, 2415, 2450, 2485, 2520, 2555, 2590, 2625, 2660, 2695]
#also
answer = [n for n in range(1500,2701) if (n % 7 == 0) and (n % 5 == 0)]
print(str(answer).strip("[]")) #print 1505, 1540, 1575, 1610, 1645, 1680, 1715, 1750, 1785, 1820, 1855, 1890, 1925, 1960, 1995, 2030, 2065, 2100, 2135, 2170, 2205, 2240, 2275, 2310, 2345, 2380, 2415, 2450, 2485, 2520, 2555, 2590, 2625, 2660, 2695
#print(", ".join(answer)) #error message because answer contains integers

#2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
#c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit
temperatureinput = input("Enter temperature followed by a space to determine Celsius 'c' or Fahrenheit 'f'")
temperature = temperatureinput.split(" ")
degrees = int(temperature[0])
measure = temperature[1]
tofahrenheit = degrees*(9/5)+32
tocelsius = (degrees-32)*(5/9)
if measure == "c":
	print("{} Celsius, {} Fahrenheit.".format(degrees,tofahrenheit))
elif measure == "f":
	print("{} Fahrenheit, {} Celsius.".format(degrees,tocelsius))
else:
	print("If you want Celsius to Fahrenheit, then {} Celsius, {} Fahrenheit.".format(measure,tofahrenheit))
	print("If you want Fahrenheit to Celsius, then {} Fahrenheit, {} Celsius.".format(measure,tocelsius))
#official solution
temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temp[:-1])
i_convention = temp[-1]
if i_convention.upper() == "C":
	result = int(round((9 * degree) / 5 + 32))
	o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
	result = int(round((degree - 32) * 5 / 9))
	o_convention = "Celsius"
else:
	print("Input proper convention.")
	quit()
print("The temperature in", o_convention, "is", result, "degrees.")

#3. Write a Python program to guess a number between 1 to 9.  Note: User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
from random import randint
computerguess = randint(1,9)
print("cheat",computerguess)
userguess = ""
while userguess != computerguess:
	userguess = int(input("Guess my number between 1 and 9 "))
	if userguess == computerguess:
		print(userguess,"Well gussed!")
		break
	elif userguess < computerguess:
		print(userguess,"is too low.")
	elif userguess > computerguess:
		print(userguess,"is too high.")
	else:
		print("Error.  Exit now.")
		break

#4. Write a Python program to construct the following pattern, using a nested for loop.
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
for n in range(1,11):
	if n < 6:
		print(n*"* ")
	else:
		for x in range(4,0,-1):
			print(x*"* ")
	break
#official solution
n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

#5. Write a Python program that accepts a word from the user and reverse it.
inputstring = input("Enter a word.  I reverse it. ")
print(inputstring) #print operation
print(inputstring[::-1]) #print noitarepo
#official solution
word = input("Input a word to reverse: ")
for char in range(len(word)-1,-1,-1):
	print(word[char], end="")

#6. Write a Python program to count the number of even and odd numbers from a series of numbers.  Sample numbers: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9).  Expected Output: Number of even numbers: 5.  Number of odd numbers: 4.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
evennumberscounter = 0
oddnumberscounter = 0
for eachnumbers in numbers:
    if eachnumbers % 2 == 0:
        evennumberscounter += 1
    elif eachnumbers % 2 != 0:
        oddnumberscounter += 1
    else:
        print("Warning!  There is an error.")
print("Number of even numbers:",evennumberscounter) #print Number of even numbers: 5
print("Number of odd numbers:",oddnumberscounter) #print Number of odd numbers: 4

#7. Write a Python program that prints each item and its corresponding type from the following list.  Sample List: datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for eachdatalist in datalist:
    print(eachdatalist,"is",type(eachdatalist))
"""1452 is <class 'int'>
11.23 is <class 'float'>
(1+2j) is <class 'complex'>
True is <class 'bool'>
w3resource is <class 'str'>
(0, -1) is <class 'tuple'>
[5, 12] is <class 'list'>
{'class': 'V', 'section': 'A'} is <class 'dict'>
"""

#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.  Note: Use 'continue' statement.   Expected Output: 0 1 2 4 5 
numberslist = list(range(0,7))
output = []
for eachnumberslist in numberslist:
    if eachnumberslist == 0:
        output.append(eachnumberslist)        
    elif eachnumberslist % 3 == 0:
        continue
    else:
        output.append(eachnumberslist)
print(" ".join(map(str, output))) #print 0 1 2 4 5

#9. Write a Python program to get the Fibonacci series between 0 to 50.   Note: The Fibonacci Sequence is the series of numbers:  0, 1, 1, 2, 3, 5, 8, 13, 21, ....   Every next number is found by adding up the two numbers before it.  Expected Output : 1 1 2 3 5 8 13 21 34
x,y=0,1
while y<50:
    print(y)
    x,y = y,x+y

#10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for n in range(1,51):
	if (n % 3 == 0 and n % 5 == 0):
		print("fizzbuzz")
	elif n % 5 == 0:
		print("buzz")
	elif n % 3 == 0:
		print("fizz")
	else:
		print(n)

#11. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
outer = []
rownumber = 3
columnnumber = 4
for rows in range(0,rownumber):	
	inner = []
	for columns in range(0,columnnumber):
		inner.append(rows*columns)
	outer.append(inner)
print(outer) #print [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]
#official solution
row_num = 3
col_num = 4
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]
for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col
print(multi_list) #print [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

#12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).  RM:  modified question.
accepts = ""
while True:
	accepts = input("Enter something, anything ")
	if accepts == "":
		break
	else:
		accepts = accepts.lower()
	print("Here is your input all lower case "+accepts)
#https://stackoverflow.com/questions/30239092/how-to-get-multiline-input-from-user.  You cannot input multi-line strings, for that purpose you would need to get input from the user line by line and then .join() them using \n, or you can also take various lines and concatenate them using + operator separated by \n.

#13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence. Sample Data : 0100,0011,1010,1001,1100,1001.  Expected Output : 1010.  Reference:  https://pythonspot.com/binary-numbers-and-logical-operators/
print(int('0100', 2)) #print 4
print(int('0011', 2)) #print 3
print(int('1010', 2)) #print 10
print(int('1100', 2)) #print 12
print(int('1001', 2)) #print 9
binarydivisibleby5 = []
#binaryinput = input("Enter four digit binary numbers consisting of 0s and 1s separated by a comma no spaces ")
#binaryinputlist = binaryinput.split(",")
#print(binaryinputlist)
binaryinput = ["0100","0011","1010","1001","1100","1001"]
print(binaryinput)
for eachbinaryinputlist in binaryinput:
	integer = int(eachbinaryinputlist,2)
	if integer % 5 == 0:
		binarydivisibleby5.append(eachbinaryinputlist)
print(binarydivisibleby5) #print ["1010"]

#14. Write a Python program that accepts a string and calculate the number of digits and letters. Sample Data : Python 3.2 Expected Output: Letters 6 Digits 2
letters = 0
digits = 0
numbers = [str(n) for n in range(0,10)]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
accepts = "Python 3.2"
for eachaccepts in accepts:
	eachaccepts = eachaccepts.lower()
	if eachaccepts in numbers:
		digits += 1		
	elif eachaccepts in alphabet:
		letters += 1
	else:
		continue
print("Letters",letters) #print Letters 6
print("Digits",digits) #print Digits 2
#using official solution better
accepts = "Python 3.2"
letters = 0
digits = 0
for eachaccepts in accepts:
	if eachaccepts.isdigit() is True:
		digits += 1
	elif eachaccepts.isalpha() is True:
		letters += 1
	else:
		continue
print("Letters",letters)
print("Digits",digits)

#15. Write a Python program to check the validity of password input by users. Validation :  At least 1 letter between [a-z] and 1 letter between [A-Z].  At least 1 number between [0-9].  At least 1 character from [$#@].  Minimum length 6 characters.  Maximum length 16 characters.
def checkpassword(password):
	passwordlength = len(password)
	characterlist = ["$","#","@"]
	lowercasecount = 0
	uppercasecount = 0
	charactercount = 0
	numbercount = 0
	if passwordlength >= 6 and passwordlength <=16:
		for casepassword in password:
			if casepassword.isdigit() == True:
				numbercount += 1
			elif casepassword in characterlist:
				charactercount += 1
			elif casepassword == casepassword.lower():
				lowercasecount += 1
			elif casepassword == casepassword.upper():
				uppercasecount += 1
			else:
				continue
		if lowercasecount == 0 or uppercasecount ==0 or charactercount == 0 or numbercount == 0:
			print("Invalid password "+password)
		else:
			print("Your password "+password, passwordlength)
			print("Lower",lowercasecount)
			print("Upper",uppercasecount)
			print("Special characters",charactercount)
			print("Numbers",numbercount)
	else:
		print("Invalid password length "+password)	
checkpassword("Thi55cakeisalie#")
checkpassword("987654#")
checkpassword("abc3")
#official solution
import re
#p= input("Input your password")
p="Thi55ca$slie#"
x = True
while x:  
    if (len(p)<6 or len(p)>16):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")

#16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.  #RM:  question didn't say all digits is an even number.
findnumbers = [n for n in range(100, 401)]
for eachfindnumbers in findnumbers:	
	stringnumber = str(eachfindnumbers)
	evendigit = []
	for eachstringnumber in stringnumber:
		if int(eachstringnumber) % 2 == 0:
			evendigit.append(eachstringnumber)
	evendigit = list(map(int,evendigit))
	evendigit = str(evendigit).strip("[]")
	print(stringnumber+": "+evendigit)
#official solution
# items = []
# for i in range(100, 401):
#     s = str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
#         items.append(s)
# print( ",".join(items))

#17. Write a Python program to print alphabet pattern 'A'.
"""
Expected Output:

  ***
 *   *
 *   *
 *****
 *   *
 *   *
 *   *

"""
counter = 1
while counter < 8:
	if counter == 1:
		print(" *** ")
	elif counter == 4:
		print("*****")
	else:
		print("*   *")
	counter += 1

#Questions 18-30 prints alphabet letters

#31. Write a Python program to calculate a dog's age in dog's years.  For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.  Expected Output:  Input a dog's age in human years: 15.  The dog's age in dog's years is 73.
humanyears = 15
if humanyears == 1:
	print("The dog's age in dog's years is 10.5.")
elif humanyears == 2:
	print("The dog's age in dog's years is 21.")
else:	
	afteryears = ((humanyears - 2) * 4) + 21
	print("The dog's age in dog's years is {}.".format(afteryears)) #print The dog's age in dog's years is 73.

#32. Write a Python program to check whether an alphabet is a vowel or consonant. Expected Output:  Input a letter of the alphabet: k is a consonant.
def alphabet(letterinput):
	vowel = "aeiou"
	if letterinput in vowel:
		return letterinput+" is a vowel."
	else:
		return letterinput+" is a constant."
print(alphabet("k")) #print k is a constant.
print(alphabet("e")) #print e is a vowel.

#33. Write a Python program to convert month name to a number of days.  Expected output:  List of months: January, February, March, April, May, June, July, August, September, October, November, December.  Input the name of Month: February.  No. of days: 28/29 days 
days30 = "30 days"
days31 = "31 days"
days2829 = "28/29 days"
monthinput = input("Input the name of month: ")
if monthinput == "September" or monthinput == "April" or monthinput == "June" or monthinput == "November":
	print(days30)
elif monthinput == "February":
	print(days2829)
else:
	print(days31)

#34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 
integersinput = input("Input two integers separated by a space: ")
integersinput = integersinput.split(" ")
resultsinteger = list(map(int,integersinput))
sumintegers = sum(resultsinteger)
if sumintegers >= 15 and sumintegers <=20:
	print(20)
else:
	print(sumintegers)

#35. Write a Python program to check a string represent an integer or not.  Expected Output:  Input a string:  Python.  The string is not an integer.
def checkstring(x):
	typecheck = type(x)
	if typecheck is str:
		return "The string is not an integer"
	elif typecheck is int:
		return "The string is actually an integer"
	else:
		return "The string is something else"
print(checkstring("Python")) #print The string is not an integer
print(checkstring(56)) #print The string is actually an integer

#36. Write a Python program to check a triangle is equilateral, isosceles or scalene.  Note:  An equilateral triangle is a triangle in which all three sides are equal.  A scalene triangle is a triangle that has three unequal sides.  An isosceles triangle is a triangle with (at least) two equal sides.  Expected Output:  Input lengths of the triangle sides: x:6, y:8, z:12, Scalene triangle.
xyz = input("Enter the lengths of a triangle x, y, z separated by a space ")
xyz = xyz.split(" ")
xyzlist = list(map(int,xyz))
if xyzlist[0] == xyzlist[1] == xyzlist[2]:
	print("Equilateral triangle")
elif (xyzlist[0] == xyzlist[1]) or (xyzlist[0] == xyzlist[2]) or (xyzlist[1] == xyzlist[2]):
	print("Isosceles triangle")
else:
	print("Scalene triangle")

#37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  Expected Output:  Input the month (e.g. January, February etc.): july Input the day: 31 Season is autumn
monthday = input("Enter the month and day in number separated by a space ")
monthdaylist = monthday.split(" ")
month = monthdaylist[0]
day = int(monthdaylist[1])
if (month == "December" and day>=21) or (month == "January" or month == "February") or (month == "March" and day <=20):
	print("Season is winter.")
elif (month == "March" and day >=21) or (month == "April" or month == "May") or (month == "June" and day <=20):
	print("Season is spring.")
elif (month == "June" and day >= 21) or (month == "July" or month == "August") or (month == "September" and day <=20):
	print("Season is summer.")
else:
	print("Season is autumn.")

#38. Write a Python program to display astrological sign for given date of birth.  Input birthday: 15.  Input month of birth (e.g. march, july etc): may.  Your Astrological sign is: Taurus.

#39. Write a Python program to display the sign of the Chinese Zodiac for given year in which you were born.   Expected Output:  Input your birth year: 1973.  Your Zodiac sign: Ox.

#40. Write a Python program to find the median of three values.  Expected Output:  Input first number: 15, Input second number: 26, Input third number: 29.  The median is 26.0.
from statistics import median
inputthreenumbers = input("Enter three numbers separated by a space ")
inputthreenumbers = inputthreenumbers.split(" ")
inputthreenumbers = list(map(int,inputthreenumbers))
print(median(inputthreenumbers))
#user solution
a=15
b=26
c=29
print(sorted((a,b,c))[1])

#41. Write a Python program to get next day of a given date.  Expected Output:  Input a year: 2016, Input a month [1-12]: 08, Input a day [1-31]: 23, The next date is [yyyy-mm-dd] 2016-8-24.
year = 2016
month = 2
day = 28
if (month == 12 and day == 31):
	print("{}-{}-{}".format(year+1,1,1))
elif (month == 9 or month == 4 or month == 6 or month == 11) and day == 30:
	print("{}-{}-{}".format(year,month+1,1))
elif (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and day == 31:
	print("{}-{}-{}".format(year,month+1,1))
elif (month == 2 and day == 28):  #RM  for speed reasons, all days in February is 28
	print("{}-{}-{}".format(year,month+1,1))
else:
	print("{}-{}-{}".format(year,month,day+1))