"""
CP1404-Practical
Reads guitars from CSV, displays them, sorts them, lets the user add new guitars,
and then writes all guitars back to the CSV file.
"""

from guitar import Guitar


def main():
    """Run the More Guitars program."""
    guitars = load_guitars()

    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    # Sort by year: oldest → newest
    guitars.sort()
    print("\nGuitars sorted by year (oldest → newest):")
    display_guitars(guitars)

    # Add new guitars
    print("\nAdd new guitars (press Enter for name to stop):")
    new_guitars = add_new_guitars()
    guitars.extend(new_guitars)

    # Save all guitars
    save_guitars(guitars)
    print("\nGuitars have been saved to guitars.csv")


def load_guitars():
    """Load guitars from CSV."""
    guitars = []
    with open("guitars.csv", "r", encoding="utf-8") as in_file:
        for line in in_file:
            line = line.strip()
            if not line or line.startswith("Name,Year,Cost"):
                continue
            name, year, cost = line.split(",")
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a numbered list of guitars."""
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")


def add_new_guitars():
    """Ask user for new guitars until blank name entered."""
    new_guitars = []
    name = input("Name: ").strip()
    while name != "":
        year = get_valid_int("Year: ")
        cost = get_valid_float("Cost: $")
        new_guitars.append(Guitar(name, year, cost))
        name = input("Name: ").strip()
    return new_guitars


def save_guitars(guitars):
    """Write all guitars back to CSV file."""
    with open("guitars.csv", "w", encoding="utf-8") as out_file:
        print("Name,Year,Cost", file=out_file)
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


def get_valid_int(prompt):
    """Validate integer input."""
    value = input(prompt)
    while True:
        try:
            return int(value)
        except ValueError:
            print("Invalid input; enter a valid number.")
            value = input(prompt)


def get_valid_float(prompt):
    """Validate float input."""
    value = input(prompt)
    while True:
        try:
            return float(value)
        except ValueError:
            print("Invalid input; enter a valid number.")
            value = input(prompt)


if __name__ == "__main__":
    main()
