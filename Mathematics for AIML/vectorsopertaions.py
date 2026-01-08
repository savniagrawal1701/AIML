import numpy as np
#Dot products of two vectors
a=np.array([2,3])
b=np.array([4,4])
a_dot_b=np.dot(a,b)
print(a_dot_b)

#Cross product
a=np.array([2,3,6])
b=np.array([4,4,7])
a_cross_b=np.cross(a,b)
print(a_cross_b)

#projecion of a vector 
# a on b 
a=np.array([2,5])
v=np.array([8,-6])
magnitude_of_v=np.sqrt(sum(v**2))
proj_of_a_on_v=(np.dot(a,v)/magnitude_of_v**2)*v
print("projection of a on v",proj_of_a_on_v)