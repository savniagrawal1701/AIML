#PYTHON PROGRAMMING FOR ML (OOPS,BASICS)
print("hello world","hiii")
print("this will be printed to next line")
print(2+9)

#VARIABLES
a=10
b=10
print(a+b)

#type of variable
print(type(a))

#expression execution
A,B="2",3
txt="@"
print(2*txt*3)
print((A+txt)*B)

#operator precedence
print(a+b*B)

import math

#arthematic operations
# // ---->use to give only integer value of float output
# % ----->use to produce remainder
#Result of divisin operator will be float
a,b=10,20
d=-3
c=a/b
print(c)

#floor gives closest integer which is lesser or equal to the float value (we need to import maths)
print(a//b,math.floor(a/b))

#remainder is negative when denominator is negative
print(d%a)
print(a%d)


#Input in pyhton
a=int(input("enter a number 1 "))
b=float(input("enter a number 2 "))
name=input("enter your name ")
print(name)
print("Sum of the number is ",a+b)



#CONDITIONAL STATEMENT
# take care of intendation and :
a=int(input("enter a number 1 "))
b=int(input("enter a number 2 "))
if(a>b):
  print("a is greater")
else:
  print("b is greater")

#single line conditional statement
#1.<var>=<val> if <condition> else <val2>
food=input(" FOOD ")
eat="yes" if food=="rice" else "no"
print(eat)
#2<st1> if <condition> else <st2>
print ("sweet") if food=="cake" or food=="toffee" else print("not sweet")
#3.clever if
#(<var>=(false_val,true_val) [condition]
A=int(input("Entre your age"))
vote="yes" if A>=18 else "no"
print(vote)



#STRINGS
str1="This is a string "
str2="Hello world"
#concatenation
str3=str1+str2
print(str3)
#Lenght of string
print(len(str3))

#slicing
print(str2[1:4])
print(str2[5:]) #5 to end
print(str2[:5]) #start to 5
print(str2[-3:-1])


#LISTS
#list can store multiple datatype,is mutable
#defined using square brackets
list=[8,2,3,9,0,1,5,6]
#properties are same as string

#methods applied directly to a list object can modify the original list in place.
# METHODS
list.append(7)
print(list)

list.sort()
print(list)

list.reverse()
print(list)

list.remove(2)
print(list)

list.pop(3)
print(list)




#TUPLE
#Tuples are immutable
#defined using parenthesis
tup=(1,2,2,3,5,8)

print(tup.index(2))
print(tup.count(2))



#DICTONARY AND SET
#dictonary store data in key value pairs
#unordered,mutable and dont allow duplicates
dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
dict1 = {
    "marks":99
}

# Adding or updating a key-value pair
dict["occupation"] = "Engineer"
print(dict)

#dictonary methods
print(dict.keys())
print(dict.values())
print(dict.items())

dict.update(dict1)
print(dict)



#NESTED DICTONARY
student_data = {
    "student1": {
        "name": "Alice",
        "age": 18,
        "courses": {
            "math": "A",
            "science": "B"
        }
    }
    }


print(student_data["student1"]["name"])
print(student_data["student1"]["courses"]["math"])



#SETS
#collection of umordered items...each element in set is immutable and unique
set1={1,3,4,8,9,9,0,0}
set2={1,3,4,8,9,9,0,0}
print(set1)

#cannot store list and dict as they are mutable

#lenght of set
print(len(set2))

#set methods
set1.add(6)
print(set1)

set1.remove(1)
print(set1)

set1.pop()
print(set1)

print(set1.union(set2))

print(set1.intersection(set2))



#range done
#loops done
#Functions in python

#agar parameters hai toh return karvana padega
def add_numbers(a,b):
    s=a+b
    return s
print(add_numbers(2,3))

def print1():
    print("hii")

print1()

#default parameters
def prod(a=2,b=2):
  print(a*b)
  return
prod(2,3)
prod(2)



#RECURSION
def factorial(n):
  if(n==0 or n==1):
    return 1
  else:
    return n*factorial(n-1)
print(factorial(3))



#OOPS
#maing a bsic class
class student1:
  name="katran"

s1=student1()
print(s1.name)

#MAKING A CONSTRUCTOR
#self argument jaisa pass karna he hai kuch bhee ho jaaye if y ou are making a constructor
class student:
  #parametrise

  def __init__(self,name="om",age=0):
    self.name=name
    self.age=age
    #self will always be written in methods
  def welcome(self):
    print("my name is ",self.name)

s2=student("kj",99)
s3=student()
print(s2.name,s2.age)
print(s3.name,s3.age)
print(s2.welcome())

