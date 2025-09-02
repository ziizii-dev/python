class Dog:
    def speak(self):
        print("Dog says: Woof!")

class Cat:
    def speak(self):
        print("Cat says: Meow!")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()

# .......................
class Product:
    def __init__(self, name):
        self.name = name

    def get_delivery_method(self):
        pass

class PhysicalProduct(Product):
    def get_delivery_method(self):
        return f"{self.name}: Ship via courier"

class DigitalProduct(Product):
    def get_delivery_method(self):
        return f"{self.name}: Email download link"

products = [
    PhysicalProduct("Laptop"),
    DigitalProduct("E-book"),
    PhysicalProduct("Phone")
]

for p in products:
    print(p.get_delivery_method())



# ...........Classes and Objects............
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.grade}")

# Create student objects
s1 = Student("Ali", "A")
s2 = Student("Sara", "B")

s1.display_info()
s2.display_info()

# Del.................
class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} has been deleted.")

p1 = Person("Alice")
del p1  # Output: Alice has been deleted.


