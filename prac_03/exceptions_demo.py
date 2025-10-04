"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   -> If the user enters something that cannot be converted to an integer
      (e.g. typing "abc" or "5.5").
2. When will a ZeroDivisionError occur?
   -> If the user enters 0 as the denominator and the program tries to divide by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   -> Yes. Check that the denominator is not zero before dividing.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator == 0:
        print("Cannot divide by zero! Please enter a non-zero denominator.")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
