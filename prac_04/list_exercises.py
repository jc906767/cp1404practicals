"""
CP1404 Practical
Basic list operations and woefully inadequate security checker.
"""

NUMBER_COUNT = 5

def main():
    """Run the number sorter and security checker."""
    numbers = get_numbers(NUMBER_COUNT)
    display_number_summary(numbers)
    check_user_access()

def get_numbers(count):
    """request 5 numbers, store them in a list, and display summary information."""
    numbers = []
    print("Please give 5 values")
    for i in range(count):
        number = int(input(f"Input number {i + 1}: "))
        numbers.append(number)
    return numbers

def display_number_summary(numbers):
    """Display the first, last, smallest, largest, and average of the numbers."""
    print()
    for i, number in enumerate(numbers, start=1):
        print(f"Number {i}: {number}")
    print(f"The first number is: {numbers[0]}")
    print(f"The last number is: {numbers[-1]}")
    print(f"The smallest number is: {min(numbers)}")
    print(f"The largest number is: {max(numbers)}")
    print(f"The average of the numbers is: {sum(numbers) / len(numbers):.1f}")

def check_user_access():
    """Ask for a username and print whether access is granted."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username_input = input("Please type your username: ")
    if username_input in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()