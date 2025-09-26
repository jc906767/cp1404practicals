"""
CP1404/CP5632 - Practical
Program for practicing Menus
"""
#gets the user's name
get_name = input("What is your name: ")

#creates the menu and print it
MENU = """H - Hello
G - Goodbye
Q - Quit"""
print(MENU)

get_menu_choice = input(">>> ").upper()

#checks the user's menu choice and starts the loop if the input isn't 'Q'
while get_menu_choice != "Q":
    #prints Hello name
    if get_menu_choice == "H":
        print("Hello", get_name)
    #prints Goodbye name
    elif get_menu_choice == "G":
        print("Goodbye", get_name)
    #informs the user if an invalid input is used
    else:
        print("Invalid choice")
    print(MENU)
    get_menu_choice = input(">>> ").upper()
#informs the user that the program has ended
print("Menu selection finished.")