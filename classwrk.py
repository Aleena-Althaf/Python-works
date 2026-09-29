# #2.Given a list
l=['Guitar','Piano','Violin','Drums','Flute']
#Add a new item 'Veena' to the list
l.append("veena")
print(l)
#**************************8
#3
f=['noodles','biriyani','shawarma','mandhi','porotta']
f.append('appam')
print(f)
f[1]='chapathi'
print(f)
print(f[-1])
print(len(f))
#********************************************
#5
l=[10,56,23,67,19,70]
l[2]=70
l[5]=23
print(l)
#***************************************
#6
from traceback import print_tb

s={10,20,30,40}
s.add(50)
print(s)