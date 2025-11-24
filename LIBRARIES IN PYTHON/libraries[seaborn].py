#Seaborn is a powerful and popular data visualization library in Python. #It is built on top of Matplotlib and provides a high-level interface for creating informative and attractive statistical graphic
import seaborn as sns
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
#inbuilt dataset
tips=sns.load_dataset('tips')

#evaluting first 5 dataset using pandas
print("Tips Dataset")
print(tips.head())

#visualising the datsset
sns.relplot(data=tips,x='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size') 
#The seaborn.relplot() function is a figure-level function in the Seaborn library designed to visualize statistical relationships between variables
plt.show()

#setting the theme for the plots
#Seaborn offers several built-in themes to control the aesthetic style of plots. These themes affect elements such as background color, grid lines, and other visual details.
sns.set_theme(style="dark", palette="pastel", font_scale=1.2)
sns.relplot(data=tips,x='total_bill',y='tip',col='time',hue='smoker',style='smoker',size='size') 
#data=tips: Specifies the dataset to be used, which is named tips.
#x='total_bill': Assigns the total_bill column to the x-axis, representing the total cost of the bill.
#y='tip': Assigns the tip column to the y-axis, representing the tip amount.
#col='time': Creates separate columns of plots based on the time column, effectively separating the data into "Lunch" and "Dinner" plots.
#hue='smoker': Colors the data points based on the smoker column, differentiating between "Yes" and "No" smokers with different colors.
#style='smoker': Changes the marker style (e.g., shape) of the data points based on the smoker column. This provides a redundant visual cue in addition to hue, making the plot more accessible.
#size='size': Adjusts the size of each data point based on the size column, representing the number of people in the party. 
plt.show()



#load irs dataset 
iris=sns.load_dataset('iris')
print(iris.head())

#To predit to what species the particular iris flower belongs based on their sepal lenght ,sepal width and petal lenght an dpeta width
#USING SCATTER PLOT
sns.scatterplot(x='sepal_length',y='petal_length',hue='species',data=iris)
plt.show()

#SCATTER PLOT WITH DIFFERENT PARAMETERS
sns.scatterplot(x='sepal_length',y='petal_width',hue='species',data=iris)
plt.show()

#COUNT PLOT
#The seaborn.countplot() function in Python's Seaborn library is used to visualize the distribution of a categorical variable. It displays the count of observations within each category as bars, essentially acting as a histogram for categorical data.


#LOADING TITANIC DATASET
titanic=sns.load_dataset('titanic')
print(titanic.head())

#whether thee person has survived or not on class basis 
sns.countplot(x='class',data=titanic)
sns.countplot(x='survived',data=titanic)
plt.show()

#BARPLOT
sns.barplot(x='sex',y='survived',hue='class',data=titanic)
plt.show()

#DISTRIBUTION PLOT
#A distribution plot is a visualization that shows how data is spread out or its frequency over a continuous range
sns.displot(titanic['age'])
plt.show()

#heatmap is usd to plot correlation
#A Seaborn heatmap is a powerful data visualization tool used to represent two-dimensional data where individual values within a matrix are depicted by colors.
cor=titanic.corr()
plt.figure(figsize=(10,10))
sns.heatmap(cor,cbar=True,square=True,fmt='.1f',annot=True,annot_kws={"size": 8} ,cmap='Blues')
plt.show()