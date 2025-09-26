"""
CP1404
Program that asks the user for a password and then prints it back as a line of stars.
"""
#Start the main function
def main():
    MIN_PASSWORD_LENGTH = 6
    password = get_password(MIN_PASSWORD_LENGTH)

#Function that collects user's password and checks the length
def get_password(MIN_PASSWORD_LENGTH):
    user_password = input("What is your password? ")
    while len(user_password) < MIN_PASSWORD_LENGTH:
        print(f"Your password must be at least {MIN_PASSWORD_LENGTH} characters long.")
        user_password = input("What is your password? ")

    star_printer(len(user_password))

#Function that converts the user's password to stars
def starprinter(star_length):
    print("*" * star_length)

#Call the main function
main()