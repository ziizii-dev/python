
fruits = ("apple", "banana", "cherry", "apple", "cherry")
print(fruits)
print(len(fruits))
print(type(fruits))

lists = tuple(("apple", "banana", "cherry"))
print(lists)

words = tuple("abc")
print(words)



def users():
    return ["MgMg", "Aung Aung", "Su Su"]

names = tuple(users())
print(names)
