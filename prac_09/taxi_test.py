"""
CP1404/CP5632 Practical
Taxi test
"""

from taxi import Taxi


def main():
    # 1. Create a taxi object WITHOUT passing price_per_km (class variable)
    my_taxi = Taxi("Prius 1", 100)

    # 2. Drive the taxi 40 km
    my_taxi.drive(40)

    # 3. Print the taxi details and current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # 4. Restart fare, then drive 100 km
    my_taxi.start_fare()
    my_taxi.drive(100)

    # 5. Print details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
