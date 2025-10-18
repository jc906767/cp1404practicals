"""
CP1404/CP5632 Practical
Hex colour code lookup program
"""

COLOUR_CODES = {
    "aliceblue":"#f0f8ff",
    "red":"#ff0000",
    "orange":"#ffa500",
    "yellow":"#ffff00",
    "green":"#008000",
    "blue":"#0000ff",
    "indigo":"#4b0082",
    "violet":"#ee82ee"
}
print(COLOUR_CODES)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        print(f"{colour_name.title()} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
