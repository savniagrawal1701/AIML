import numpy as np
#creating matrix using numpy
matrix1=np.array([[2,3],[6,7]])
print(matrix1)

#finding shape
print(matrix1.shape)
 # creating matrix with random values
print('Create random matrix')
random_matrix=np.random.rand(3,3)
print(random_matrix)

print('Create random matrix with int values')
random_int_matrix=np.random.randint(100,size=(4,5))
print(random_int_matrix)

#maatrix with all values 1
matrix3=np.ones((2,3))
print(matrix3)

#maatrix with all values int ones
matrix4=np.ones((2,3),dtype=int)
print(matrix4)

#creating null matrix
nullmatrix=np.zeros((4,4))
print(nullmatrix)

#creting identity matrix
identity_matrix=np.eye(3,3)
print(identity_matrix)

#transpose of a matrix
a=np.random.randint(100,size=(4,5))
print(a)

transposeofa=np.transpose(a)

print(transposeofa)
