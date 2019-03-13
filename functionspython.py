#https://www.w3resource.com/python-exercises/python-functions-exercises.php

#1. Write a Python function to find the Max of three numbers.
def maxnumbers(n1, n2, n3):
	return max(n1, n2, n3)
print(maxnumbers(1, 100, 999999)) #print 999999
print(maxnumbers(5, 8, 33)) #print 33

#2. Write a Python function to sum all the numbers in a list.  Sample List: (8, 2, 3, 0, 7).  Expected Output: 20.
def sumthelist(inputlist):
	return sum(inputlist)
print(sumthelist([8, 2, 3, 0, 7])) #print 20

#3. Write a Python function to multiply all the numbers in a list.  Sample List: (8, 2, 3, -1, 7).  Expected Output: -336.  #RM:  I can't use list comprehension because I'm not returning a list
def multiplylist(inputlist):
	product = 1	
	for eachinputlist in inputlist:
		product *= eachinputlist
	return product
print(multiplylist([8, 2, 3, -1, 7])) #print -336

#4. Write a Python program to reverse a string. Sample String: "1234abcd".  Expected Output: "dcba4321".
def reversethestring(inputstring):
	return inputstring[::-1]
print(reversethestring("1234abcd"))

#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
from math import factorial
def numberfactorial(n):
	return factorial(n)
print(numberfactorial(4)) #print 24
print(numberfactorial(10)) #print 3628800

#6.Write a Python function to check whether a number is in a given range.
from random import randint
lowerrange = randint(1,10)
upperrange = randint(11,20)
def rangecheck(n):
	if n >= lowerrange and n <=upperrange:
		print(n, lowerrange, upperrange)
		return "In Range"
	else:
		print(n, lowerrange, upperrange)
		return "Not In Range"
print(rangecheck(7)) #print 7 6 12\n In Range
print(rangecheck(14)) #print 14 6 12\n Not In Range
#official solution
def test_range(n):
    if n in range(3,9):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5) #return 5 is in the range

#7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Sample String : 'The quick Brow Fox'.  Expected Output:  No. of Upper case characters: 3  No. of Lower case Characters: 12.
#ord(character) returns ascii of the character.  chr(ascii number) returns character of the ascii number.  Specifically, ord(character)-64 returns the upper case alphabeutical number.  ord(character)-96 returns lower case alphabeutical number.  a-z 97-122.  A-Z 65-90.  print(ord("a")) #print 97.  print(ord("Z")) #print 90
def countupperlowercase(samplestring):
	lowercount = 0
	uppercount = 0
	for eachsamplestring in samplestring:
		if eachsamplestring == " ":
			continue
		elif (ord(eachsamplestring) >=97) and (ord(eachsamplestring) <=127):
			lowercount += 1
		elif (ord(eachsamplestring) >=65) and (ord(eachsamplestring) <=90):
			uppercount += 1
	print("No. of Upper case characters {}".format(uppercount))
	print("No. of Lower case characters {}".format(lowercount))
countupperlowercase("The quick Brow Fox") #return No. of Upper case characters 3\n No. of Lower case characters 12
#official solution
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])
string_test('The quick Brow Fox')

#8. Write a Python function that takes a list and returns a new list with unique elements of the first list.  Sample List: [1,2,3,3,3,3,4,5].  Unique List: [1, 2, 3, 4, 5].
def uniqueelements(samplelist):
	return list(set(samplelist))
print(uniqueelements([1,2,3,3,3,3,4,5])) #print [1, 2, 3, 4, 5]

#9. Write a Python function that takes a number as a parameter and check the number is prime or not.
def isprime(n):
	if n == 1:
		return False #1 is not a prime number
	for d in range(2, n):
		if n % d == 0:
			return False
	return True
print(isprime(1)) #print False
print(isprime(7)) #print True
print(isprime(100)) #print False

#10. Write a Python program to print the even numbers from a given list.  Sample List: [1, 2, 3, 4, 5, 6, 7, 8, 9].  Expected Result: [2, 4, 6, 8].
def evennumbers(givenlist):
	evennumberslist = []
	for eachgivenlist in givenlist:
		if eachgivenlist % 2 == 0:
			evennumberslist.append(eachgivenlist)
	return evennumberslist
print(evennumbers([1, 2, 3, 4, 5, 6, 7, 8, 9])) #print [2, 4, 6, 8]

#11. Write a Python function to check whether a number is perfect or not. According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).  Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
def perfectnumber(number):
	divisorslist = []
	for eachnumber in range(1,number):
		if number % eachnumber == 0:
			divisorslist.append(eachnumber)
	sumdivisors = sum(divisorslist)
	if sumdivisors == number:
		return "Perfect Number"
	else:
		return "Not Perfect Number"
print(perfectnumber(6)) #print Perfect Number
print(perfectnumber(28)) #print Perfect Number
print(perfectnumber(8128)) #print Perfect Number
print(perfectnumber(564897)) #print Not Perfect Number

#12. Write a Python function that checks whether a passed string is palindrome or not.  Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palindrome(passedstring):
	nospaces = [eachpassedstring for eachpassedstring in passedstring if eachpassedstring != " "]
	passedstring = "".join(nospaces)
	if passedstring == passedstring[::-1]:
		return ("palindrome")
	else:
		return ("not a palindrome")
print(palindrome("madam")) #print palindrome
print(palindrome("nurses run")) #print palindrome
print(palindrome("joyful")) #print not a palindrome

#13. Write a Python function that prints out the first n rows of Pascal's triangle. Note: Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
#Source:  https://www.geeksforgeeks.org/pascal-triangle/
def printPascal(n):      
	# Iterate through every line  and print entries in it 
	for line in range(0, n):           
	# Every line has number of  integers equal to line number 
		for i in range(0, line + 1) : 
			print(binomialCoeff(line, i), " ", end = "") 
		print()
def binomialCoeff(n, k): 
	res = 1
	if (k > n - k):
		k = n - k
	for i in range(0 , k):
		res = res * (n - i)
		res = res // (i + 1)
	return res  
n = 7
printPascal(n) 
#official solution
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6) 