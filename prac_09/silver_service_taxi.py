"""
CP1404/CP5632 Practical
Silver Service Taxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi that includes fanciness and flagfall charges."""

    flagfall = 4.50  # class variable for every new fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Multiply the price per km by fanciness to make expensive taxis more costly
        self.price_per_km *= fanciness

    def get_fare(self):
        """Calculate fare: base fare from Taxi + flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
