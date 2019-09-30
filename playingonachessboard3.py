#https://www.codewars.com/kata/playing-on-a-chessboard
#6 Kyu
#With a friend we used to play the following game on a chessboard (8, rows, 8 columns). On the first row at the bottom we put numbers:  1/2, 2/3, 3/4, 4/5, 5/6, 6/7, 7/8, 8/9
#On row 2 (2nd row from the bottom) we have:  1/3, 2/4, 3/5, 4/6, 5/7, 6/8, 7/9, 8/10
#On row 3:  1/4, 2/5, 3/6, 4/7, 5/8, 6/9, 7/10, 8/11
#until last row:  1/9, 2/10, 3/11, 4/12, 5/13, 6/14, 7/15, 8/16
#When all numbers are on the chessboard each in turn we toss a coin. The one who get "head" wins and the other gives him, in dollars, the sum of the numbers on the chessboard. We play for fun, the dollars come from a monopoly game!
#How much can I (or my friend) win or loses for each game if the chessboard has n rows and n columns? Add all of the fractional values on an n by n sized board and give the answer as a simplified fraction.
#For Python, the function called 'game' with parameter n (integer >= 0) returns as result an irreducible fraction written as an array of integers: [numerator, denominator]. If the denominator is 1 return [numerator].
#test.assert_equals(game(0), [0])
#test.assert_equals(game(1), [1, 2])
#test.assert_equals(game(8), [32])

import numpy as np

def game(size):
	if size == 0:
		return [0]
	numerator = np.array([n for n in range(1,size+1)]*size, dtype=np.int64)
	denominator = np.array([], dtype=np.int64)
	uniquedenominators = np.arange(2,(size*2)+1)
	# print("uniquedenominators",uniquedenominators)
	dollars = []
	leastcommonmultiple = np.lcm.reduce(uniquedenominators)
	for row in range(1,size+1):
		for eachdenominator in range(1,size+1):
			denominator = np.append(denominator, np.array(row+eachdenominator, dtype=np.int64))
	numeratorconversion = np.array([], dtype=np.int64)
	for x in range(0,len(numerator)):		
		numeratorconversion = np.append(numeratorconversion, ((leastcommonmultiple//denominator[x])*numerator[x]))
	leastcommonmultipleconversion = np.array([])
	numerator = np.sum(numeratorconversion)
	print("numerator",numerator)
	print("denominator",denominator)
	print("leastcommonmultiple",leastcommonmultiple)
	print("numeratorconversion",numeratorconversion)
	if numerator % leastcommonmultiple == 0:
		dollars.append(numerator//leastcommonmultiple)
	else:
		dollars.append(numerator)
		dollars.append(leastcommonmultiple)
	return dollars
# print(game(0))
# print(game(1))
# print(game(3))
print(game(8))
# print(game(100))
#print(game(1000))


