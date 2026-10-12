# 1
my_set={1,2,3,4}
print(my_set)

# 2
my_set={1,2,3,4}
my_set.add(5)
print(my_set)

# 3
my_set={1,2,3,4}
my_set.remove(3)
print(my_set)

# 4
my_set={1,2,3,4}
print(2 in my_set)

# 5
my_list=[1,2,2,3,4,4]
print(set((my_list)))

# 6
my_tuple=(10,20,30)
print(set(my_tuple))

# 7
set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))

# 8
set1={1,2,3}
set2={3,4,5}
result=set1 & set2
print(result)

# 9
set1={1,2,3,4}
set2={3,4}
result=set1 - set2
print(result)

# 10
my_set={5,6,7}
a=my_set.copy()
print(a)

# 11
my_set={1,2,3}
my_set.clear()
print(my_set)

# 12
set1={1,2}
set2={1,2,3}
print(set1.issubset(set2))

# 13
set1={1,2,3}
set2={1,2}
print(set1.issuperset(set2))

# 14
set1={1,2,3}
set2={3,4,5}
result=set1 ^ set2
print(result)

# 15
my_set={1,2,3}
my_set.update({8,9,10})
print(my_set)

# 16
my_set={1,2,3}
removed= my_set.pop()
print(removed,my_set)

# 17
set1={1,2,3}
set2={3,2,1}
print(set1 == set2)

# 18
my_list=[1,2,2,3,4,4,5]
result=set(my_list)
print(result)

# 19
my_set={1,2,3}
print(list(my_set))

# 20
my_set={1,2,3,4,5}
my_set.difference_update({4,5})
print(my_set)
