import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 

## plotting a vector
plt.quiver(0,0,5,5)
plt.show()


plt.quiver(0,0,5,5,scale_units='xy', angles='xy',scale=1,color='b')
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()
 # plotting multiple vectors
plt.quiver(0,0,5,5,scale_units='xy', angles='xy',scale=1,color='b')
plt.quiver(0,0,-4,-4,scale_units='xy', angles='xy',scale=1,color='y')
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()
##Addition of 2 vectors
v1=np.asarray([0,0,2,3])
v2=np.asarray([0,0,5,2])
sum=v1+v2
print(sum)
#Multiplying vectors
v3=np.asarray([0,0,6,2])
vmul=2*v3
print(vmul)
