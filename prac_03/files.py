"""
CP1404 - Practical - Files
Make the appropriate choice of file-reading technique for each task:
- read()
- readline()
- for line in file
"""

# 1. Ask for user’s name and write it to a file
with open("name.txt", "w") as out_file:
    name = input("What is your name? ")
    print(name, file=out_file)

# 2. Read the name back and greet the user
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print(f"Hi {name}!")

# 3. Read first two numbers and add them
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4. Sum all numbers in the file
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)
