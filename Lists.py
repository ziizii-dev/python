thislist = ["apple", "banana", "cherry", "orange", "water lemon", "melon", "mango"]
thislist.append("orange")
print("append",thislist)
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
thislist[1] = "blackcurrant"
print(thislist)
thislist[0:3] = ["ChangeName", "Hello world"]
print(thislist)

thislist.insert(1, "add item")
print("add item = ",thislist)



tropical = ["A", "B", "C"]
thislist.extend(tropical)
print("extend = ",thislist)

thistuple = ("kiwi", "banana")
thislist.extend(thistuple)
print(thislist)

thislist.remove("banana")
print(thislist)

thislist.pop(1)
print("pop = " ,thislist)

# thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# del thislist
# print("delete successfully")
thislist.clear()
print("clear successfully")
