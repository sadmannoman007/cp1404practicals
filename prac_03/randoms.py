"""CP1404 Practical — random module."""

import random

# Test 1
print(random.randint(5, 20))
# Smallest possible: 5
# Largest possible: 20

# Test 2
print(random.randrange(3, 10, 2))
# Smallest possible: 3
# Largest possible: 9
# Could it produce 4? No (step=2 gives 3, 5, 7, 9)

# Test 3
print(random.uniform(2.5, 5.5))
# Smallest possible: 2.5
# Largest possible: 5.5

# Random number between 1 and 100 inclusive
print(random.randint(1, 100))
