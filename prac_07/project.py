"""
CP1404 Practical - Project Management Program
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion percent."""
    name: str
    start_date: date
    priority: int
    cost_estimate: float
    completion_percent: int

    # ----- Utility methods -----
    def is_complete(self) -> bool:
        """Return True if the project is complete (100%)."""
        return self.completion_percent >= 100

    def priority_key(self):
        """Return priority for sorting projects (lower = higher priority)."""
        return self.priority

    def date_key(self):
        """Return start date for sorting by date."""
        return self.start_date

    def update(self, new_percent: int | None = None, new_priority: int | None = None) -> None:
        """Update completion percent and/or priority if provided."""
        if new_percent is not None:
            self.completion_percent = new_percent
        if new_priority is not None:
            self.priority = new_priority

    def __str__(self) -> str:
        """Return a nicely formatted string for displaying a project."""
        start_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percent}%")
