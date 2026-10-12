# # 1
# a=float(input("Enter a number: "))
# print(a)
# if a>0:
#     print("a is positive")
# elif a==0:
#     print("a is zero")
# else:
#     print("a is negative")

# # 2
# a=int(input("Enter a number: "))
# if a%2==0:
#     print("a is even")
# else:
#     print("a is odd")

# # 3
# a=int(input("enter a num: "))
# if a >100:
#     print("a is greater than 100")
# elif a==100:
#     print("a is equal to 100")
# else:
#     print("a is not greater than 100")

# # 4
# a=int(input("enter age: "))
# if a >= 18:
#     print("eligible for vote")
# else:
#     print("not eligible") 

# # 5
# a=int(input("enter first num: "))
# b=int(input("enter second num:"))
# if a>b:
#     print(a)
# elif a<b:
#     print(b)
# else:
#     print("both are equal")

# # 6
# a=int(input("enter first num: "))
# b=int(input("enter second num:"))
# c=int(input("enter third num: "))
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

# # 7
# a=int(input("enter a year: "))
# if a % 400==0:
#     print("year is leap")
# elif a% 100 ==0:
#     print("year is not leap")
# elif a% 4==0:
#     print("leap year")
# else:
#     print("not a leap year")

# # 8
# a=int(input("enter mark: "))
# if a >= 40:
#     print("passed")
# else:
#     print("failed")

# # 9
# a=int(input("enter mark: "))
# if a >= 90:
#     print("A")
# elif a >= 75:
#     print("B")
# elif a >= 60:
#     print("C")
# else:
#     print("failed")

# 10
# ch = input("enter a character: ").lower()
# if ch in "aeiou":
#     print("vowel")
# else:
#     print("consonant")

# 11
# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i) 

# 12
# for i in range(1,11):
#     if i ==5:
#         continue
#     print(i)

# 13
# n=int(input("enter a number: "))
# if n>0:
#     pass
# print("program ended")

# 14
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# 15
# result=0
# for i in range (1,11):
#     result= result+i
# print(result)

# 16
# n=int(input("enter a number: "))
# if n % 3 == 0 and n % 5 == 0:
#     print("multiple of both")
# else:
#     print("not multiple of both")

# 17
# for a in range (1,6):
#     print("hello")

# 18
# num = [1,2,3,4,5]
# for i in num:
#     if i > 3:
#         print(i)

# 19
# attempts = 3
# for i in range(attempts):
#     user=input("username: ")
#     code=input("password: ")
#     if user.lower() == "admin" and code == "1234":
#         print("login successful")
#         break
#     print("attempts remaining: ", attempts - i - 1)
# else:
#     print("accounted locked")

# 20
# a= input("enter a colour or number: ").strip().lower()
# if a in ("1","red"):
#     print("stop and wait for 60 seconds")
# elif a in ("2","yellow"):
#     print("ready and wait for 5 seconds")
# elif a in ("3", "green"):
#     print("go and drive safely")
# else:
#     print("invalid signal")

# list comprehension questions
 
# 1
# num = [4,6,9,13,15,10,18]
# total = sum([x for x in num])
# even_sum=sum([x for x in num if x % 2 == 0])
# odd_sum=sum([x for x in num if x % 2 != 0])
# print(total)
# print(even_sum)
# print(odd_sum)

# # 2
# l2=[x for x in num if x > 10 and x % 3 == 0]
# print(l2)

# # 3
# l3=[x for x in num if x % 2 == 0 and x > 10]
# print(l3)

# # 4
# words = ["apple","kiwi","cherry"]
# l4=[len(w) for w in words]
# print(l4)

# # 5
# l5=["even" if x % 2 == 0 else "odd" for x in num]
# print(l5)