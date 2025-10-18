"""
CP1404/CP5632 Practical
Wimbledon data processing
Estimate: 30 minutes
Actual:   xx minutes
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data, then display champion win counts and countries."""
    rows = load_wimbledon_data(FILENAME)
    champion_to_wins = count_champions(rows)
    countries = get_countries(rows)

    print("Wimbledon Champions:")
    for champion in sorted(champion_to_wins):
        print(f"{champion} {champion_to_wins[champion]}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


def load_wimbledon_data(filename):
    """Load rows from the Wimbledon CSV file.

    Returns a list of lists in the order [year, country, champion].
    """
    rows = []
    with open(filename, "r", encoding="utf-8-sig", newline="") as in_file:
        reader = csv.reader(in_file)
        headers = next(reader)  # Skip header row

        # Try to handle either positional or named columns robustly
        try:
            year_i = headers.index("Year")
            country_i = headers.index("Country")
            champion_i = headers.index("Champion")
        except ValueError:
            # Fallback to the standard CP1404 order if headers are unexpected
            year_i, country_i, champion_i = 0, 1, 2

        for row in reader:
            if not row:
                continue
            rows.append([row[year_i], row[country_i], row[champion_i]])
    return rows


def count_champions(rows):
    """Build and return a dict mapping champion -> number of wins."""
    champion_to_wins = {}
    for _year, _country, champion in rows:
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def get_countries(rows):
    """Return a set of unique countries from the data."""
    return {country for _year, country, _champion in rows}


if __name__ == "__main__":
    main()
