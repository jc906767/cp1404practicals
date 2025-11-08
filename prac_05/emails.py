"""
CP1404/CP5632 Practical
Emails
Estimate: 25 minutes
Actual:   23 minutes
"""

def main():
    """Store users' emails and names, then print them."""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirm not in ("", "y"):
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a name from an email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
