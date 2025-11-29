"""
CP1404/CP5632 Practical
UnreliableCar class
"""

from car import Car
import random


class UnreliableCar(Car):
    """Specialised Car that only drives based on its reliability percentage."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar with name, fuel, and reliability."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than reliability."""
        random_chance = random.uniform(0, 100)

        # If the random value is less than the reliability, the car drives
        if random_chance < self.reliability:
            return super().drive(distance)

        # Otherwise, car fails to drive — return 0 km as required
        return 0
