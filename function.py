# function definition
# def greet():
#     print("hello world")

# function call
# greet()

# def greet(name):
#     print(f"hello, {name}!")

# greet("judith")
# greet("rick")

# def greet(name,age,place):
#         print(f"hello, {name} from {place}, you are {age} years old")

# greet("judith",12,"Commom Wealth")
# greet("rick",55,"Unknown")

# type of arguments
# positional argument
# def add(a,b):
#     print(a)
#     print(b)
# add(20,30)

# keyword arguments
# def greet(name,age,place):
#     print(f"Hello {name} your age is {age} and your place is {place}")
# greet(age=22,name="rui",place="portugal")

# # default arguments
# def numbers(*a):
#     print(a)

# numbers(1,2,3,4,5,6,7,8,9,10)

# arbitary keyword arguments
# def details (**a):
#     print(a)
# details(name="rick",age=66,place="texas",country="U.S.A")

# return statement
# def multiply(a,b):
#     return a* b
# result=multiply(4,5)
# print(result)

# docstrings in function
# def add(a,b):
#     """this function adds two numbers"""
#     return a+b
# print(add.__doc__)

# lambda function 
# add = lambda a,b : a+b
# print(add(3,5))

# lambda functions with map()
# num=[1,2,3,4,5]
# square=map(lambda x:x ** 2, num)
# print(list(square))

# # lambda filter()
# num=[1,2,3,4,5,6,7,8,9,10]
# even=filter(lambda x:x % 2 == 0,num)
# print(list(even))

# lambda reduce()
# from functools import reduce
# num=[1,2,3,4]
# sum_result=reduce(lambda x,y:x+y,num)
# print(sum_result)

# function scope
a=10 #global function

def greet():
    a=15 #enclosing function
    def greet1():
        x=20 #local function
        print(a)
    
    greet1()
    
greet()
print(a)
