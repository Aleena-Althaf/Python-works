#map function
# l=[1,2,3,4]
# print(map(lambda x:x**2,l))
# print(list(map(lambda x:x**2,l)))
#**********************************************88
#reate a new list of cubes
# print(list(map(lambda x:x**3,l)))
#*****************************************************
#create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x:x**0.5,l )))
#*********************************************************
#create a new list of lengths
# colors=['red','green','blue','yellow','black']
#create a new list of first characters
# print(list(map(lambda x:x[0],colors)))
#*****************************************************
#create a new list of last characters
# print(list(map(lambda x:x[-1],colors)))
#*********************************************************
#create a new list of reverse of each elemnt
# print(list(map(lambda x:x[::-1],colors)))
#********************************************************
#Given a list
# l=[23,78,12,56]
#Add 10 to each element in the given sequence
# print(list(map(lambda x:x+10,l)))
#****************************************************
##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]

# # create a new list of emails
# print(list(map(lambda x:x["email"],l)))
#************************************************************
#filter function
# l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))
# print(list(filter(lambda x:x%5==0,l)))
#***************************************************
#given a list
# l=[23,65,89,12,20,33,85,40]
#filter the elements greatr than 50
# print(list(filter(lambda x:x>50,l)))
#filter the even elements less than 50
# print(list(filter(lambda x:x%2==0 and x<50,l)))
#***************************************************
#given a list
# l=['apple','orange','pineapple','grapes','avocado']
#filter elements whose length is greater than 5
# print(list(filter(lambda x:len(x)>5,l)))
#*****************************************************
#reduce functionEAW
# l=[1,2,3,4]
# #sum of list
# import functools
# print(functools.reduce(lambda a,b:a+b,l,0))     #0 is the initial value of sum=0
# #***********************************
# #product of list
# print(functools.reduce(lambda a,b:a*b,l,1))    #1 is the initial value for product=1
#************************************************************
