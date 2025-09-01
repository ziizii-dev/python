car = {"brand": "Ford", "model": "Mustang", "year": 1964}

for key in car:
    print(key)
    print("........")
    print("value",car[key])


for key in car.keys():
    print(key)

for value in car.values():
    print(value)

for key, value in car.items():
    print(key, value)
