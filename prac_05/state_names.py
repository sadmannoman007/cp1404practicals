"""
CP1404/CP5632 Practical
State names in a dictionary
File has been reformatted and updated to meet practical requirements
"""

# Constant dictionary of Australian state abbreviations and their full names
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

# Print all states and names neatly lined up
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

# Ask the user for a short state code (case-insensitive)
state = input("Enter short state: ").strip().upper()
while state != "":
    # Use EAFP (Easier to Ask Forgiveness than Permission) approach
    try:
        print(f"{state} is {CODE_TO_NAME[state]}")
    except KeyError:
        print("Invalid short state")
    state = input("Enter short state: ").strip().upper()
