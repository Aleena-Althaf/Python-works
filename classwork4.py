#1.program tp find the BMI (BMI= weight in (kg)/ height**2 in (m)
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese
# w=float(input("enter the weight:"))
# if(w>=40):
#     print("status:Obese")
# elif(w<=39.9 and w>=25.0):
#     print("status:Overweight")
# elif(w<=24.9 and w>=18.5):
#     print("status:Normal")
# elif(w<=18.4):
#     print("status:Underweight")
# else:
#     print("invalid weight")
#**********************************************************************
#2 Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.
# pc=int(input("enter the code:"))
# amnt=int(input("enter the amount:"))
# discount=0
# if(pc==1):
#     if amnt>1000:
#         discout=amnt*0.10
# elif (pc==2):
#     if amnt>100:
#         discount=amnt*0.05
# elif (pc==3):
#     if(amnt>500):
#         discount=amnt*0.10
# else:
#     print("invalid code")
# total_amnt=amnt-discount
# print("amnt t be paid:",total_amnt)
#*********************************************************************
#3 FIZZBUZZ PRoblem
# n=int(input("enter the number:"))
# if(n%3==0 and n%5==0):
#     print('fizzbuzz')
# elif(n%5==0):
#     print("buzz")
# elif(n%3==0):
#     print("fizz")
# else:
#     print(n)
