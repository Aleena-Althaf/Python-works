#sum of digits in a number
# n=int(input("enter the number:"))  #145
# sum=0                              #1+4+5
# while n>0:                          #145>0
#     d=n%10                          #d=145%10=5    ie;d=5
#     sum=sum+d                        #sum=0+5
#     n=n//10     #incrementation takes place here       #n=145//10 14
# print(sum)
#***************************************************************************8
#check whether a number is armstrong or not
# n=int(input("enter the number:"))
# sum=0
# s=str(n)
# l=len(s)
# for i in s:
#     sum=sum+int(i)**l
# if (sum==n):
#     print(n,"is an armstrong number")
# else:
#     print(n,"is not an armstrong number")

#******************************************************************
#check whether a number s prime or not
# n=int(input("enter the number:"))
# if (n>1):
#     for i in range(2, n):
#         if n % i == 0:
#             print("non prime")
#             break
#     else:
#         print("prime number")
# else:
#     print("number is neither prime nor composite")

#*******************************************************
# #given list print the prime numbers
# l=[23,65,42,80,56,41]
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             #print("not prime")
#             break
#     else:
#         print(i)
# print()
#*******************************************************
#print all prime numbers in range(1,100)
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=" ")
# print()
#*******************************************************
#print all armstrong numbers in the range(100,1000)
# for i in range(100,1001):
#     sum=0
#     s=str(i)
#     l=len(s)
#     for j in s:
#         sum=sum+int(j)**l
#     if sum==i:
#         print(i)
# print()
