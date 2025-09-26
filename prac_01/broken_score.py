"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

#retrieve the usesr's score as a float
get_score = float(input("Enter score: "))

#re-formatted the code to use elif instead of stacked if functions
if get_score < 0:
    print("Invalid score")
elif get_score < 50:
    print("Bad")
elif get_score < 90:
    print("Passable")
elif get_score < 100:
    print("Excellent")
else:
    print("Invalid score")
