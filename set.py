# creating a set
# my_set={1,2,3,4}
# print(my_set)

# another_set=set([5,6,7])
# print(another_set)

# empty_set=set()
# print(type(empty_set))

# accessing set items
# my_set={10,20,30,40}
# print(10)
# print(10 in my_set)
# print(50 in my_set)

# adding items to a set
# my_set={1,2,3}
# my_set.add(4) #adding single item
# print(my_set)

# my_set={1,2,3}
# my_set.update([4,5,6,7]) #adding multiple items 
# print(my_set)

# removing items
# my_set={1,2,3,4}
# my_set.remove(2)
# print(my_set)

# my_set.discard(1)
# print(my_set)

# my_set={1,2,3,'apple','banana'}
# removed_item=my_set.pop()
# print(removed_item)

# joining sets

# union
# set1={1,2,3,4}
# set2={4,5,6}
# result=set1.union(set2)
# print(result)

# update
# set1={1,2,3,4}
# set2={4,5,6}
# set1.update(set2)
# print(set1)

# intersection
# set1={1,2,3}
# set2={2,3,4}
# result=set1 & set2
# print(result)

# set difference
# set1={1,2,3}
# set2={2,3,4}
# result=set1 - set2
# print(result)

# set1={1,2,3}
# set2={2,3,4}
# result=set1^set2
# print(result)

# set1={1,2}
# set2={1,2,3,4,5}
# print(set1.issubset(set2))