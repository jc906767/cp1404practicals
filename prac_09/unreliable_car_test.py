"""
CP1404/CP5632 Practical
Unreliable car test
"""
from unreliable_car import UnreliableCar

def main():
    """Run tests on the UnreliableCar class."""
    # Create two cars with different reliabilities
    reliable_car = UnreliableCar("Reliable", 100, 90)
    unreliable_car = UnreliableCar("Unreliable", 100, 30)

    # Test reliability behaviour over many drive attempts
    reliable_successes = 0
    unreliable_successes = 0

    for _ in range(100):
        if reliable_car.drive(1) > 0:
            reliable_successes += 1
        if unreliable_car.drive(1) > 0:
            unreliable_successes += 1

    print(f"Reliable car drove successfully {reliable_successes} times out of 100")
    print(f"Unreliable car drove successfully {unreliable_successes} times out of 100")

    print("\nIf the reliable car is MUCH higher than the unreliable car, it's working.")


if __name__ == "__main__":
    main()