"""
CP1404/CP5632 Practical
Read guitars from a CSV file into Guitar objects, display them,
then show them sorted by year (oldest to newest).
"""

import csv
from guitar import Guitar


FILENAME = "guitars.csv"


def main():
    """Load, display, and sort guitars from a CSV file."""
    guitars = load_guitars(FILENAME)

    print("All guitars:")
    display_guitars(guitars)

    print("\nGuitars sorted by year (oldest → newest):")
    guitars.sort()  # uses Guitar.__lt__
    display_guitars(guitars)


def load_guitars(filename: str) -> list[Guitar]:
    """Read guitars from CSV (Name,Year,Cost) and return a list of Guitar objects."""
    guitars: list[Guitar] = []
    with open(filename, "r", newline="", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for name, year_text, cost_text in reader:
            guitar = Guitar(name, int(year_text), float(cost_text))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars: list[Guitar]) -> None:
    """Print each guitar, one per line."""
    for guitar in guitars:
        print(guitar)


if __name__ == "__main__":
    main()
