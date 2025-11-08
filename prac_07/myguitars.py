"""
CP1404/CP5632 Practical
Read guitars from a CSV file into Guitar objects, display them,
then show them sorted by year (oldest to newest).
"""

import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load, extend, display, and save the guitar collection."""
    guitars = load_guitars(FILENAME)

    print("Current guitars:")
    display_guitars(guitars)

    print()
    new_guitars = get_new_guitars()
    guitars.extend(new_guitars)

    if new_guitars:
        print("\nAdded guitars:")
        display_guitars(new_guitars)

    # Sort for display niceness; file can stay unsorted or sorted—your choice.
    guitars.sort()
    print("\nAll guitars (sorted by year):")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\nSaved {len(guitars)} guitars to {FILENAME}")


def load_guitars(filename: str) -> list[Guitar]:
    """Read guitars from CSV (Name,Year,Cost) and return a list of Guitar objects."""
    guitars: list[Guitar] = []
    with open(filename, "r", newline="", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            if not row:
                continue
            name, year_text, cost_text = row
            guitars.append(Guitar(name, int(year_text), float(cost_text)))
    return guitars


def save_guitars(filename: str, guitars: list[Guitar]) -> None:
    """Write guitars to CSV (Name,Year,Cost)."""
    with open(filename, "w", newline="", encoding="utf-8") as out_file:
        writer = csv.writer(out_file)
        for g in guitars:
            writer.writerow([g.name, g.year, f"{g.cost:.2f}"])


def display_guitars(guitars: list[Guitar]) -> None:
    """Print each guitar, one per line."""
    for guitar in guitars:
        print(guitar)


def get_new_guitars() -> list[Guitar]:
    """Prompt the user to enter new guitars until a blank name is entered."""
    print("Enter your new guitars (blank name to finish):")
    new_guitars: list[Guitar] = []
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        year = get_valid_int("Year: ")
        cost = get_valid_float("Cost: $")
        new_guitars.append(Guitar(name, year, cost))
    return new_guitars


def get_valid_int(prompt: str) -> int:
    """Get a valid integer from user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; enter an integer.")


def get_valid_float(prompt: str) -> float:
    """Get a valid float from user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input; enter a number.")


if __name__ == "__main__":
    main()