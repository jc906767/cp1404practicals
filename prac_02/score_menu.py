"""
CP1404/CP5632 - Practical
Program that uses a menu to determine score status
"""
def main():
    MENU = """G - Get a valid score
P - Print result
S - Show stars
Q - Quit"""
    score = None
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            user_score = input("Please enter a score between 0 and 100: ")
            while int(user_score) < 0 or int(user_score) > 100:
                print("That score is invalid.")
                user_score = input("Please enter a score between 0 and 100: ")
            score = int(user_score)
        elif choice == "P":
            if score is None:
                print("You must choose G first.")
            else:
                print(f"Result: {score_result(score)}")
        elif choice == "S":
            if score is None:
                print("You must choose G first.")
            else:
                print(print_stars(score))
        else:
            print("Invalid option, please choose an option from the menu.")

        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell.")

def score_result(score):
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


def print_stars(number_of_stars):
    return "*" * number_of_stars

main()