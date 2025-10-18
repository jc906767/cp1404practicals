"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
# NOTE: auto code reformatting adds the spaces back have no clue why or how to change that

CODE_TO_NAME = {"QLD":"Queensland",
                "NSW":"New South Wales",
                "NT":"Northern Territory",
                "WA":"Western Australia",
                "ACT":"Australian Capital Territory",
                "VIC":"Victoria",
                "TAS":"Tasmania",
                "SA":"South Australia"}
print(CODE_TO_NAME)

# Print all states and names neatly lined up
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        # Try to access the dictionary key directly
        state_name = CODE_TO_NAME[state_code]
        print(f"{state_code} is {state_name}")
    except KeyError:
        # Handle the case where the key doesn't exist
        print("Invalid short state")
    state_code = input("Enter short state: ") #could also add .upper() here