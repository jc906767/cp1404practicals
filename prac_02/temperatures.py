"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(celsius_to_fahrenheit(celsius))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(fahrenheit_to_celsius(fahrenheit))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"Result: {fahrenheit:.2f} F"


def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return f"Result: {celsius:.2f} C"

main()