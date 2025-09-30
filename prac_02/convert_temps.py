"""
CP1404 - Convert temperatures between Fahrenheit and Celsius
Includes a function to create an initial random data file.
"""

import random

MIN_TEMP = -200
MAX_TEMP = 200


def main():
    """Convert input file of one temperature unit to output file of another unit."""
    conversion = input("Convert (F to C / C to F)? ").strip().upper()
    with open("temps_input.txt", "r") as input_file, open("temps_output.txt", "w") as output_file:
        for line in input_file:
            value = float(line)
            if conversion == "F TO C":
                result = convert_fahrenheit_to_celsius(value)
            else:
                result = convert_celsius_to_fahrenheit(value)
            print(result, file=output_file)
    print("Conversion completed! Results in temps_output.txt")


def create_input_file(quantity):
    """Write a given number of random temperatures to the input file."""
    with open("temps_input.txt", "w") as temperatures_file:
        for _ in range(quantity):
            temperature = random.uniform(MIN_TEMP, MAX_TEMP)
            print(temperature, file=temperatures_file)


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)


if __name__ == "__main__":
    main()
