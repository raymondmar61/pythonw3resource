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