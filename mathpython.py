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
