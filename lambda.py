#lambda function
# s=lambda n:n**2
# print(s(5))
# s=lambda n:n**3
# print(s(5))
#***************************************************************************************
#sum of two numbers
s=lambda n,d:n+d
print(s(12,23))

# #product of 3 numbers
s=lambda a,b,c:a*b*c
print(s(12,3,4))

# #length of a string
s=lambda n:len(n)
print(s("python"))

#square root of a number
s=lambda n:n**0.5
print(s(64))

#first letter of a string
s=lambda n:n[0]
print(s("python"))

#last letter of string
s=lambda n:n[-1]
print(s("python"))

#name value  from dictionary
n={"name":"anu","salary":50000}
s=lambda n:n["name"]
print(s(n))

#salary value from diionary
n={"name":"anu","salary":50000}
s=lambda n:n["salary"]
print(s(n))
s=lambda n:n["salary"]

#add 10 to a number
s=lambda n:n+10
print(s(12))

s=lambda n:n+10
print(s(20))