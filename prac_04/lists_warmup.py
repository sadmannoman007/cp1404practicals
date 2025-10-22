"""
CP1404 Lists "warm-up"
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# --------------------------------------------
# What values do the following expressions have?
# --------------------------------------------

# numbers[0] - 3 (the first element)
# numbers[-1] - 2 (the last element)
# numbers[3] - 1 (the fourth element, since index starts at 0)
# numbers[:-1] - [3, 1, 4, 1, 5, 9] (all elements except the last one)
# numbers[3:4] - [1] (slice containing only the element at index 3)
# 5 in numbers - True (5 exists in the list)
# 7 in numbers - False (7 is not in the list)
# "3" in numbers - False (string "3" ≠ integer 3)
# numbers + [6, 5, 3] - [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] (new combined list)

# --------------------------------------------
# Write Python expressions to achieve the following
# --------------------------------------------

# Change the first element of numbers to "ten"
numbers[0] = "ten"

# Change the last element of numbers to 1
numbers[-1] = 1

# Get all the elements from numbers except the first two
print(numbers[2:])  # Expected: [4, 1, 5, 9, 1]

# Check if 9 is an element of numbers
print(9 in numbers)  # Expected: True
