#https://www.w3resource.com/python-exercises/numpy/basic/index.php
#Reference:  numpy constants https://numpy.org/devdocs/reference/constants.html
import numpy as np

#1.Write a NumPy program to get the numpy version and show numpy build configuration.
print(np.__version__)
print(np.show_config())

#2. Write a NumPy program to  get help on the add function.
print(np.info(np.add))

#3. Write a NumPy program to test whether none of the elements of a given array is zero.  In other words, any no zeroes.
randomintegers = np.random.randint(-10, 10, size=[1,10]) #number is from -10 to 10 exclusive 1 row 10 entries
print(randomintegers) #print [[-9  2 -6  0  0 -4  4 -9 -1 -6]]
isthereazero = randomintegers[randomintegers == 0]
print(isthereazero == 0) #print [ True  True]
print(randomintegers.all(0)) #print [ True  True  True False False  True  True  True  True  True]
print(np.all(randomintegers)) #print True
x = np.array([1, 2, 3, 4])
print(np.all(x)) #print True
x = np.array([0, 1, 2, 3])
print(np.all(x)) #print False

#4. Write a NumPy program to test if any of the elements of a given array is non-zero.  In other words, all no zeroes.
randomintegers = np.random.randint(-10, 10, size=[1,10]) #number is from -10 to 10 exclusive 1 row 10 entries
print(randomintegers) #print [[-1 -2  4  0 -1 -4  7 -9  0 -6]]
print(randomintegers.any(0)) #print [ True  True  True False  True  True  True  True False  True]
print(np.any(randomintegers)) #print True
x = np.array([1, 2, 3, 4])
print(np.any(x)) #print True
x = np.array([0, 1, 2, 3])
print(np.any(x)) #print True
x = np.array([0, 0, 0, 0])
print(np.any(x)) #print False

#5. Write a NumPy program to test a given array element-wise for finiteness (not infinity or not a Number).
randomintegers = np.random.randint(-10, 10, size=[1,10]) #number is from -10 to 10 exclusive 1 row 10 entries
print(randomintegers) #print [[-2  2 -2 -1  2 -5 -4  3 -5  0]]
print(np.isfinite(randomintegers)) #print [[ True  True  True  True  True  True  True  True  True  True]]
officialsolution = np.array([1, 0, np.nan, np.inf]) #np.nan is Not a Number, np.inf is a floating point representing positive infinity
print(np.isfinite(officialsolution)) #print [ True  True False False]

#6. Write a NumPy program to test element-wise for positive or negative infinity.
randomintegers = np.random.randint(-10, 10, size=[1,10]) #number is from -10 to 10 exclusive 1 row 10 entries
print(randomintegers) #print [[  3   5   5   6  -4   1 -10   2   8   4]]
print(np.isinf(randomintegers)) #print [[False False False False False False False False False False]]
officialsolution = np.array([1, 0, np.nan, np.inf])  #np.nan is Not a Number, np.inf is a floating point representing positive infinity
print(np.isinf(officialsolution)) #print [False False False  True]

#7. Write a NumPy program to test element-wise for NaN of a given array.
randomintegers = np.random.randint(-10, 10, size=[1,10]) #number is from -10 to 10 exclusive 1 row 10 entries
print(randomintegers) #print [[ 4 -9  4 -9  5  3 -3  8 -8 -2]]
print(np.isnan(randomintegers)) #print [[False False False False False False False False False False]]
officialsolution = np.array([1, 0, np.nan, np.inf])  #np.nan is Not a Number, np.inf is a floating point representing positive infinity
print(np.isnan(officialsolution)) #print [False False  True False]

#8. Write a NumPy program to test element-wise for complex number, real number of a given array. Also test if a given number is a scalar type or not.
randomintegers = np.random.randint(-10, 10, size=[1,10]) #number is from -10 to 10 exclusive 1 row 10 entries
print(randomintegers) #print [[ 0  6  7  5  3 -1  3 -3  3  4]]
print(np.iscomplex(randomintegers)) #print [[False False False False False False False False False False]]
print(np.isreal(randomintegers)) #print [[ True  True  True  True  True  True  True  True  True  True]]
officialsolution = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print(np.iscomplex(officialsolution)) #print [ True False False False False  True]
print(np.isreal(officialsolution)) #print [False  True  True  True  True False]
print(np.isscalar(3.1)) #print True
print(np.isscalar([3.1])) #print False

