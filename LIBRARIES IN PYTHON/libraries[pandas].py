#Pandas is an open-source Python library widely used for data manipulation and analysis. It provides powerful and flexible data structures, particularly the DataFrame and Series, designed to handle tabular and time-series data efficiently.

#how  to work with pandas library(how to create dataframe from dictonary)
import pandas as pd 
import numpy as np
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'Paris']
}
df = pd.DataFrame(data)
print("DataFrame created from dictionary:")
print(df) #0,1,2..are indexes which is udes to identify rows and coloumn are identified by col name

#to convert this into excel sheet 
df.to_csv('df')

#to convert this into excel sheet without indexes
df.to_csv('df',index=False)

#head-----The head() method returns the first n rows of a DataFrame or Series. By default, it returns the first 5 rows if no argument is provided. 
#tail-----The tail() method returns the last n rows of a DataFrame or Series. Similar to head(), it returns the last 5 rows by default if no argument is provided. 
print("First 5 rows:")
print(df.head())
print("Last 2 rows:")
print(df.tail(2))

#Describe-----The describe() method in Pandas generates descriptive statistics of DataFrame columns which provides key metrics like mean, standard deviation, percentiles and more.


#how to read a csv
read_csv=pd.read_csv('salary_data.csv')
print(read_csv)

#How to change indexing 
#df.index=[1,2,3,4]
#print(df)

#MORE ABOUT PANDAS
#Series: A Series is a one-dimensional labeled array capable of holding data of any type (integers, strings, floats, Python objects, etc.). It can be thought of as a single column of data with an associated index.
#DataFrame: A DataFrame is a two-dimensional labeled tabular data structure with columns of potentially different types. It is similar to a spreadsheet or a table in a relational database, with both row and column labels. A DataFrame can be considered a collection of Series, where each column is a Series

#series
s = pd.Series([10, 20, 30, 40])
print(s)

#using random
#Generate n random no with indexes in tabular form
ser=pd.Series(np.random.rand(4))
print(ser)

newdf=pd.DataFrame(np.random.rand(2,3),index=np.arange(2))
print(newdf)

#DROP
#used to delte row and col
delet=df.drop(0)
print(delet)

#how to convert data frame into numpy
conversion=newdf.to_numpy
print("converting into numpy\n")
print(conversion)

#ATTRIBUTES
#transpose 
#all of numpy

#SORTING INDEXES
 #TO sort  DataFrame or Series by its index, you use the .sort_index() method. This method allows you to sort based on the row index (default) or the column index.
data1= {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [28, 22, 25]}
df1= pd.DataFrame(data)
newdf1=df1.sort_index(axis=0,ascending=False)
print(newdf1)

#View:
#A view is a shallow copy or a reference to the original data. It does not create a new independent object in memory.
#Modifying a view will affect the original DataFrame or Series because both are pointing to the same underlying data.
#Views are often created for efficiency when pandas can avoid making a full copy, for example, during certain indexing operations #(though this behavior can be complex and depends on memory layout).
#Copy:
#A copy is a deep copy or an independent duplicate of the original data. It creates a new object in memory with its own data.
#Modifying a copy will not affect the original DataFrame or Series because they are separate entities.
#Copies are explicitly created using methods like .copy() or when operations inherently require a new, independent data structure.


#loc
#In Pandas, .loc is a label-based indexer used for selecting data from a DataFrame. It allows you to access rows and columns using their labels (names) rather than their integer positions.
#sometimes pandas decide by itself because of internal memory management that it will return view or copy that is why we use loc

#changing the values using loc
df1.loc[0,'Name']="Savni"
print(df1)

#Slicing Data by Labels
# Select rows 'row_a' and 'row_c'
multiple_rows = df1.loc[[1,2]]
print(multiple_rows)
#3. Slicing a range of rows by labels:


# Select rows from 'row_a' to 'row_c' (inclusive)
sliced_rows = df1.loc['1':'2']
print(sliced_rows)

#Applying queries
print("Applying queries\n")
print(df1.loc[df1['Age']<30])

#iloc
#The iloc property in Pandas DataFrames and Series is used for integer-location-based indexing. This means you select data based on its numerical position (index) rather than its label.

# Retrieve the first row
first_row = df.iloc[0]
print("First row:\n", first_row)

# Retrieve the third column (all rows)
third_column = df.iloc[:, 2]
print("\nThird column:\n", third_column)

# Retrieve a specific cell (row 1, column 0)
specific_cell = df.iloc[1, 0]
print("\nSpecific cell (row 1, col 0):", specific_cell)

# Retrieve a slice of rows and columns (rows 0-1, columns 0-1)
subset = df.iloc[0:2, 0:2]
print("\nSubset (rows 0-1, cols 0-1):\n", subset)

#implace=true ,it will change ,modify the original dataframe


# Detect null values in the entire DataFrame
null_df = df.isnull()
print("DataFrame with nulls detected:\n", null_df)

#dropna---drops rows and coloumn with null values

#drop_duplicates----remove duplocates



#handling sheet from pandas
#Essential information includes: 
#The primary function for reading an Excel file into a pandas DataFrame is pd.read_excel('filename.xlsx').
#To read a specific sheet within a workbook, the sheet_name parameter is used, for example: pd.read_excel('filename.xlsx', #sheet_name='Sheet2').
#To write a DataFrame to a specific Excel sheet, the .to_excel() method is used with the sheet_name parameter, for example: data.#to_excel('data.xlsx', sheet_name='Sheet2').