
# manual Writing..........
def copy_list(input_list):
    return [item for item in input_list]

# new_list = []
# for item in input_list:
#     new_list.append(item)
# return new_list

fruits = ["apple", "banana", "cherry"]
mylist = copy_list(fruits)
print("Copied List:", mylist)

#Using Function.........
words = ["a", "b", "c"]
wordlist = words.copy()
print(wordlist)

# Using list to copy
names = ["john", "pinkle", "kary"]
namelist = list(names)
print(namelist)