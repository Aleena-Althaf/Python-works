#print all 3 digit numbers using while loop
# i=100
# while i<=999:
#     print(i,end=" ")
#     i+=1
#****************************************************
#using for loop
# for i in range(100,1000):
#     print(i,end=" ")
#************************************************
colors=['red','green','yellow','blue','orange','black']
# #print each color
# for i in colors:
#     print(i)
#*********************************************
#color contains 'b'
# for i in colors:
#     if 'b' in i:
#         print(i)
#****************************************
#startig with letter g
# for i in colors:
#     if i[0]=='g':
#         print(i)
#***************************
#end with 'e'
# for i in colors:
#     if i[-1]=='e':
#         print(i)
#***************************************
# #colors except colors starting with 'b'
# for i in colors:
#     if i[0]=='b':
#         continue
#     print(i)
#***************************************
l=[23,45,12,78,90,51,75]
#print all numbers
# for i in l:
#     print(i)
#**************************************
#print all even numbers
# for i in l:
#     if i%2==0:
#         print(i)
#***************************************
#print those numbers that are divisible by 5
# for i in l:
#     if i%5==0:
#         print(i)
#*****************************************
#stop the loop if i>50
# for i in l:
#     if i>50:
#         break
#     print(i)
#*******************************************
# #skip all even numbers
# for i in l:
#     if i%2==0:
#         continue
#     print(i)
#************************************
#print the first even number whose value is greater than 50
# for i in l:
#     if i%2==0 and i>50:
#         print(i)
#         break
#****************************************************
#count of all even numbers
# count=0
# for i in l:
#     if i%2==0:
#         count += 1
# print(count)
#*****************************************
#sum of list
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)
#*****************************************
#product of odd numbers
# p=1
# for i in l:
#     if i%2!=0:
#         p=p*i
# print(p)
#****************************************
#print each digit in a number
# n=234
# s=str(n)
# for i in s:
#     print(i)
# #*****************************************************
#print the sum of digits using for loop
#n=int(input("enter the number:"))
# s=str(n)
# sum=0
# for i in s:
#     sum=sum+int(i)
# print(sum)
#************************************************
#using while loopp
# n=int(input("enter the number:"))
# sum=0
# while n>0:
#     d=n%10
#     sum=sum+d
#     n=n//10
# print(sum)
#******************************************
#factors of a number
# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)
#******************************************
# l=[1,2,3,4,5]
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)
#********************************************
# l=[1,2,3,4,5]
# new=set()
# for i in l:
#     new.add(i**2)
# print(new)
#******************************
# l=[1,2,3,4]
# sum=0
# new=[]
# for i in l:
#     sum=sum+i
#     new.append(sum)
# print(new)
#*************************
# l=[10,20,30,40]
# sum=0
# for i in range(0,len(l),2):
#     sum=sum+l[i]
# print(sum)
#****************************************
#for --else
# for i in range(1,6):
#     print(i)
# else:
#     print("hello")

# for i in range(1,5):
#     if(i==4):
#         break
#     print(i)
# else:
#     pint("hello")
#***********************************
#while --else
i=0
while i<6:
    print(i)
    i+=1
else:
    print("hello")