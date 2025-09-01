# First Way
import copy

original = {
    "brand": "Ford",
    "specs": {"engine": "V8", "color": "red"}
}

deep_copy_dict = copy.deepcopy(original)
print(deep_copy_dict)

# Second way
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
copy_dict = car.copy()

print(copy_dict)
