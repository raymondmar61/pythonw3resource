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


