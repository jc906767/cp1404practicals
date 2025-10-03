"""
CP1404/CP5632 - Practical
Files exercises
"""

# 1. Ask user for their name, write it to name.txt
name = input("Enter your name: ")
output_file = open("name.txt", "w")
print(name, file=output_file)
output_file.close()


# 2. Read the name from name.txt and print it
input_file = open("name.txt", "r")
name = input_file.read().strip()
input_file.close()
print(f"Hi {name}!")


# 3. Create numbers.txt with these lines: 17, 42, 400
# Then read only the first two numbers, add them, and print result
with open("numbers.txt", "r") as input_file:
    number1 = int(input_file.readline())
    number2 = int(input_file.readline())
    print(number1 + number2)


total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        total += int(line)
print(total)