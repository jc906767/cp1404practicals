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
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            user_score = input("Please enter a score between 0 and 100: ")
            while not user_score.isdigit() or not (0 <= int(user_score) <= 100):
                print("Invalid score")
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
            print("Invalid option")

        print(menu)
        choice = input(">>> ").upper()

    print("Farewell.")





main()