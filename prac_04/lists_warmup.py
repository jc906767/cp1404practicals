"""
CP1404 - Practical
Warm-up exercise for lists
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# Predicted Answers:
# numbers[0]          = 3
# numbers[-1]         = 2
# numbers[3]          = 1
# numbers[:-1]        = [3, 1, 4, 1, 5, 9]
# numbers[3:4]        = [1]
# 5 in numbers        = True
# 7 in numbers        = False
# "3" in numbers      = False
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(f"numbers before changing anything: {numbers}")

#1 Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(f"numbers after changing first element: {numbers}")

#2 Change the last element of numbers to 1
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[-1] = 1
print(f"numbers after changing the last element: {numbers}")

#3 Print all the elements from numbers except the first two (slice)
numbers = [3, 1, 4, 1, 5, 9, 2]

numbers = numbers[slice(2, None)]
print(f"numbers after removing the first 2 elements: {numbers}")


#4 Print whether 9 is an element of numbers
numbers = [3, 1, 4, 1, 5, 9, 2]

if 9 in numbers:
    print(f"9 is in: {numbers}")
else:
    print(f"9 is not in: {numbers}")

