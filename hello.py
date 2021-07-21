# print("hello world")
# # integer
# a=2
# print(a)
# b=9223720936737
# print(b)
# # Floating point
# pi = 3.14
# print(pi)
# # string
# c = "a"
# print(c)
# name = "john Doe"
# print(name)
# #boolean
# q = True
# print(q)
# # Null data type
# x = None
# print(x)
# a = 2
# # type
# print(type(a))
# # assigning multiple variables to multiple value
# a,b,c = 1,2,3
# print(a,b,c)
# a=b=c=True
# print(a,b,c)
# b=2
# print(a,b,c)
# x=y=[7,8,9]
# print(x,y)
# x=[13,8,9]
# print(y)
# # nested list
# x=[1,2,[3,4,5],6,7]
# print(x[2][1])
# # blocks and identation
# def myfunction():
#     a=2
#     return a
# print(myfunction())

# if a > b:
#     print(a)
# else:
#     print(b)

# a =reversed('hello')
# print(a)
# a = None
# print(a)

# # to test if something is of a nonetype
# x = None
# if x is None:
#     print("not a suprise")
# # converting between datatypes
# a ="123"
# b=int(a)
# print(b)
# print(a)

# m="123.456"
# n = float(m)
# # o=int(m)
# p=int(n)
# print(p)

# a = "hello"
# print(tuple(a))

names=["Alice","Bob","craig","Diana","Eric"]
# print(names[0])
# print(names[2])
# print(names[-1])
# print(names[-3])
# names[3] = "Amanda"
# print(names)
# names.insert(-1,"James")
# print(names[-1])
# # names.append('Faridah')
# print(names)
# names.insert(-1, "Evans")
# print(names)
# names.remove("craig")
# print(names)
# len(names)
# print(len(names))
# print(len([2]))
# names.insert(-1,"James")
# print(names)
# print(names.count("James"))
# # names.reverse()
# # print(names)
# names.pop()
# print(names)
# first_names = {'Adam', 'Beth', 'Charlie'}

# # name=input("what is ur name?")
# # print(name)
# # x=input('write a number')
# # print(float(x)/2)
    
# import math
# print(math.sqrt(16))
# print(dir(math))
# print(math.log2(20))
# s="""wow"""
# print(repr(s))
# print(str(s))
# # print(eval(str(s)))
# print(eval(repr(s)))

# import datetime
# today = datetime.datetime.now()
# print(str(today))
# print(repr(today))

# def stutter(word):
#     space=" "
#     ellipsis="..."
#     stut=word[0:2]+ellipsis+space+word[0:2]+ellipsis+space+word+"?"
#     return stut
# print(stutter("mother"))

# def stutter2(word):
#     return f'{word[0:2]}... {word[0:2]}... {word}?'

# print(stutter2("brother"))
# # print(help(help))
# import math
# print(help(math))
# a = "hello world"
# print(a)
# print(a[0])
# print(a[0:5])
# b = frozenset("asdfagsa")
# print(b)
# cities =frozenset(["Frankfurt","Basel","Freiburg"])
# print(cities)
# # print(cities.add("Accra"))
# list =["bread","drink",32,"gari"]
# print(list*2)
# def func():
#     """This is a function that does nothing"""
#     return
# print(func.__doc__)
# print(help(func))

# intersection
a ={1,2,3,4,5,}
b ={3,4,5,6}
# print(a.intersection(b))
# print(a&b)
# print(a|b)
# print(a-b)
# print(a^b)
# print(a>=b)
def couson(num):
    if (2**num + 1)&(2*num+1):
        return True
    else:
        return False
print(couson(33))
    
        