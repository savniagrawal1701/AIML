import numpy as np
#addition
A=np.array([[2,3],[4,5]])
B=np.array([[6,7],[8,9]])
sum=A+B
print(sum)

#another way
sum2=np.add(A,B)
print(sum2)

#substracting
difference=A-B
print(difference)

diff=np.subtract(A,B)
print(diff)

#scaler multiplication
x=5
y=np.random.randint(10,size=(4,4))
product=np.multiply(x,y)
print(product)

#multipliy two matrix
matrix1=np.random.randint(10,size=(4,5))
matrix2=np.random.randint(10,size=(5,3))

matrixmulti=np.dot(matrix1,matrix2)


