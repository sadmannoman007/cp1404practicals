"""CP1404 Practical 3 — String formatting."""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

# T-1 — f-string with currency formatting (rounded to whole dollars)
print(f"{year} {name} for about ${cost:,.0f}!")

# T-2 — powers of 2 with alignment
for exponent in range(11):  # 0 to 10
    power = 2 ** exponent
    # :>2 means width 2, right aligned for exponent; :>5 means width 5 for power
    print(f"2 ^ {exponent:>2} is {power:>5}")
