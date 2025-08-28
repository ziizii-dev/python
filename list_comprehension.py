
#filtering method

fruits = ["aung", "maung", "susu", "swea", "moe"]
newlist = []

for x in fruits:
  if "u" in x:
    newlist.append(x)

print("newlist = ",newlist)