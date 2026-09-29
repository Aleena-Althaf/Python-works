# Q1.Define a function that takes 2 numbers and returns their product
# def mult(n1,n2):
#     prod=n1*n2
#     return prod
# a=5
# b=4
# p=mult(a,b)
# print("product:",p)

#**********************************************************************
# Q2.Define a function that takes a string and returns number of vowels
# def vowels():
#     count=0
#     for i in v:
#         if i in"AEIOUaeiou":
#             count+=1
#     return count
# v=input("enter the string:")
# s=vowels()
# print(s)
#************************************************************************
# # Q3.Define a function that takes length and breadth and returns area of rectangle
# def area(l,b):
#     ar=l*b
#     return ar
# l1=int(input("enter the length:"))
# b1=int(input("enter the breadth: "))
# a=area(l1,b1)
# print(a)
#*****************************************************************************
# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]
# def evenlist():
#     new=[i for i in l if i%2==0]
#     print(new)
#     return
# evenlist()
# #********************************************************************************
# # #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # # each value is the sum of digits of corresponding number in the original list.
# def sumlist():
#     l = [123, 345, 111, 678, 134, 809]
#     new=[]
#     for i in l:
#         sum=0
#     #i=0
#         while i>0:
#             d=i%10
#             sum=sum+d
#             i=i//10
#         new.append(sum)
#     # print(new)
#     return new
# s=sumlist()
# print(s)
#************************************************************
#Q6.Define a function that takes a list and returns a new list containing unique elemnets from the given
# list
# def uniquelst():
#     l = [12, 34, 78, 12, 67, 34, 90, 23]
#     new=[]
#     for i in l:
#         if i not in new:
#             new.append(i)
#     return new
# u=uniquelst()
# print(u)
#***************************************************************************
#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements
# l1=[12,34,56,78,90]
# l2=[90,34,11,57,45]
# def common(l1,l2):
#     new=[]
#     for i in l1:
#         for j in l2:
#             if i==j:
#                 new.append(i)
#     return new
# c=common(l1,l2)
# print(c)
#****************************************************************
#define a function that takes string as argument and return a new dictionary
#where keys are words and values are length of each word
#call th function nd print the dictionary
# def dictionary(s):
#     w= s.split()
#     new={i:len(i) for i in w}
#     return new
# n=input("enter the string:")
# di=dictionary(n)
# print(di)

#fibonacii
a=0
b=1
for  i in range(10):
    c=a+b
    a=b
    b=c
    print(a)