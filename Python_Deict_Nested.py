car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "specs": {
        "engine": "V8",
        "color": "red",
        "dimensions": {
            "length": "4.8m",
            "width": "1.8m"
        }
    }
}

print(car["specs"]["engine"])        # Output: V8
print(car["specs"]["dimensions"]["length"])  # Output: 4.8m


for key, value in car.items():
    if isinstance(value, dict):
        print(f"{key} is a nested dictionary:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")


child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)