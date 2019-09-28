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
