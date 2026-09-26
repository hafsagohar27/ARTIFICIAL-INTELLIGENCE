```python
# =========================
# LAB 3 - PYTHON PROGRAMS
# =========================


# Q1. Numbers divisible by 7 and multiple of 5
print("\nQ1")
for number in range(1500, 2701):
    if number % 7 == 0 and number % 5 == 0:
        print(number)


# Q2. Celsius to Fahrenheit and Fahrenheit to Celsius
print("\nQ2")

c = float(input("Enter temperature in Celsius: "))
f = (c * 9 / 5) + 32
print(c, "C is", f, "Fahrenheit")

f = float(input("Enter temperature in Fahrenheit: "))
c = (f - 32) * 5 / 9
print(f, "F is", c, "Celsius")


# Q3. Guess a number between 1 and 9
print("\nQ3")

secret = 5

while True:
    guess = int(input("Guess a number between 1 and 9: "))

    if guess == secret:
        print("Well guessed!")
        break


# Q4. Star pattern
print("\nQ4")

rows = [1, 2, 3, 4, 5, 4, 3, 2, 1]

for row in rows:
    for i in range(row):
        print("*", end=" ")
    print()


# Q5. Reverse a word
print("\nQ5")

word = input("Enter a word: ")
reverse = word[::-1]

print("Reverse:", reverse)


# Q6. Count even and odd numbers
print("\nQ6")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even = 0
odd = 0

for number in numbers:
    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even numbers:", even)
print("Number of odd numbers:", odd)


# Q7. Print each item and its type
print("\nQ7")

datalist = [
    1452,
    11.23,
    1 + 2j,
    True,
    "w3resource",
    (0, -1),
    [5, 12],
    {"class": "V", "section": "A"}
]

for item in datalist:
    print(item, type(item))


# Q8. Print numbers from 0 to 6 except 3 and 6
print("\nQ8")

for number in range(7):
    if number == 3 or number == 6:
        continue

    print(number)


# Q9. Fibonacci series between 0 and 50
print("\nQ9")

a = 0
b = 1

while b <= 50:
    print(b, end=" ")
    a, b = b, a + b

print()


# Q10. Two-dimensional array
print("\nQ10")

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

array = []

for i in range(m):
    row = []

    for j in range(n):
        row.append(i * j)

    array.append(row)

print(array)


# Q11. Accept lines until blank line
print("\nQ11")

while True:
    line = input("Enter a line: ")

    if line == "":
        break

    print(line.lower())


# Q12. Binary numbers divisible by 5
print("\nQ12")

numbers = input("Enter 4-digit binary numbers separated by comma: ").split(",")

result = []

for binary in numbers:
    decimal = int(binary, 2)

    if decimal % 5 == 0:
        result.append(binary)

print("Result:", ",".join(result))


# Q13. Count letters and digits
print("\nQ13")

text = input("Enter a string: ")

letters = 0
digits = 0

for character in text:
    if character.isalpha():
        letters += 1
    elif character.isdigit():
        digits += 1

print("Letters", letters)
print("Digits", digits)


# Q14. Password Validation
print("\nQ14")

import re

password = input("Enter password: ")
3

if (6 <= len(password) <= 16 and
    re.search("[a-z]", password) and
    re.search("[A-Z]", password) and
    re.search("[0-9]", password) and
    re.search("[$#@]", password)):

    print("Valid Password")
else:
    print("Invalid Password")
```
============================================================ 