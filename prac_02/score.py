"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    score = float(input("What is your score?  "))
    result = determine_score_status(score)
    print(result)

def determine_score_status(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()