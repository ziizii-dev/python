car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("brand = ",car["brand"])
year= car["year"]
model = car.get("model")
print(model)
print(year)
carValue = car.values()
print("car value",carValue)
key = car.keys()
print(key)

print(key) #before the change

car["color"] = "white"

print("changed color",key)



value = car.values()

print(value)

car["year"] = 2020
car["color"]="red"

print("change color",value)

carlists = car.items()
print("car lists",carlists)

if "model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary")

  car.update({"year": 2021})
  print("updated successfully",car)

  car["owner"]="Aung Aung"
  print("added successfully",car)

car.pop("model")
print("removed successfully",car)


car.popitem()
print("removed success",car)

del car["year"]
print("deleted successfully",car)
car.clear()
print("clear successfully",car)
