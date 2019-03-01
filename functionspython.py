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