#https://www.w3resource.com/python-exercises/math/

#1. Write a Python program to convert degree to radian.
from math import pi
degrees = 15
radians = degrees * ((pi)/180)
print(radians) #print 0.2617993877991494

#2. Write a Python program to convert radian to degree.
from math import pi
radians = .52
degrees = radians * (180/pi)
print(degrees) #print 29.79380534680281

#3. Write a Python program to calculate the area of a trapezoid.
height = 5
firstbase = 5
secondbase = 6
trapezoidarea = ((firstbase+secondbase)/2)*height
print(trapezoidarea) #print 27.5

#4. Write a Python program to calculate the area of a parallelogram.
base = 5
height = 6
parallelogramarea = base*height
print(parallelogramarea) #print 30

#5. Write a Python program to calculate surface volume and area of a cylinder.
from math import pi
height = 4
radius = 6
volumecylinder = pi*(radius**2)*height
print(volumecylinder) #print 452.3893421169302
areacylinder = (2*pi*radius*height)+(2*pi*(radius**2))
print(areacylinder) #print 376.99111843077515

#6. Write a Python program to calculate surface volume and area of a sphere. 
from math import pi
radius = .75
volmesphere = (4/3)*pi*(radius**3)
print(volmesphere) #print 1.7671458676442584
areasphere = 4*pi*(radius**2)
print(areasphere) #print 7.0685834705770345

#7. Write a Python program to calculate arc length of an angle.
from math import pi
radius = 4.5
angle = 45
angleinradians = angle * ((pi)/180)
arclength = radius*angleinradians
print(arclength) #print 3.5342917352885173

#8. Write a Python program to calculate the area of the sector.
from math import pi
radius = 4
angle = 45
area = pi*(radius**2)*(angle/360)
print(area) #print 6.283185307179586

#9. Write a Python program to calculate the discriminant value.
#Source:  https://www.solumaths.com/en/calculator-online/calculate/discriminant  =(b**2)-(4*a*c)
x = 4
y = 0
z = -4
discriminant = (y**2)-(4*x*z)
print(discriminant) #print 64

#10. Write a Python program to find the smallest multiple of the first n numbers. Also, display the factors.
#RM:  I don't understand the question.

#11. Write a Python program to calculate the difference between the squared sum of first n natural numbers and the sum of squared first n natural numbers.(default value of number=2).
n = 12
squaredsum = 0
sumsquared = 0
for x in range(1,n+1):
	squaredsum+=x
	sumsquared = (sumsquared + (x**2))
squaredsum = squaredsum**2
print(squaredsum - sumsquared) #print 5434

#12. Write a Python program to calculate the sum of all digits of the base to the specified power.
#RM:  sum each digit in a number raised to a power; e.g. 2**100 is 1267650600228229401496703205376.  Sum each digit.
def powerbasesum(base, power):
	number = pow(base, power)
	answersum = 0
	for eachnumber in str(number):
		answersum = answersum + int(eachnumber)
	return answersum
print(powerbasesum(2, 100)) #print 115
print(powerbasesum(8, 10)) #print 37

#13. Write a Python program to find out, if the given number is abundant.  Note: In number theory, an abundant number or excessive number is a number for which the sum of its proper divisors is greater than the number itself.  The integer 12 is the first abundant number. Its proper divisors are 1, 2, 3, 4 and 6 for a total of 16.
def isabundant(number):
	abundantsum = 0
	for eachnumber in range (1,number):
		if number % eachnumber == 0:		
			abundantsum+=eachnumber
	if abundantsum > number:
		return True
	else:
		return  False
print(isabundant(12)) #print True
print(isabundant(13)) #print False

#14. Write a Python program to sum all amicable numbers from 1 to specified numbers. Note: Amicable numbers are two different numbers so related that the sum of the proper divisors of each is equal to the other number. (A proper divisor of a number is a positive factor of that number other than the number itself. For example, the proper divisors of 6 are 1, 2, and 3.)
#RM:  https://projecteuler.net/problem=21 Amicable Numbers explained Amicable numbers better.
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

def isamicablenumber(firstnumber):
	divisorslista = []
	for eachnumber in range(1,firstnumber):
		if firstnumber % eachnumber == 0:
			divisorslista.append(eachnumber)
	secondnumber = sum(divisorslista)
	divisorslistb = []
	for eachnumber in range(1,secondnumber):
		if secondnumber % eachnumber == 0:
			divisorslistb.append(eachnumber)
	secondnumber = sum(divisorslistb)
	if firstnumber == secondnumber:
		return True
	else:
		return False
print(isamicablenumber(220)) #print True
print(isamicablenumber(284)) #print True
print(isamicablenumber(99)) #print False

def amicablenumberssum(number):
	amicablenumberslist = []
	counter = 2
	while counter < number:
		lista = []
		for eachnumber in range(1,counter):
			if counter % eachnumber == 0:
				lista.append(eachnumber)
		b = sum(lista)
		listb = []
		for eachnumber in range(1,b):
			if b % eachnumber == 0:
				listb.append(eachnumber)
		c = sum(listb)
		if (counter == c) and (counter != b):
			amicablenumberslist.append(counter)
			amicablenumberslist.append(b)
		else:
			pass
		counter +=2
	print(amicablenumberslist)
	print(sum(set((amicablenumberslist))))
amicablenumberssum(9999) #print 31626
amicablenumberssum(999) #print 504
amicablenumberssum(99) #print 0

#15. Write a Python program to returns sum of all divisors of a number.
def sumdivisors(number):
	divisorssum = []
	for eachnumber in range(1,number):
		if number % eachnumber == 0:
			divisorssum.append(eachnumber)
	return sum(divisorssum)
print(sumdivisors(8)) #print 7
print(sumdivisors(12)) #print 16

#16. Write a Python program to print all permutations of a given string (including duplicates).
from itertools import permutations
permutatestring = "ABC D"
permutatestring = permutatestring.replace(" ","")
permutatestringlength = len(permutatestring)
permutatestringlist = list(map(str, permutatestring))
finalanswer = []
for eachpermutation in permutations(permutatestringlist,permutatestringlength):
	#print(list(map(str, permutatestring)), end=", ") #print ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D'], ['A', 'B', 'C', 'D']
	print("".join(list(map(str, eachpermutation))))
	finalanswer.append("".join(list(map(str, eachpermutation))))
print(finalanswer) #print ['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC', 'BCAD', 'BCDA', 'BDAC', 'BDCA', 'CABD', 'CADB', 'CBAD', 'CBDA', 'CDAB', 'CDBA', 'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA']
