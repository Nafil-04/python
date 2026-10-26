# # defining a class
# class Car:
#     def __init__(self,make,model,year,price):
#         self.m=make
#         self.mo=model
#         self.y=year
#         self.p=price

#     def display_info(self):
#      print(f"Car:this is a {self.m} {self.mo} {self.y} price is {self.p}")

# car1 = Car("toyota","corolla","2020","3500000")
# car1.display_info()
# car2 = Car("Ford","Mustang","2024","200000000")
# car2.display_info()

# car1.p="3000000"
# car1.display_info()
# car2.mo="GT"
# car2.p="400000000"
# car2.y=2013
# car2.display_info()

# str method
# class Book:
#     def __init__(self,title,author):
#         self.t=title
#         self.a=author

#     def __str__(self):
#         return f"'{self.t}'by {self.a}"

# book = Book ("1984","George Orwell")
# print(book)

# cls variable vs instance variable
# class Employee:
#     company = "ABC Corp"

#     def __init__(self,name,position):
#         self.name=name
#         self.position=position

# emp1=Employee("jack","manager")
# emp2=Employee("alice","developer")

# # cls variable = same 
# print(emp1.company)
# print(emp2.company)

# # instance variable = unique
# print(emp1.position)
# print(emp2.position)

# task
class Student:
    def __init__(self,name,marks):
        self.n=name
        self.m=marks
    def display_grade(self):
        if self.m>= 90:
            self.grade = "A"
        elif self.m >= 75:
            self.grade ="B"
        elif self.m >= 50:
            self.grade = "C"
        else:
            self.grade = "Fail"
        print(f"{self.n}'s grade: {self.grade} ")


std1=Student("jack",80)
std2=Student("alice",95)

std1.display_grade()
std2.display_grade()