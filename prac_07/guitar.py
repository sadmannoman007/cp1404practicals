"""
CP1404/CP5632 Practical - More Guitars
Defines the Guitar class and comparison behavior for sorting by year.
Structure: module docstring → class → helpers (none) → no guard needed.
"""


class Guitar:
    """Represent a guitar with name, year, and cost."""

    def __init__(self, name: str, year: int, cost: float):
        """Construct a Guitar from given values."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self) -> str:
        """Return a user-friendly string for this guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __repr__(self) -> str:
        """Return a precise string representation for debugging."""
        return f"Guitar(name={self.name!r}, year={self.year!r}, cost={self.cost!r})"

    def __lt__(self, other: "Guitar") -> bool:
        """
        Return True if this guitar is older (smaller year) than the other.
        Enables sorting by year ascending (oldest → newest).
        """
        return self.year < other.year
