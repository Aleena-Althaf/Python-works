# x=20 #global
# print("outside",x)
#
# def f():
#     print("inside",x)
#
# f()
#
#
# #local
# def f():
#     x=20 #local
#     print("inside",x)
# f()
# print("otside",x)
#***************************
#non local
def outer():
    x=20 #non local

    def inner():
        y=30 #local
        print("inside inner functon",x)
    inner()
    print("inside outer function",x)
outer()

#LEGB ULE