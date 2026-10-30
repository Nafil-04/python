# class Employee:
#     def __init__(self,name,salary):
#         self.n= name
#         self.__s=salary

#     def display_employee(self):
#         print(f"name:{self.n}, salary:{self.__s}")

#     def update_salary(self,new_salary):
#         self.__s=new_salary

# emp=Employee("john",50000)
# emp2=Employee("jane",75000)
# # emp.display_employee()
# emp2.display_employee()

# emp.update_salary(60000)
# emp.display_employee()

#          Inheritance
#   Single Inheritance

# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print(f"{self.name}makes a sound.")

# class Dog (Animal):
#     def speak(self):
#         print(f"{self.name} says Woof!!")

# dog=Dog("Buddy")
# dog.speak()

#     Multiple Inheritance

# class Engine:
#     def start_engine(self):
#         print("Engine started")

# class Wheels:
#     def rotate(self):
#         print("Wheels are rotating")

# class Car(Engine,Wheels):
#     def drive(self):
#         print("Car is driving")

# car=Car()
# car.start_engine()
# car.rotate()
# car.drive()


#      Multilevel inheritance

# class Grandparent:
#     def sing(self):
#         print("Grandfather is singing.")

# class Parent(Grandparent):
#     def dance(self):
#         print("parent is dancing")

# class Child(Parent):
#     def play(self):
#         print("child is playing")

# child=Child()
# child.sing()
# child.dance()
# child.play()

#     Hierarchical Inheritance

# class Animal:
#     def speak(self):
#         print("animal speaks")

# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# class Cat(Animal):
#     def speak(self):
#         print("Cat meows.")

# dog=Dog()
# cat=Cat()

# dog.speak()
# cat.speak()

#       Hybrid Inheritance

# class A:
#     def method_a(self):
#         print("Method from class A")

# class B(A):
#     def method_b(self):
#         print("Method from class B")

# class C(A):
#     def method_c(self):
#         print("Method from class C")

# class D(C,B):
#     def method_d(self):
#         print("Method from class D")

# d=D()
# d.method_a()
# d.method_b()
# d.method_c()
# d.method_d()

# Polymorphism

class Animal:
    def speak(self):
     return "some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Human:
    def speak(self):
        return "yello"

def animal_sound(animal:Animal):
    return animal.speak()

dog=Dog()
cat=Cat()
human=Human()
print(animal_sound(dog))
print(animal_sound(cat))
print(animal_sound(human))


