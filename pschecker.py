import string
import getpass  # This helps us in displaying the password

def password_check():
    password = getpass.getpass("Enter the password: ")
    strength = 0
    lc = up = nc = ws = spch = 0  # Initialize all counts
    remarks = ''

    for char in password:
        if char in string.ascii_lowercase:
            lc += 1
        elif char in string.ascii_uppercase:
            up += 1
        elif char in string.whitespace:
            ws += 1
        elif char in string.digits:
            nc += 1
        else:
            spch += 1  # Count special characters

    # Password strength criteria
    if lc >= 1:
        strength += 1
    if up >= 1:
        strength += 1
    if nc >= 1:
        strength += 1
    if ws >= 1:
        strength += 1  # Include whitespace in strength calculation
    if spch >= 1:
        strength += 1

    # Strength remarks
    if strength == 1:
        remarks = 'Very weak password'
    elif strength == 2:
        remarks = 'Weak password'
    elif strength == 3:
        remarks = 'Not very weak, neither very strong'
    elif strength == 4:
        remarks = 'Strong password, but can be better'
    elif strength == 5:
        remarks = 'Very strong password!!'

    print("\nYour password has:")
    print(f"{lc} lower case letters")
    print(f"{up} upper case letters")
    print(f"{nc} digits")
    print(f"{ws} whitespaces")
    print(f"{spch} special characters")
    print(f"Password Strength: {strength}")
    print(f"Remarks: {remarks}\n")


def userpassword(newpassword=False):
    """Asks the user whether they want to continue checking passwords."""
    while True:
        choice = input("Do you want to continue entering a password (Y/N)? " if newpassword else "Do you want to check password strength (Y/N)? ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter Y or N.")


if __name__ == '__main__':  # Corrected the condition
    print("!!! Welcome to the Password Strength Checker !!!")
    
    while userpassword():
        password_check()
