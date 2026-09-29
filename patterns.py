# * * * *
# * * * *
# * * * *
# for i in range(1,4):
#     for j in range(1,5):
#         print("*",end=" ")
#     print()
#****************************************
#  *
#  * *
#  * * *
#  * * * *
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

#**********************************
# 2 2 2 2
# 4 4 4 4
# 6 6 6 6
# 8 8 8 8
# for i in range(2,9,2):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()

#********************************
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#*************************************
# * * * *
# * * *
# * *
# *
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
#*****************************************
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
#**********************************
# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4
# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(i,end=" ")
#         else:
#             print("0",end=" ")
#     print()
#**************************************
# 1
# 1 0
# 1 0 1
# 1 0 1 0
# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2==0:
#             print("0",end=" ")
#         else:
#             print("1",end=" ")
#     print()
#***********************************
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# num=0
# for i in range(1,5):
#     for j in range(1,i+1):
#         num+=1
#         print(num,end=" ")
#
#     print()

#*******************************************
# 1
# 4 9
# 16 25 36
# 49 64 81 100
# num=0
# for i in range(1,5):
#     for j in range(1,i+1):
#         num+=1
#         print(num,end=" ")
#     print()
#*********************************************
# *
# ***
# *****
# *******
# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
#**************************************************
# for i in range(2,9,2):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
#*************************************************
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# #*************************************************
# 1
# 3 5
# 7 9 11
# 13 15 17 19
# num=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num+=2
#     print()
#**************************************************
#hollow square
# * * * * * *
# *         *
# *         *
# *         *
# *         *
# * * * * * *

# n=int(input("enter the number:"))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
#*************************************************
# A
# B C
# D E F
# G H I J
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()

#****************************************
# A
# B B
# C C C
# D D D D
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k+=1
#     print()
#**********************************************
# A
# A B
# A B C
# A B C D
# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k+=1
#     print()
#************************************************
#       *
#     * *
#   * * *
# * * * *
# sp=3*2          #space
# for i in range(1,5):
#     for s in range(1,sp+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print('*',end=" ")
#     sp-=2
#     print()
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# kw=4*2
# for i in range(1,6):
#     for p in range(1,sp+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     sp-=2
#     print()
#************************************************
# *
# * *
# * * *
# * * * * 
# * * *
# * *
# *
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for k in range(3,0,-1):
#     for g in range(1,k+1):
#         print("*",end=" ")
#     print()
#******************************************
#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *

# sp=3*2
# for i in range(1,5):
#     for s in range(1,sp+1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print("*",end=" ")
#     sp-=2
#     print()
# sp=1*2
# for k in range(3,0,-1):
#     for p in range(1,sp+1):
#         print(end=" ")
#     for l in range(1,k+1):
#         print("*",end=" ")
#     sp+=2
#     print()
#************************************************
#      *
#     *   *
#   *   *   *
# *   *   *   *
#   *   *   *
#     *   *
#       *



sp=3*2
for i in range(1,5):
    for s in range(1,sp+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end="   ")
    sp-=2
    print()
sp=1*2
for k in range(3,0,-1):
    for p in range(1,sp+1):
        print(end=" ")
    for l in range(1,k+1):
        print("*",end="   ")
    sp+=2
    print()
#*****************************************
# E
# D D
# C C C
# B B B B
# A A A A A
# k=ord('E')
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k-=1
#     print()
#***************************************
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
#***************************************
# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(6-i,end=" ")
#     print()



