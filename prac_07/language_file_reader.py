"""
CP1404-Practical
"""

import csv
from collections import namedtuple

from prac_07.programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []

    # Open file for reading
    in_file = open('languages.csv', 'r')

    # Consume header line
    in_file.readline()

    # Read remaining lines
    for line in in_file:
        parts = line.strip().split(',')

        # Correct CSV layout:
        # 0=name, 1=typing, 2=reflection, 3=year, 4=pointer_arithmetic
        name = parts[0]
        typing = parts[1]
        reflection = parts[2] == "Yes"
        year = int(parts[3])
        pointer_arithmetic = parts[4] == "Yes"

        # Construct object
        language = ProgrammingLanguage(name, typing, reflection, pointer_arithmetic, year)

        languages.append(language)

    in_file.close()

    # Display languages using __str__()
    for language in languages:
        print(language)


main()


def using_csv():
    """Language file reader version using the csv module."""
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()  # Skip header
    reader = csv.reader(in_file)
    for row in reader:
        print(row)
    in_file.close()


# using_csv()


def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)

    # Defined *in correct column order*
    Language = namedtuple('Language', 'name typing reflection year pointer_arithmetic')

    reader = csv.reader(in_file)
    for row in reader:
        language = Language._make(row)
        print(repr(language))
    in_file.close()


# using_namedtuple()


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    Language = namedtuple('Language', 'name typing reflection year pointer_arithmetic')

    in_file = open("languages.csv", "r")
    in_file.readline()

    for language in map(Language._make, csv.reader(in_file)):
        print(f"{language.name} was released in {language.year}")
        print(repr(language))


# using_csv_namedtuple()
