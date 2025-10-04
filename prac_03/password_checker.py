"""
CP1404 - Practical - Password Checker
Validates a user's password based on length and character-type rules.
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
IS_SPECIAL_CHARACTER_REQUIRED = True

SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Get a password from the user and validate it against the rules."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        # Note the space after the colon to match the sample output spacing
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)

    password = input("> ").strip()
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ").strip()

    # Match the sample wording exactly (no hyphen before 'character')
    print(f"Your {len(password)} character password is valid: {password}")

def is_valid_password(password):
    """Return True if password meets all rules; otherwise False."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    lower = upper = digit = special = 0
    for ch in password:
        if ch.isdigit():
            digit += 1
        elif ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
        elif ch in SPECIAL_CHARACTERS:
            special += 1

    if lower == 0 or upper == 0 or digit == 0:
        return False

    if IS_SPECIAL_CHARACTER_REQUIRED and special == 0:
        return False

    return True

if __name__ == "__main__":
    main()
