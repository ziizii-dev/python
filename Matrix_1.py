

if 5 > 4:
    print("5 is greater than 4")

    x = 5
    y=50
    z = x+y
    print("Value",z)
    fruits = ["apple","banana","mango"]
    for fruit in fruits:
        print(fruit)

        run= "awesome"
        def running():
            run = "fantastic"
            print("Python is " + run)
            running()
        print("Python is"+run)


b = "Hello, World!"
print(b[3:5])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print("Strip",a.strip()) # returns "Hello, World!"
a = "Aung Htwe!"
print(a.replace("Aung", "Maung"))

a = "Hello, World!"
print("Split",a.split(","))


age = 36

txt = f"My name is John, I am {age} years old"
print(txt)

age = 36
txt = f"My name is John \"Width\", I am {age}"
print(txt)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

x = 30
students =["John","Anna","Michael"]

i = 0
while i < len(students):
    print(students[i])
    i += 1

    i = 0
    while True:
        print(students[i])
        i += 1
        if i >= len(students):
            break


