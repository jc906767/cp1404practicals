"""
CP1404/CP5632 - Practical
Answer the following questions:
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

#1. When will a ValueError occur?
#If something that cannot be converted to an interger as either the numerator or denominator, like letters and imaginary numbers.

#2. When will a ZeroDivisionError occur?
# If the denominator is chosen to be 0.

#3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Yes you could. You would need to check the denominator is not 0 before completing the division.