class Car:
    def __init__(self, made, brand, model, year, engine):
        self.made = made
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine

    def display_info(self):
        print(f"{self.made} {self.year} {self.brand} {self.model} - Engine: {self.engine}")

my_car = Car("Japan", "Toyota", "Corolla", 2002, "V4")
my_car.display_info()

# Inheritance


