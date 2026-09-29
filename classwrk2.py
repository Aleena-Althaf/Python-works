#1
student_grades={'Alice':98,'Bob':85,'Charlie':74,'Mike':70}
s=student_grades['Charlie']
print(s)
student_grades['Bob']=90
print(student_grades)
student_grades['Sam']=75
print(student_grades)
print(student_grades.keys())
#*******************************************

#2
student_marks={'Arun':{'maths':30,'science':35,'english':40,'history':33},
               'Amal':{'maths':40,'science':45,'english':48,'history':43},
               'Anu':{'maths':45,'science':46,'english':47,'history':49}}
l=student_marks['Amal']
print(l)
student_marks['Arun']['maths']=35
print("updated marks of arun:",l)
print(student_marks.values())