#9. Write a NumPy program to test if two arrays are element-wise equal within a tolerance.
#Sources: https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_equal.html, https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html
numpya = np.array([1,2,3])
numpyb = np.array([33,51,398493])
numpyc = np.array([1,2,3])
numpyd = np.array([2,3,4])
print(np.array_equal(numpya,numpyc)) #print True
print(np.array_equal(numpyb,numpyc)) #print False
print(np.allclose(numpya, numpyd, rtol=1, atol=1)) #print True
print(np.allclose(numpya, numpyb, rtol=1, atol=1)) #print True

#10. Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays
numpya = np.array([1,2,3])
numpyb = np.array([33,51,398493])
numpyc = np.array([1,2,3])
numpyd = np.array([2,3,4])
numpye = np.array([77,20,-1])
print(numpya >= numpyb) #print [False False False]
print(numpya >= numpyc) #print [ True  True  True]
print(numpyd > numpyc) #print [ True  True  True]
print(numpyb > numpyc) #print [False False False]
print(numpyb > numpye) #print [False  True  True]
numpyx = ([3,5])
numpyy = ([2,5])
print(np.greater(numpyx,numpyy)) #print [ True False]
print(np.greater_equal(numpyx,numpyy)) #print [ True  True]
print(np.less(numpyx,numpyy)) #print [False False]
print(np.less_equal(numpyx,numpyy)) #print [False  True]
print(np.less(numpyy,numpyx)) #print [ True False]

#11. Write a NumPy program to create an element-wise comparison (equal, equal within a tolerance) of two given arrays.
numpya = np.array([1,2,3])
numpyb = np.array([33,51,398493])
numpyc = np.array([1,2,3])
numpyd = np.array([2,3,4])
numpye = np.array([77,20,-1])
numpyf = np.array([1,5,9,8,9,10,65,98])
numpyg = np.array([1,6,8,4,9,10,56,40])
print(np.equal(numpyf,numpyg)) #print [ True False False False  True  True False False]
print(np.greater(numpyf,numpyg)) #print [False False  True  True False False  True  True]
print(np.less(numpyf,numpyg)) #print [False  True False False False False False False]
print(np.greater_equal(numpyf,numpyg)) #print [ True False  True  True  True  True  True  True]
print(np.less_equal(numpyf,numpyg)) #print [ True  True False False  True  True False False]

#12. Write a NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.
numpyvalues = np.array([1,7,13,105])
print(numpyvalues.itemsize) #print 8 #memory size in bytes

#13. Write a NumPy program to create an array of 10 zeros,10 ones, 10 fives.
numpyzeros = np.zeros(10)
print(numpyzeros) #print[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
numpyones = np.ones(10, dtype=np.int16)
print(numpyones) #print [1 1 1 1 1 1 1 1 1 1]
numpyfives = np.linspace(5,5,10, dtype=np.int16)
print(numpyfives) #print [5 5 5 5 5 5 5 5 5 5]

#14. Write a NumPy program to create an array of the integers from 30 to70.
integers3070 = np.arange(30,71,1)
print(integers3070) #print [30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70]

#15. Write a NumPy program to create an array of all the even integers from 30 to 70.
integers3070 = np.arange(30,71,2)
print(integers3070) #print [30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70]

#16. Write a NumPy program to create a 3x3 identity matrix.
print(np.identity(3))
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''

#17. Write a NumPy program to generate a random number between 0 and 1.
randomnumber01 = np.random.random(1)
print(randomnumber01) #print [0.66874215]
#official solution
rand_num = np.random.normal(0,1,1)
print(rand_num) #print [0.20932705]
rand_num = np.random.normal(0,1,5)
print(rand_num) #print [ 0.01550774 -0.46678178  0.04564863  0.14748109  0.80262617]
rand_num = np.random.normal(0,500,3)
print(rand_num) #print [719.70605161 704.96887588 256.56701177]

#18. Write a NumPy program to generate an array of 15 random numbers from a standard normal distribution.
randomnumbers15 = np.random.randint(0,100,15)
print(randomnumbers15) #print [83 51 73 12 72 44 86 52 51 20 35 38  5 25 78]
print(randomnumbers15.std()) #print 25.22608878830715
#official solution  RM:  dumb answer
rand_num = np.random.normal(0,1,15)
print("15 random numbers from a standard normal distribution:")
print(rand_num) #print [ 0.58968788 -1.30451068 -0.16452003 -0.36511579 -0.52806576  0.07834043  0.74370826 -0.03742576 -0.63248241 -1.24015999  0.28567644 -1.4467676  0.02737708  0.73224269 -0.353737  ]

