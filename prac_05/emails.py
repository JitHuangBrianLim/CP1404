"""
Estimate: 20 mins
Actual: 31 mins
"""

def main():
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = get_email_name(email)
        check_correct = input(f"Is your name {name}? (Y/n)")
        if check_correct.upper() != "Y" and check_correct != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_email_name(email):
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()