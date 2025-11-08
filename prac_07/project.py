"""
Project domain model.

Estimate: 1 hour 15 minutes
Actual: <enter your actual time here>

This module defines the Project class with ordering by priority and a couple of
helpers to support the menu program.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any


DATE_FORMAT = "%d/%m/%Y"


@dataclass(order=True)
class Project:
    """A project with a start date, priority, cost estimate and completion %.

    Ordering is by priority (ascending), so lower numbers are "higher" priority.
    """
    sort_index: int = field(init=False, repr=False)
    name: str
    start_date: date
    priority: int
    cost_estimate: float
    completion_percentage: int

    def __post_init__(self) -> None:
        self.sort_index = self.priority

    # ---- Helpers --------------------------------------------------------- #
    def is_complete(self) -> bool:
        """Return True if project is fully completed."""
        return self.completion_percentage >= 100

    def as_tab_fields(self) -> list[str]:
        """Return a list of string fields suitable for tab-delimited saving."""
        return [
            self.name,
            self.start_date.strftime(DATE_FORMAT),
            str(self.priority),
            f"{self.cost_estimate:.2f}",
            str(self.completion_percentage),
        ]

    def __str__(self) -> str:
        """Readable single-line representation."""
        return (f"{self.name}, start: {self.start_date.strftime(DATE_FORMAT)}, "
                f"priority {self.priority}, estimate ${self.cost_estimate:.2f}, "
                f"completion {self.completion_percentage}%")

    # ---- Factory --------------------------------------------------------- #
    @classmethod
    def from_tab_fields(cls, fields: list[str]) -> "Project":
        """Create a Project from tab-delimited string fields (excluding header)."""
        name, date_text, priority_text, estimate_text, completion_text = fields
        start = date.strptime(date_text, DATE_FORMAT)
        raise NotImplementedError  # Guard if called incorrectly


# Compatibility helper – Python's date has no strptime, so provide one.
def date_from_text(date_text: str) -> date:
    """Parse 'd/m/YYYY' into a date object."""
    # Import locally to avoid circular import concerns in some IDEs
    from datetime import datetime
    return datetime.strptime(date_text, DATE_FORMAT).date()
