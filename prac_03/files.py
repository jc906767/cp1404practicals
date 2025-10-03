"""
CP1404/CP5632 - Practical
Files exercises
"""

# 1. Ask user for their name, write it to name.txt
name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()


# 2. Read the name from name.txt and print it
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")


# 3. Create numbers.txt with these lines: 17, 42, 400
# Then read only the first two numbers, add them, and print result
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    print(number1 + number2)


# TODO: 4) ow write a fourth block of code that prints the total for all
#  lines in numbers.txt. This should work for a file with any number of
#  numbers. Use with instead of open and close for this question.

