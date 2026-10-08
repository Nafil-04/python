# 1
my_dict={"name":"nik","age":20}
print(my_dict)

# 2
my_dict={"name":"nik","age":20}
print(my_dict["name"])

# 3
my_dict={"name":"nik" ,"age":20}
my_dict["city"]="delhi"
print(my_dict)

# 4
my_dict={"name":"nik","age":20,"city":"delhi"}
my_dict.update({"age":25})
print(my_dict)

# 5
my_dict={"name":"nik","age":20}
del my_dict["age"]
print(my_dict)

# 6
my_dict={"name":"nik","age":20}
print("email" in my_dict)

# 7
my_dict={"name":"nik","age":20}
print(my_dict.keys())

# 8
my_dict={"name":"nik","age":20}
print(my_dict.values())

# 9
my_dict={"a":1,"b":2}
print(list(my_dict.items()))

# 10
keys=["name","age"]
values= ["nik", 20]
print(dict(zip(keys,values)))

# 11
my_dict={"a":1, "b":2, "c":3 }
print(len(my_dict))

# 12
a={"a":1}
b={"b":2}
a.update(b)
print(a)

# 13
my_dict={"a":1,"b":2}
my_dict.clear()
print(my_dict)

# 14
my_dict={"x":10,"y":20}
copied=my_dict.copy()
print(copied)

# 15
my_dict={"name":"nik","age":20}
print(my_dict.get("salary"))

# 16
my_dict={"a":1,"b":2,"c":3}
print(my_dict.popitem())
print(my_dict)

# 17
student={"name":"rahul","marks":{"math":90,"science":85}}
print(student["marks"]["science"])

# 18
student["marks"]["maths"]=95
print(student)

# 19
student["marks"]["english"]=88
print(student)

# 20
del student["marks"]["science"]
print(student["marks"])