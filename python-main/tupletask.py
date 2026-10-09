# 1
my_tuple=(1,2,3,4)
print(my_tuple[2])

# 2
my_tuple=(10,20,30)
temp_list=list(my_tuple)
print(temp_list)

# 3
my_list=[1,2,3]
temp_tuple=tuple(my_list)
print(temp_tuple)

# 4
my_tuple=("a","b","c","d")
print(my_tuple[1:3])

# 5
my_tuple=("x","y","z")
print("x" in my_tuple)

# 6
my_tuple=(5,3,9,1)
print(max(my_tuple))

# 7
my_tuple=(1,2,3)
result= my_tuple * 2
print(result)


# 8
my_tuple=(1,2,2,3,2)
print(my_tuple.count(2))

# 9
my_tuple=("dog","cat","mouse")
print(my_tuple.index("cat"))

# 10
my_tuple=(1,2,3,4,5)
print(my_tuple[::-1])

# 11
tuple1=(1,2)
tuple2=(3,4)
combined_tuple=tuple1+tuple2
print(combined_tuple)

# 12
print(tuple("hello"))

# 13
my_tuple=(1,2,3,4)
print(my_tuple[0],my_tuple[-1])

# 14
my_tuple=(10,20,30,40)
my_list=list(my_tuple)
my_list[2]=99
my_tuple=tuple(my_list)
print(my_tuple)

# 15
a, b, c=(1, 2, 3)
print(a, b, c)

# 16
my_tuple=(1, 2, 3)
nested=(my_tuple,)
print(nested)

# 17
my_tuple=("a","b")
my_list=["c","d"]
print(my_tuple+tuple(my_list))

# 18
my_tuple=(1,2,3)
print(my_tuple == my_tuple[::-1])

# 19
my_tuple=([1,2],[3,4])
flat=[]
for my_list in my_tuple:
    flat.extend(my_list)
print(flat)    

# 20
my_tuple=(1,[2,3],4)
my_tuple[1].append(5)
print(my_tuple)