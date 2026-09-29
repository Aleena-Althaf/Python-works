# define  funcion to display your name
# def hello():
#     name=input("enter the name:")
#     print("hello",name)
#     return
# hello()
#*********************************************************
# #define a function to find the count of a specific character from a string
# def countchar():
#     n=input("enter the string:")
#     count=0
#     ch=input("enter the character:")
#     for i in n:
#         if (i==ch):
#             count+=1
#     print(count)
#     return
# countchar()
#*******************************************************
# #define a function to find the factorial of a number
# def fact():
#     n = int(input("enter the number:"))
#     fact = 1
#     i = 1
#     while i < n:
#         fact = fact * i
#         i += 1
#     print(fact)
#     return
# fact()
#**********************************************************
#define a function to find whether a number armstrong or not
# def armstrong():
#     n=int(input("enter the number:"))
#     s=str(n)
#     sum=0
#     l=len(s)
#     for i in s:
#         sum=sum+int(i)**l
#     if (sum==s):
#         print("armstrong ")
#     else:
#         print(" not armstrong")
#     return
# armstrong()
#**********************************************************
# #define a function to check whether a number is prime or not
# def prime():
#     n=int(input("enter the number:"))
#     if(n>1):
#         for i in range(2,n):
#             if n%i==0:
#                 print("not prime ")
#                 break
#         else:
#             print("prime number")
#         return
# prime()
#**************************************************************
#define a function to find the factors of a number
# def factors():
#     n=int(input('enter the number:'))
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
#     return
# factors()
#***********************************************************
#function to print the um of tw numbers
# def add(n1,n2):
#     s=n1+n2
#     print("sum:",s)
# add(23,24)
#***********************************************************
#define a function that takes 3 arguments and find the simple interest
# def interest(a,y,r):
#     s=(a*y*r)/100
#     print("simple interest is:",s)
#
# amount=int(input("enter the amount:"))
# year=int(input("enter the year:"))
# rate=int(input("enter the rate:"))
# interest(amount,year,rate)
#***********************************************************************
#define a function that take string and character as arguments and print the count  of characters in the string
# def countchar(s,ch):
#     count=0
#     for i in s:
#         if i==ch:
#             count+=1
#     print(count)
#     return
# string="ALEENA"
# character="A"
# countchar(string,character)
#*********************************************************************************
#sum of two numbers using return
# def add(n1,n2):
#     s=n1+n2
#     return s
# a=add(23,34)
# print("sum is:",a)
#*******************************************************************************
# define a function tht takes 3 numbers and return the product as the result call the the function and print the result
# def mult(n1,n2,n3):
#     p=n1*n2*n3
#     return p
#
# pro=mult(2,3,4)
# print("product:",pro)
#***********************************************************************************
#positional argument example:
# def fun(n,a):
#     print("name:",n)
#     print("age:",a)
#     return
# fun("arun",23)
# # fun(23)#error
# # fun(23,"arun")  #logical mistake
#***************************************************************
#keyword argument example:
# def fun(n,a):
#     print("name:",n)
#     print("age:",a)
#     return
# fun(n="Arun",a=23)
# fun(a=23,n="Arun")
#************************************************************
#default arguments example:
# def fun(n,a=24):
#     print("name:",n)
#     print("age:",a)
#     return
# fun(n="Arun")
# fun(a=23,n="Arun")
#***********************************************************
#variable length/ arbitary aguments
# def fun(a,b):
#     print(a,b)
# fun(10,20)
# fun(10,20,30) #error
       #or
# def fun(*args):                      }#*args
#     print(args)
# fun(10,20)
# fun(10,20,30)
#          #or
# def fun(**kwargs):                         }#**kwargs
#     print(kwargs)
# fun(a=10,b=20)
# fun(a=10,b=20,c=30)
#************************************************************************
#define a function to find the sum of numbers using arbitary positional arguments
# def add(*args):
#     sum=0
#     for i in args:
#          sum+=i
#     print(sum)
#
# add(2,3)
# add(2,3,4)
# add(10,20,30,40,50)
