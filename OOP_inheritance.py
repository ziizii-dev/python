class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"{self.brand} - {self.year}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_cc):
        super().__init__(brand, year)
        self.engine_cc = engine_cc

    def info(self):
        super().info()
        print(f"Engine: {self.engine_cc} cc")

# Create object
bike = Motorcycle("Yamaha", 2021, 155)

# Call method
bike.info()

# .....................
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")
# Another child class
class Cat(Animal):
    def speak(self):

        
        print(f"{self.name} meows.")

        

# Create objects
dog = Dog("Buddy")

    
cat = Cat("Whiskers")

# Use inherited and overridden methods
dog.speak()   # Output: Buddy barks.
cat.speak()   # Output: Whiskers meows.
q