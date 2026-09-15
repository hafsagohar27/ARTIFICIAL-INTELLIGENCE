# Lab 2 - Iterative Structures in Python

# 1. While Loop
print("1. While Loop")

count = 0

while count < 3:
    count = count + 1
    print("Hello Geek")


# 2. For Loop with List
print("\n2. For Loop with List")

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# 3. For Loop with String
print("\n3. For Loop with String")

word = "Geeks"

for letter in word:
    print(letter)


# 4. Continue Statement
print("\n4. Continue Statement")

for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        continue
    print(letter)


# 5. Break Statement
print("\n5. Break Statement")

for letter in "geeksforgeeks":
    if letter == "e" or letter == "s":
        break
    print(letter)


# 6. Function
print("\n6. Function")

def my_function():
    print("Hello from a function")

my_function()


# 7. Function with Parameter
print("\n7. Function with Parameter")

def greet(name):
    print("Hello " + name)

greet("Ali")
greet("Ahmed")


# 8. Function with Return Value
print("\n8. Function with Return Value")

def multiply(x):
    return 5 * x

print(multiply(3))
print(multiply(5))
print(multiply(9))


# 9. Function with List
print("\n9. Function with List")

def print_fruits(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

print_fruits(fruits)


# 10. Class and Object
print("\n10. Class and Object")

class MyClass:
    x = 5

p1 = MyClass()

print(p1.x)


# 11. Class with Constructor
print("\n11. Class with Constructor")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


# 12. Class with Method
print("\n12. Class with Method")

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p2 = Student("John", 36)

p2.myfunc()
