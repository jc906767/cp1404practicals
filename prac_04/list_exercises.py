"""
CP1404 Practical
Basic list operations
"""


def main():
    """request 5 numbers, store them in a list, and display summary information."""
    numbers = []
    NUMBER_COUNT = 5

    for i in range(NUMBER_COUNT):
        number = int(input("Number: "))
        numbers.append(number)

    display_number_summary(numbers)

def display_number_summary(numbers):
    """Display all the numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

main()
