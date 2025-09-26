"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

#Main function where the menu is shown and conversion choices are made
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
            print("Invalid option, please choose an option from the menu")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

#Function that converts Celcius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return f"Result: {fahrenheit:.2f} F"

#Function that converts Fahrenheit to Celcius
def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return f"Result: {celsius:.2f} C"

main()