"""
CP1404 Practical
Quick Pick Lottery Ticket Generator
"""

import random

# Constants
NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
FIELD_WIDTH = len(str(MAX_NUMBER))  # width for aligned printing

def main():
    """request number of quick picks, generate them, and display results."""
    number_of_picks = get_non_negative_num("How many quick picks? ")
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:{FIELD_WIDTH}d}" for number in quick_pick))

def get_non_negative_num(prompt):
    """Get a non-negative integer"""
    value = int(input(prompt))
    while value < 0:
        print("Invalid input; enter 0 or more.")
        value = int(input(prompt))
    return value

def generate_quick_pick():
    """Return one quick pick: a sorted list of unique random numbers."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

main()
