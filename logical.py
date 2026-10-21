# que 1
numbers = [12,5,12,9,7]
largest = None
second_largest= None

for num in numbers:

    if largest is None:
        largest = num
    elif num > largest:
        second_largest = largest
        largest = num
    elif second_largest is None and num < largest:
        second_largest = num
    elif num < largest and num > second_largest :
        second_largest = num
    
if second_largest is None:
    print("No second-largest distinct value")
else:
    print(second_largest)

# que 2
text = input("enter a string")

for char in text:
    count = 0



        

