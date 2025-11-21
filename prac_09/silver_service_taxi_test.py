"""
CP1404/CP5632 Practical
Silver Service Taxi test
"""

from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Test Taxi", 100, 2)

    taxi.start_fare()  # <-- IMPORTANT
    taxi.drive(18)

    fare = taxi.get_fare()
    print("Price per km =", taxi.price_per_km)
    print("Current fare distance =", taxi.current_fare_distance)
    print("Fare =", fare)

    assert abs(fare - 48.8) < 0.01, f"Fare calculation incorrect: got {fare}"


    print("Test passed!")

if __name__ == "__main__":
    main()
