#program to display a number(dynamic)
# a=int(input("enter a number:"))
# if a>=0:
#     print(a ,"is a positive")
# else:
#     print(a,"is a negative number")
#*****************************************
#program to print odd or even number
# a=int(input("enter the number:"))
# if(a%2==0):
#     print(a,"is an even number")
# else:
#     print(a,"is an odd number")
#***********************************************
 #program to print a number if it is divisible by 3
# n=int(input("enter the number:"))
# if(n%3==0):
#     print(n,"is divisible by 3")
# else:
#     print(n,"is not divisible by 3")
#************************************************
#program to display the number if it is divisible by 5 and 7
# num=int(input("enter the number:"))
# if (num%5==0 and num%7==0):
#     print(num)
#***********************************************
#program to display a name if name contain a letter 'n'
# name=input("enter the name:")
# if ('n'in name):
#     print("n is present in",name)
#********************************************
#program to display a name if name starts with the letter 'A'
# name=input("enter the name:")
# if(name[0]=='A'):
#     print(name)
#**************************************************
#program to check if a number is positive or negtive
#a=int(input("enter the number:"))
# if(a>=0):
#     print(" number is positive number")
# else:
#     print(" number is negative number")
#***************************************************************
#program to display whether the number si odd or even
# a=int(input("enter the  number:"))
# if (a%2==0):
#     print(f"{a} is even")
# else:
#     print(f"{n}is odd")
#******************************************************************
#program to check whether the two numbers are equal or not
# a=int(input("enter the number1:"))
# b=int(input("enter the number2:"))
# if(a==b):
#     print(a,"and",b,"are equal")
# else:
#     print(a,"and",b,"are not equal")
#*****************************************************************
#program to check whether the two wods are equal or not
# a=input("enter the word1:")
# b=input("enter the word2:")
# if (a==b):
#     print("two words are equal")
# else:
#     print("two words are not equal")
#*****************************************************************
#program to find the maximum off two numbers
# a=int(input("enter the number1:"))
# b=int(input("enter the number2:"))
# if(a>b):
#     print(a,"is the greater number")
# else:
#     print(b,"is the greater number")
#********************************************************************
# program to check whether the entered character is a vowel or not
# a=input("enter the string:")
# if (a in ("A","E","I","O","U","a","e","i","o","u")):
#     print(a,"is a vowel")
# else:
#     print(a,"is not a vowel")
#************************************************************************
#program to che whether the enterd country name is contains 'land'
# a=input("enter the country name:")
# if ('land' in a):
#     print(a,"contains the word land")
# else:
#     print(a,"  not contains the word land")
#*******************************************************************
#program to check whether te number is  three digit number or not
# a=int(input("enter the number:"))
# if(a<999 and a>=100):
#     print(a,"is a three digit number")
# else:
#     print(a,"is not a three digit number")
#*******************************************************************
#program to check whether a string is a palidrome or not
# a=input("enter the string:")
# b=a[::-1]
# if(a==b):
#     print(a,"is a palindrome")
# else:
#     print(a,"is not a palindrome")
#*********************************************************************
#program to check whether a number is present in a given list
# l=[23,34,45,56,67,78]
# a=int(input("enter the number:"))
# if a in l:
#     print(a,"is present in l")
# else:
#     print(a,"is not present in l")
#********************************************************************
#program to check whether  key is present in dictionary or not
# a=input("enter the key:")
# d={'101':'Arun',102:'Amal',103:'Anu'}
# if a in d:
#     print("key is present")
# else:
#     print("key is not present")
#****************************************************************
#program to check whetherthe password is strong or weak less that length 8
# a=input("enter the password:")
# if (len(a)<8):
#     print("password is weak")
# else:
#     print("password is strong")
#******************************************************************
#program to heck whether a number is positive negative or zero
# n=int(input("enter a number:"))
# if (n==0):
#     print("the number is 0")
# elif  n>0:
#     print("the number is positive")
# else:
#     print("the number is negative")
#**********************************************************
#program to print the greatest of 3 numbers
# a=int(input("enter the num1:"))
# b=int(input("enter the num2:"))
# c=int(input("enter the num3:"))
# if (a>b and a>c):
#     print(a,"is the greatest number")
# elif (b>a and b>c):
#     print(b,"is the greatest number" )
# else:
#     print(c,"is the greatest number")
#***********************************************************************
#program to calculate the electricity bill based on the criteria
# amnt=int(input("enter the amount:"))
# bill=0
# if (amnt<=100):
#     bill=0
# elif (amnt>100 and amnt<=200):
#     bill=0+(amnt-100)*5
# elif (amnt>200 and amnt<=300):
#     bill=0+500+(amnt-200)*10
# else:
#     bill=0+500+1000+(amnt-300)*15
# print(bill)
#*****************************************************************
# #program to check whether the user entered a 2digit/3digit ro 4digit number
# num=int(input("enter the number:"))
# if (num<=99 and num>=10):
#     print(num,"is a 2digit number")
# elif (num<=999 and num>=100):
#     print(num,"is a 3 digit number")
# elif num<=9999 and num>=1000:
#     print(num,"is a 4 digit number")
# else:
#     print("the number is a invalid number")
#*******************************************************************************
#write a basic calculator program to do all the arithmatic operations
# a=int(input("enter the num1:"))
# b=int(input("enter the num2:"))
# o=input("enter the operator:")
# if o=="+":
#     print(a+b)
# elif o=='-':
#     print(a-b)
# elif o=='*':
#     print(a*b)
# elif o=='/':
#     print(a/b)
# elif o=="//":
#     print(a//b)
# elif o=="%":
#     print(a%b)
# else:
#     print("invalid operator")
#************************************************************************
#program to print the number of days in a month
# l1=["january","march","may","july","august","october","december"]
# l2=["april","june","september","november"]
# l3=["february"]
# m=input("enter the month:")
# if (m in l1):
#     print("the number of days are 31")
# elif (m in l2):
#     print("the number days are 30")
# else:
#     print("the number of days are 28 or 29")
#************************************************************************
#program to print the grades based on the following
#91-100  grade A     81-90 grade B       71-80   grade C
#61-70 grade D    below61 grade E
# m=int(input("enter the marks:"))
# if (m<=100 and m>=91):
#     print("grade A")
# elif (m<=90 and m>=81):
#     print("grade B")
# elif(m<= and m>=80):
#     print("grade C")
# elif (m<=61 and m>=70):
#     print("grade D")
# else:
#     print("grade E")
#************************************************************************
#program to check whether a number is positive odd/even or negative even/odd
# num=int(input("enter the number:"))
# if(num>0):
#     if(num%2==0):
#         print("positive even number")
#     else:
#         print("positive odd number")
# else:
#     if(num%2==0):
#         print("negative even number")
#     else:
#         print("negative odd number")
#***********************************************************************
# program to check whether a number is divisible by 2 and 3
# divisible by 2 and not by 3
#divisible 3 and not by 2
# not divisible by 2 and 3
# num=int(input("enter the number:"))
# if (num%2==0):
#     print(num,"is divisible by 2")
#     if(num%3==0):
#         print(num,"is divisible by 3")
#     else:
#         print(num,"is not divisible by 3")
# else:
#     print(num,"is not divisible by 2")
#     if (num%3==0):
#         print(num,"is divisible by 3")
#     else:
#         print(num,"is not divisible by 3")
#****************************************************************
