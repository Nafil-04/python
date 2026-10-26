# opening & reading a file
# a=open("sample.txt","r")
# file=a.read()
# print(file)
# a.close()

# readline method
# a=open("sample.txt","r")
# file=a.readline()
# print(file)
# a.close

# readlines method
# a=open ("sample.txt","r")
# file=a.readlines()
# print(file)
# a.close

# writing on files
# a=open("sample.txt","w")
# a.write("hello world")
# a.close

# writelines
# a=open("sample.txt","w")
# lines=["hello\n","welcome\n","python\n"]
# a.writelines(lines)
# a.close()

# appending data
# a=open("sample.txt","a")
# a.write("nafil\n")
# a.close()

# with statement
# with open ("sample.txt","r") as file:
#     content=file.read()
#     print(content)

# tell and seek
# a=open("sample.txt","r")
# file=a.read()
# Position=a.tell()
# a.seek(2)
# print(a.read())
# a.close()

# common python errors

#zerodivision

a=10
b=0                
try:
    print(a/b)  
    x=10/0
except ZeroDivisionError:
    print("cannot divide by zero")
    

#type error


try:
    a=[list]+str
    print(a)
except TypeError:
    print("error")

#value error
try:
    a=int("hello")
    print(a)
except ValueError:
    print("invalid value given")


#index error
try:
    my_list=['a','b']          
    print(my_list[3])
except IndexError:
    print("index not found")

#key error
try:
    my_dict={"name":"nafil"}   
    print(my_dict["place"])
except KeyError:
    print("invalid key entered")

# file not found error
try:
    a=open("samm.txt")
except FileNotFoundError:
    print("no such file")