"""
CP1404 Practical
Data file
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly."""
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Load data from file formatted like: code,lecturer,number_of_students."""
    subject = []
    input_file = open(filename)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject.append(parts)
    input_file.close()
    return subject


def display_subjects(subjects):
    """Display subject data nicely."""
    for subject in subjects:
        print("{} is taught by {:12} and has {:3} students".format(*subject))


main()
