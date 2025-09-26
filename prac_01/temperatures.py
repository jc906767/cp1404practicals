"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
#prints the input menu
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)

get_temperature = input(">>> ").upper()
while get_temperature != "Q":
    if get_temperature == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif get_temperature == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)  # F to C = 5/9*(F-32)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    get_temperature = input(">>> ").upper()
print("Thank you.")