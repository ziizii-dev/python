class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(f"{self.brand} - {self.year}")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_cc):
        super().__init__(brand, year)  

    def info(self):
        super().info()  
        print(f"Engine: {self.engine_cc} cc")


bike = Motorcycle("Yamaha", 2021, 155)

bike.info()
