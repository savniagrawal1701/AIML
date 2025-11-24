import numpy as np
myarr=np.array([3,2,5,6,7],np.int64)
print(myarr)

#type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.
print(type(myarr))

#the shape of an array refers to the number of elements along each dimension of the array.
print(myarr.shape)

#To know datatype of aray
print(myarr.dtype)

#Indexing
print(myarr[0])

#changing values in array
myarr[3]=18
print(myarr)

#Ways of creating array
#1.conversion from other python structure
myarr1=np.array([[4,1,8,0,1]])
print(type(myarr1))

#2 Intrinsic numpy array creation 
#ZEROES-----The numpy.zeros() function creates a new array of a given shape and data type, filled entirely with zeros
arrzero=np.zeros((2,5))
print(arrzero)

#ARANGE-----The numpy.arange() function generates an array with evenly spaced values within a specified interval, similar to Python's built-in range() function but returning a NumPy array.
aran=np.arange(7)
print(aran)

#LINSPACE------numpy.linspace() is a function within the NumPy library in Python that generates an array of evenly spaced numbers over a specified interval.
#SYNATX-----(start ,stop ,  total no of elements)
lspace=np.linspace(2,20,10)
print(lspace)

#EMPTY-----The numpy.empty() function in NumPy creates a new array of a specified shape and data type without initializing its elements. This means the array will contain arbitrary, uninitialized values
emp=np.empty((4,5))
print(emp)

#EMPTYLIKE-----numpy.empty_like() creates a new NumPy array with the same shape and data type as a given "prototype" array, but with uninitialized (arbitrary) values
emplike=np.empty_like(myarr)
print(emplike)

#IDENTITY-----numpy.identity(n, dtype=None) creates a square identity matrix of size n x n. This matrix has ones along its main diagonal (from top-left to bottom-right) and zeros in all other positions.
ide=np.identity(3,dtype=float)
print(ide)

#RESHAPE----The numpy.reshape() function allows you to change the shape (dimensions) of a NumPy array without altering its data. It returns a new array with the specified shape, as long as the total number of elements remains the same. (NO OF ELEMENTS SHOULD BE SAME)
resh=np.arange(8)
new=resh.reshape(4,2)
print(resh) #origunal array is not changed
print(new)

#RAVEL-----numpy.ravel() is a function that transforms a multi-dimensional NumPy array into a one-dimensional array.
new=np.ravel(new)
print(new)

#AXIS
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
#axis =0 (downward -signifies rows) This means it aggregates values across rows for each column.(sum of 1st col vvalues )
print(x.sum(axis =0))


#ATTRIBUTE AND METHODs OF NUMPY
#TRANSPOSE
print("Transpose of x\n",x.T)

#FlAT----will provide a 1-d iterator over a numpy aray (it will iterate row wise)
x.flat
for item in x.flat:
    print(item )


#ndim----Tells dimension of aray
print("Tells Dimension of aray\n",x.ndim)

#SIZE----Tells total number of elements
print("Total no of elements in an array",x.size)

#nBYTES----Total no of bytes consumed in an array
print("Total no of bytes consumed in an array",x.nbytes)


#METHODS
#argmax() and argmin()----return index of max min element
#2d array mea row wise seedha kar liya and woh wala index
print(x.argmax())
print(x.argmin())

#argsort()----- Instead of returning the sorted array itself, it returns an array of indices that would sort the original array.
print("array with indices  that will sort the array ",x.argsort())


#mathematical operation in an array 
arr0 = np.array([[1, 2, 3],[8,5,2],[3,2,8]])
arr2 = np.array([[4, 5, 6],[0,5,1],[3,5,8]])

    # Addition
print("Addition of two array",arr0 + arr2) 

   # Multiplication
print("Multiplication of two array",arr0 * arr2)

#square root
print(np.sqrt(arr0))

#max min in an array 
print(x.min(),x.max())


#counting non zero
print(np.count_nonzero(arr2))

#MEAN
print(np.mean(arr0, axis=0))

#trigno

import numpy as np

# Create a NumPy array of angles in degrees
angles_deg = np.array([0, 30, 45, 60, 90])

# Convert degrees to radians
angles_rad = np.deg2rad(angles_deg)
print(f"Angles in radians: {angles_rad}")

# Calculate sine of the angles
sine_values = np.sin(angles_rad)
print(f"Sine values: {sine_values}")

# Calculate cosine of the angles
cosine_values = np.cos(angles_rad)
print(f"Cosine values: {cosine_values}")

# Calculate tangent of the angles
tangent_values = np.tan(angles_rad)
print(f"Tangent values: {tangent_values}")

# Calculate arcsine of sine_values
arcsin_values = np.arcsin(sine_values)
print(f"Arcsine values (in radians): {arcsin_values}")