#19. Write a NumPy program to create a vector with values ranging from 15 to 55 and print all values except the first and last.
vector = np.arange(15,56)
print(vector) #print [15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55]
print(vector[1:-1]) #print [16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54]

#20. Write a NumPy program to create a 3X4 array using and iterate over it.
threebyfourarray = np.empty((3,4), dtype=np.int32)
print(threebyfourarray)
'''
[[  39387616          0  -42307712      32693]
 [  10969120          0 -304512656      32693]
 [-304512528      32693 -304512464      32693]]
'''
for eachrow in range(0,threebyfourarray.shape[0]):
	for eachcolumn in range(0,threebyfourarray.shape[1]):
		print(threebyfourarray[eachrow][eachcolumn],end=", ") #print 39387616, 0, -42307712, 32693, 10969120, 0, -304512656, 32693, -304512528, 32693, -304512464, 32693,
print("\n")
#official solution
arraytens = np.arange(10,22).reshape(3,4)
print(arraytens)
'''
[[10 11 12 13]
 [14 15 16 17]
 [18 19 20 21]]
'''
for eacharraytens in np.nditer(arraytens):
	print(eacharraytens, end=", ") #print 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 

#21. Write a NumPy program to create a vector of length 10 with values evenly distributed between 5 and 50.
size10 = np.linspace(5, 50, 10, dtype=np.int8)
print(size10.size) #print 10
print(size10) #print [ 5 10 15 20 25 30 35 40 45 50]
#RM:  question asked for length 10, not size 10
length10 = np.linspace(5, 50, 5)
print(length10.size) #print 5
print(length10) #print [ 5.   16.25 27.5  38.75 50.  ]

#22. Write a NumPy program to create a vector with values from 0 to 20 and change the sign of the numbers in the range from 9 to 15.
numpyh = np.arange(0, 21)
print(numpyh) #print [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
for x in range(9,16):
	numpyh[x] = (numpyh[x]*-1)
print(numpyh) #print [  0   1   2   3   4   5   6   7   8  -9 -10 -11 -12 -13 -14 -15  16  17  18  19  20]
#official solution
numpyh = np.arange(0, 21)
numpyh[(numpyh >= 9) & (numpyh <= 15)] *= -1
print(numpyh) #[  0   1   2   3   4   5   6   7   8  -9 -10 -11 -12 -13 -14 -15  16  17  18  19  20]

#23. Write a NumPy program to create a vector of length 5 filled with arbitrary integers from 0 to 10.
vectorfive = np.random.randint(0,11,5)
print(vectorfive) #print [7 9 3 3 5]

#24. Write a NumPy program to multiply the values of two given vectors.
multiply1 = np.random.randint(0,11,5)
multiply2 = np.random.randint(0,11,5)
multply12 = multiply1*multiply2
print(multiply1) #print [ 7  8 10 10  4]
print(multiply2) #print [10  8  6 10  9]
print(multply12) #print [ 70  64  60 100  36]

#25. Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.
matrix34 = np.arange(10,22).reshape(3,4)
print(matrix34)
'''
[[10 11 12 13]
 [14 15 16 17]
 [18 19 20 21]]
'''

#26. Write a NumPy program to find the number of rows and columns of a given matrix.
matrix34 = np.arange(10,22).reshape(3,4)
print(matrix34.shape) #print (3, 4)

#27. Write a NumPy program to create a 3x3 identity matrix, i.e. diagonal elements are 1, the rest are 0.
print(np.identity(3))
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''
#official solution
x = np.eye(3)
print(x)

#28. Write a NumPy program to create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.
numpyzeroes = np.zeros((10,10), dtype=np.int16)
print(numpyzeroes)
'''
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]

'''
numpyzeroes[0:1,0:10] = 1
numpyzeroes[9:10,0:10] = 1
numpyzeroes[:,0:1] = 1
numpyzeroes[:,9:10] = 1
print(numpyzeroes)
'''
[[1 1 1 1 1 1 1 1 1 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 0 0 0 0 0 0 0 0 1]
 [1 1 1 1 1 1 1 1 1 1]]
'''
#RM:  incorrect assigning and slicing.  I mentioned the variable numpyzeroes twice.  Too tired.  Take a break.
# numpyzeroes[numpyzeroes[0:1,0:10]] = 1
# numpyzeroes[numpyzeroes[9:10,0:10]] = 2
# numpyzeroes[numpyzeroes[:,0:1]] = 3
# numpyzeroes[numpyzeroes[:,9:10]] = 4
#official solution
x = np.ones((10, 10))
x[1:-1, 1:-1] = 0
print(x)





