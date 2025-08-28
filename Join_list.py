from list_comprehension import fruits
# Using manual writing
alphabet = ["a", "b", "c"]
numbers = [1, 2, 3]

sum = alphabet + numbers
print(sum)

# Using append method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

print(list1)


# Using extend method.......
fruits=["apple","banana","cheery","strawberry"]
juices =["appjuice","streJuice","gjuice","oneJuice"]
fruits.extend(juices)
print(fruits)

#List Method	Description.........
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()