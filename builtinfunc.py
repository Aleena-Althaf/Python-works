#write a program to find the position of a specific character in a string
# s="python is easy and fun"
# ch="i"
# if ch in s:
#     print("the position of",ch, "in",s,"is",s.index(ch))
# else:
#     print("the charcter",ch,"is not present")
#**********************************************************
#Write a program to find the count of a specific character in a string
# s="python is easy and fun"
# ch="a"
# if ch in s:
#     print("count of ",ch,":",s.count(ch))
# else:
#     print("character not present")
#**************************************************************
#write a program to create new dictionary where keys are letters and values
#are the count of each letter
# s="hello world"
# new={}
# new={i:s.count(i) for i in s}
# print(new)
#*******************************************************************************
#Write a program to create a new list with 5 random 3 digit numbers
# import random
# new=[]
# for i in range(1,6):
#     a=random.randint(100,999)
#     new.append(a)
# print(new)
#***********************************************************************
#write a program to create a 5 digit otp number
# import random
# for i in range(1,6):
#     a=random.randint(10000,99999)
#     print(a)
#********************************************************************
#write a program to find the count of letters,spaces and digits in a string
# s="python is easy and fun123"
# l=0
# d=0
# sp=0
# for i in s:
#     if i.isalpha():
#         l+=1
#     elif i.isdigit():
#         d+=1
#     else:
#         sp+=1
# print("letter count:",l)
# print("digit count:",d)
# print("space count:",sp)
##*******************************************************************************************
#given a list
# l=[1,1,2,3,4,5,5,5,6,7]
# #create a new dictionary where keys are number and values are coun of eaxh number
# new=[]
# for i in l:
#     new={i:l.count(i) for i in l}
# print(new)
#**************************************************************************
#given a list
# l=[34,12,56,89,90,11]
# #find the larges element
# #find the secon largest element
# #find the smallest element
# #find the second smallest element
# a=
# max(l)
# print(a)
# b=l.sort()
# print(l[-2])
# print(min(l))
# print(l[1])
#*****************************************
# l=[["arun",23,40000],
#    ["amal",24,340000],
#    ["anu",26,500000]]
#create a new list of salaries  and fnd the max f salaries same like find the min of age
# new=[]
# new=[i[2] for i in l]
# print(new)
# print(max(new))
# age=[]
# age=[i[1] for i in l]
# print(age)
# print(min(age))
#******************************************************************
 #define a function that takes list of functions as arguments and returns the count of even numbers odd numbers and numbers whose value greater than 50
# l=[23,56,12,78,98,89,31,67]
# def numcount(l):
#     eve = 0
#     odd = 0
#     gr = 0
#     for i in l:
#         if i %2==0:
#             eve=eve+1
#         elif i%2!=0:
#             odd+=1
#         if i>50:
#             gr+=1
#     print("count of even numbers:",eve)
#     print("count of odd numbers:",odd)
#     print("count of numbers greater than 50:",gr)
# numcount(l)
#**************************************************
#define a function that takes a list of words as arguments and return a new list of length
# l=["red","green","orange","yellow","blue"]
# def wordlen(l):
#     new=[]
#     new=[len(i) for i in l]
#     return new
# n=wordlen(l)
# print(n)
#*****************************************************************************
#user defined
#define a function that takes a number as rguments and retrn the its square
# def square(n):
#     a=n**2
#     return a
# n=int(input("enter the numbers:"))
# sq=square(n)
# print(sq)


