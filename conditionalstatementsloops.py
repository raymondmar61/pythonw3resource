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