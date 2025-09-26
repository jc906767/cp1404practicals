"""
CP1404
Program that asks the user for a password and then prints it back as a line of stars.
"""


min_password_length = 6

password = input("What is your password: ")

while len(password) < min_password_length:
    print(f"Your password must be at least {min_password_length} characters long.")
    password = input("What is your password: ")

print("*" * len(password))
