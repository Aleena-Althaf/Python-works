#1Given a string
#s="I am learning Python"

# find the length of the string
#
# find the reverse of the string

# find the last character of the strings
#find the 13th character
#print the characters from 2nd index to 15 th index
#combines the string s with word "programming"

# #2.Given a string s="python is a programming language"
# #Remove the first 10 characters and print the remaining
# #print the last 5 characters

#********************************
s="I am learning Python"
print(len(s))
#**********************************
l=s[::-1]
print(l)
#***********************************
m=s[17:20]
print(m)
#*******************************
n=s[12]
print(n)
#********************************
a=s[2:15]
print(a)
#********************************
b=s+' '+'programming'
print(b)
#******************************
s="python is a programming language"
a=s[10::]
print(a)
print(s[-5:: ])
