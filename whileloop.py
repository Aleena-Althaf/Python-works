#1.write a program to print first ten integers
# i=1
# while i<=10:
#     print(i,end=" ")
#     i+=1
#*************************************************************
#2.program to print frst 10 even numbers
# i=2
# while i<=20:
#     if i%2==0:
#         print(i,end=" ")
#     i+=1
#**************************************************************
#3.program to print first 10 odd numbers
# i=1
# while i<=19:
#     if i%2!=0:
#         print(i,end=" ")
#     i+=1
#*************************************************************
#4.print 1 4 7 10 13 16
# i=1
# while i<=16:
#     print(i,end=" ")
#     i+=3
#**********************************************************
#5.print 10 20 30 40 50 60 70 80
# i=10
# while i<=80:
#     print(i,end=" ")
#     i+=10
#*********************************************************
#6.print series 3 6 9 12 15 18 21
# i=3
# while i<=21:
#     if i%3==0:
#         print(i,end=" ")
#     i+=1
#*******************************************************
#7.print series 5 4 3 2 1
# i=5
# while i>=1:
#     print(i,end=" ")
#     i-=1
#*************************************************
#8.print 8 6 4 2 0
# i=8
# while i>=0:
#     print(i,end=" ")
#     i-=2
#****************************************************
#9.print 100,101,102,103......200
# i=101
# while i<=200:
#     print(i,end=",")
#     i+=1
#**************************************************************
#10.print all 4 digit numbers (1000-9999)
# i=1000
# while i<=9999:
#     print(i, end=" ")
#     i+=1
#************************************************************
#11.print those 3 digits numbers that are divsile by 3
# i=100
# while i<=999:
#     if i%3==0:
#         print(i,end=" ")
#     i+=1
#****************************************************************
#12.print all 4 digit numbers that contains 3
# i=1000
# while i<=9999:
#     s=str(i)
#     if '3' in s:
#         print(int(s),end=" ")
#     i+=1
#***********************************************************
#13.print all  numbers tht are divisible are 3 and 5 in the range(1,100)
# i=1
# while i<=100:
#     if (i%3==0 and i%5==0):
#         print(i ,end=" ")
#     i+=1
#************************************************************
#14.print 1 4 9 16 25 36 49 64 81 100
# i=1
# while i<=10:
#     print(i**2,end=" ")
#     i+=1
#*************************************************************
#15.count those 3 digit numbers that contains a 3
# count=0
# i=100
# while i<=999:
#     s=str(i)
#     if '3' in s:
#         count=count+1
#     i+=1
# print(count)
#************************************************************
#program to count of  numbers that are divisible by 7 or 3 in the range of 200 to 300
# count=0
# i=200
# while i<=300:
#     if (i%3==0 or i%7==0):
#         count=count+1
#     i+=1
# print(count)
#******************************************************8
#count of odd numbers that are divisible by 5 in the range of (1,100)
# count=0
# i=1
# while i<=100:
#     if(i%2!=0):
#         if(i%5==0):
#             #print(i)
#             count=count+1
#     i+=1
# print(count)
#******************************************************
#count of all palindrome numbers in the range (1,1000)
# count=0
# i=1
# while i<=1000:
#     s=str(i)
#     if(s[::-1]==s):
#         #print(s)
#         count=count+1
#     i+=1
# print(count)
#***************************************************
#count of numbers divisible by 3 in rage of(1,50)
# count=0
# i=1
# while i<=50:
#     if (i%3==0):
#         #print(i)
#         count=count+1
#     i+=1
# print(count)
#**********************************************************
#SUM
#find the sum of first five numbers
# s=0
# i=1
# while i<=5:
#     s=s+i
#     i+=1
# print(s)
#***********************************************************
#sum of those numbers that are divisible by 3 in range(1,50)
# s=0
# i=1
# while i<=50:
#     if (i%3==0):
#         s+=i
#     i+=1
# print(s)
#******************************************************************
#sum of all 3 digit numbers
# s=0
# i=100
# while i<=999:
#     s+=i
#     i+=1
# print(s)
#****************************************************************8
#sum of fist 10 even numbers
# s=0
# i=2
# while i<=20:
#     #if(i%2==0):
#     s+=i
#     i+=2
# print(s)
#**********************************************************************
#PRODUCT
# p=1
# i=1
# while i<=5:
#     p=p*i
#     i+=1
# print(p)
#*********************************************************
#product of first 10 odd numbers
# p=1
# i=1
# while i<=19:
#     p*=i
#     i+=2
# print(p)
#*****************************************************
#product of numbers that contain  digit '3' in the range(1,50)
# p=1
# i=1
# while i<=50:
#     s=str(i)                     }or if '3' in str(i)
#     if '3' in s:
#         p*=i
#     i+=1
# print(p)
#************************************************
#factorial of a number entered by user
# n=int(input("enter the number:"))
# fact=1
# i=1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)
#*************************************************************
#multiplication table of a number till 10
# p=1
# i=1
# n=int(input("enter the number to print the multiplication table:"))
# while i<=10:
#     p=i*n
#     print(i,'x',n,'=',p)
#     i+=1
#*****************************************************************



