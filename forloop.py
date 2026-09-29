#program to print hello
# s="hello"
# for i in s:                                 }takes the index of the string
#     print(i,end=" ")
#*******************************************
#list
# l=[1,2,3,4,5]
# for i in l:
#     print(i)
#*************************************
#tuple
# t=(1,2,3,4)
# for i in t:
#     print(i)
#***********************************
#set
# s={1,2,3,4,5,6}
# for i in s:
#     if i%2==0:
#         print(i)
#
#********************************************
#print each colors in the ist
# colors=['blue','red','yellow','green']
# for i in colors:
#     print(i)
#***************************************
#print each numbers i the tuple
# t=[23,45,65,89,12]
# for i in t:
#     print(i)
#**************************************
#print the dictionary key value pairs
d={1:'a',2:'b',3:'c',4:'d'}
for i in d:
    print(i,':',d[i])
#**************************************
#print the sum of each numbers in the list
# l=[89,56,34,10]
# sum=0
# for i in l:
#     sum=sum+i
#     i+=1
# print(sum)
#***************************************
#reverse without using slicing
# s="hello"
# rev=""
# for i in s:
#     rev=i+rev  (#-->reverse ie;olleh       #rev=rev+i ->same order ie;hello)
# print(rev)
# if s==rev:
#     print("pal")
# else:
#     print("no pal")
#****************************************
#reverse of a number
# n=1034
# rev=""
# s=str(n)
# for i in s:
#     rev=i+rev
# print(rev)
# if s==rev:
#     print("palindrome")
# else:
#     print("not palindrome")
#********************************************
#print each number in a list
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     print(i)
#*********************************************
#print even values
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if i%2==0:
#         print(i)
#***********************************************
#print those numbers that are divisible by 5
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if (i%5==0):
#         print(i)
#***********************************************
#print those numbers that contains digit '3'
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     if '3' in str(i):
#         print(i)
#*************************************************
#sum of list
# l=[12,34,56,45,89,16,69,33]
# s=0
# for i in l:
#     s=s+i
# print(s)
#***********************************************
#count of even numbers in a list
# l=[12,34,56,45,89,16,69,33]
# count=0
# for i in l:
#     if i%2==0:
#         count+=1
#     i+=1
# print(count)
#**************************************************
#product of list
# l=[12,34,56,45,89,16,69,33]
# p=1
# for i in l:
#     p=p*i
#     i+=1
# print(p)
#*******************************************************
#print squares of each number
# l=[12,34,56,45,89,16,69,33]
# for i in l:
#     print(i**2)
#*********************************************************
#print only float point values
# l=[12,4.5,6.8,30,'arun','hello']
# for i in l:
#     if type(i)==float:                  #imp
#         print(i)
#*************************************************
#print only strings
# l=[12,4.5,6.8,30,'arun','hello']
# for i in l:
#     if type(i)==str:
#         print(i)
#************************************************
# d={'a':23,'b':25,'c':28,'d':'30','e':22}
# for i in d.values():
#     if int(i)%2==0:
#         print(i)
#**************************************************8
