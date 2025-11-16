"""CP1404/CP5632
Guitar class.

Estimate: 25 minutes
Actual: 20 minutes
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name: str = "", year: int = 0, cost: float = 0):

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:

        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self) -> int:
        """Return how old the guitar is in years"""
        return CURRENT_YEAR - self.year

    def is_vintage(self) -> bool:
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other: "Guitar") -> bool:
        """Return True if this guitar is 'less than' another, ordered by year (oldest to newest)."""
        return self.year < other.year