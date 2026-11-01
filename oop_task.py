# # 1
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def display_grade(self):
#         if self.marks >= 90:
#             self.grade = "A"
#         elif self.marks >= 75:
#             self.grade ="B"
#         elif self.marks >= 50:
#             self.grade ="C"
#         else:
#             self.grade = "Fail"

#         print(f"{self.name}'s grade :{self.grade}")

# s1 = Student("alice",88)
# s2 = Student("john",92)

# s1.display_grade()
# s2.display_grade()

# # 2
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def calculate_average(self):
#      return sum (self.marks.values()) / len(self.marks)

#     def display_grade(self):
#         avg = self.calculate_average()

#         if avg >= 90:
#             self.grade = "A"
#         elif avg >= 75:
#             self.grade ="B"
#         elif avg >= 50:
#             self.grade ="C"
#         else:
#             self.grade = "Fail"

#         print(f"{self.name}'s average: {avg} | grade: {self.grade}")

# s1 = Student("alice",{"math": 85 , "science": 94})
# s2 = Student("john",{"math": 90 , "science": 88})

# s1.display_grade()
# s2.display_grade()

# # 3
# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner= owner
#         self.__balance = balance 

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited Rs {amount}")

#     def withdraw(self,amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrew Rs {amount}")
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.__balance

# acc = BankAccount("Alice" , 1000 )

# acc.deposit(500)
# acc.withdraw(200)
# print("final balance:", acc.get_balance())

# print(acc.__balance)

# 3
# class Bird:
#     def sound(self):
#         print("Bird makes a sound")

# class Parrot(Bird):
#     def sound(self):
#         print("parrot says 'hello'")

# class Sparrow(Bird):
#     def sound(self):
#         print("sparrow chirps")

# def make_sound(bird):
#     bird.sound()

# make_sound(Parrot())
# make_sound(Sparrow())

# 4
# class Book:
#     def __init__(self,title,author,copies):
#         self.title = title
#         self.author = author
#         self.copies = copies

#     def display_info(self):
#         print(f"Title: {self.title} | Author: {self.author} | copies: {self.copies}")

# books= []

# for i in range(3):
#     title = input("Enter book title: ")
#     author = input("enter author: ")
#     copies = int(input("enter copies: "))
#     books.append(Book(title,author,copies))

# search = input("enter book title to search")
# found = False

# for book in books:
#     if book.title.lower() == search.lower():
#         book.display_info
#         found = true
#         break

# if not found:
#     print("book not available")

# 5
# class Employee:
#     def __init__(self, name, position, salary):
#         self.name= name
#         self.position = position
#         self.salary = salary

#     def apply_bonus(self, percentage):
#         self.salary += self.salary * percentage / 100

#     def display_info(self):
#         print(f"Name: {self.name} | position: {self.position} | salary: {self.salary}")

# employees = []

# for i in range(2):
#     name= input("enter name: ")
#     position = input("enter position: ")
#     salary = float(input("enter salary: "))
#     bonus = float(input("enter bonus %: "))

#     emp = Employee(name, position,salary)
#     emp.apply_bonus(bonus)
#     employees.append(emp)

# for emp in employees:
#     emp.display_info()

# 6
# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price

# class Cart:
#     def __init__(self):
#         self.products=[]

#     def add_product(self, product):
#         self.products.append(product)

#     def total_price(self):
#         total=0
#         for p in self.products:
#             total += p.price
#         return total

# cart = Cart()

# for i in range(3):
#     name= input("enter product name: ")
#     price = float(input("enter price: "))
#     cart.add_product(Product(name, price))

# print("total price: Rs", cart.total_price()) 

# 7
# class Movie:
#     def init(self, title, available_seats):
#         self.title = title
#         self.available_seats = available_seats

#     def book_ticket(self, seats):
#         if seats <= self.available_seats:
#             self.available_seats -= seats
#             print(f"{seats} tickets booked successfully.")
#         else:
#             print("Not enough seats.")

# title = input("Enter movie title: ")
# seats = int(input("Enter available seats: "))
# movie = Movie(title, seats)

# for i in range(2):
#     n = int(input("Enter seats to book: "))
#     movie.book_ticket(n)


# #8
# class Customer:
#     def init(self, name, income, credit_score):
#         self.name = name
#         self.income = income
#         self.credit_score = credit_score

#     def check_eligibility(self):
#         if self.income >= 25000 and self.credit_score >= 650:
#             print(f"{self.name} is eligible for loan.")
#         else:
#             print(f"{self.name} is not eligible for loan.")

# name = input("Enter name: ")
# income = int(input("Enter income: "))
# credit_score = int(input("Enter credit score: "))

# customer = Customer(name, income, credit_score)
# customer.check_eligibility()


# # 9
# class Order:
#     def init(self, order_id, product_name, status):
#         self.order_id = order_id
#         self.product_name = product_name
#         self.status = status

# orders = []

# for i in range(2):
#     oid = int(input("Enter order ID: "))
#     pname = input("Enter product name: ")
#     status = input("Enter status: ")
#     orders.append(Order(oid, pname, status))

# update_id = int(input("Enter order ID to update: "))
# for order in orders:
#     if order.order_id == update_id:
#         order.status = input("Enter new status: ")
#         break
# else:
#     print("Order not found")

# print("Updated Orders:")
# for order in orders:
#     print(f"{order.order_id} - {order.product_name} - {order.status}")