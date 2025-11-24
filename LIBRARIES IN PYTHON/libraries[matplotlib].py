#Line plots
import matplotlib.pyplot as plt
import numpy as np

#SINE <COSINE
x=np.linspace(10,20,30)
y=np.sin(x)
plt.plot(x,y)
plt.show()

z=np.cos(x)
plt.plot(x,z)
plt.show()

#parabola
k=np.linspace(-10,10,20)
y=k**2
plt.plot(k,y,'r+')
plt.show()

#plotting multiple graphs
plt.plot(x,np.sin(x),'g')
plt.plot(x,np.cos(x),'r')
plt.show()

#bar plot

# Data for the bar plot
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [25, 40, 30, 55]

# Create the bar plot
plt.bar(categories, values)

# Add labels and a title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Basic Bar Plot Example')

# Display the plot
plt.show()


#PIE CHART

values = [12, 11, 3, 30]  # Example data
plt.pie(values)
plt.show()


#scatter plot
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 4, 5, 4, 6])

plt.scatter(x1, y1)
plt.show()


##D scatter plot
fig3=plt.figure()
ax=plt.axes(projection='3d')
z3=20*np.random.random(100)
x3=np.sin(z3)
y3=np.cos(z3)
ax.scatter(x3,y3,z3,c=z3  ,cmap='Blues')
plt.show()