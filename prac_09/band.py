"""
Band class for CP1404
"""

class Band:
    """Band class that contains a list of musicians."""

    def __init__(self, name=""):
        """Initialise a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of the Band and its musicians."""
        musician_str = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_str})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a multi-line string showing each musician playing."""
        return "\n".join(musician.play() for musician in self.musicians)
