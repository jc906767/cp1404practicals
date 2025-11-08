"""
Project Management Program

Estimate: 1 hour 45 minutes
Actual: About 2 hours

Menu-driven program to load/save tab-delimited projects and manage them using a
list of Project objects. Follows CP1404 patterns and SRP/DRY.
"""

from __future__ import annotations

import csv
from datetime import datetime, date
from pathlib import Path
from typing import List

from project import Project, DATE_FORMAT, date_from_text

DEFAULT_FILENAME = "projects.txt"
MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
>>> """


def main() -> None:
    """Run the Project Management menu program."""
    projects: List[Project] = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    choice = input(MENU).strip().upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load from: ").strip()
            projects = load_projects(filename)
            print(f"{len(projects)} projects loaded from {filename}")
        elif choice == "S":
            filename = input("Filename to save to: ").strip()
            save_projects(filename, projects)
            print(f"{len(projects)} projects saved to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid choice")
        choice = input(MENU).strip().upper()

    # Quit: offer to save to default file
    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip().upper()
    if save_choice == "Y":
        save_projects(DEFAULT_FILENAME, projects)
        print(f"Saved {len(projects)} projects to {DEFAULT_FILENAME}")
    print("Thank you for using the Project Management Program.")


# ---------------------------- Load / Save ---------------------------------- #
def load_projects(filename: str) -> List[Project]:
    """Load projects from a tab-delimited file with a header row."""
    projects: List[Project] = []
    path = Path(filename)
    if not path.exists():
        print(f"File not found: {filename} (starting with an empty list)")
        return projects

    with path.open("r", encoding="utf-8", newline="") as in_file:
        reader = csv.reader(in_file, delimiter="\t")
        header = next(reader, None)  # discard header
        if header is None:
            return projects
        for row in reader:
            if not row:
                continue
            # Client code converts strings -> types (per brief)
            name = row[0]
            start_date = date_from_text(row[1])
            priority = int(row[2])
            cost_estimate = float(row[3])
            completion = int(row[4])
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
    return projects


def save_projects(filename: str, projects: List[Project]) -> None:
    """Save projects to a tab-delimited file with a header row."""
    path = Path(filename)
    with path.open("w", encoding="utf-8", newline="") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow(project.as_tab_fields())


# ---------------------------- Displaying ----------------------------------- #
def display_projects(projects: List[Project]) -> None:
    """Display incomplete then completed projects, each sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete:
        print(f"  {project}")


def filter_projects_by_date(projects: List[Project]) -> None:
    """Ask for a date and display projects that start after it, sorted by date."""
    date_text = input(f"Show projects that start after date (dd/mm/yyyy): ").strip()
    try:
        threshold = datetime.strptime(date_text, DATE_FORMAT).date()
    except ValueError:
        print("Invalid date format")
        return

    filtered = sorted([p for p in projects if p.start_date > threshold],
                      key=lambda p: p.start_date)
    for project in filtered:
        print(project)


# ---------------------------- Modifying ------------------------------------ #
def add_new_project(projects: List[Project]) -> None:
    """Prompt for project fields and append to the list."""
    name = input("Name: ").strip()
    date_text = input(f"Start date (dd/mm/yyyy): ").strip()
    try:
        start = datetime.strptime(date_text, DATE_FORMAT).date()
    except ValueError:
        print("Invalid date format")
        return

    try:
        priority = int(input("Priority: ").strip())
        estimate = float(input("Cost estimate: $").strip())
        completion = int(input("Percent complete: ").strip())
    except ValueError:
        print("Invalid number")
        return

    projects.append(Project(name, start, priority, estimate, completion))
    print("Project added.")


def update_project(projects: list[Project]) -> None:
    """Choose a project, then modify completion % and/or priority (blank to keep)."""
    if not projects:
        print("No projects to update.")
        return

    # Show all projects with their indices
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        index = int(input("Project choice: ").strip())
        chosen = projects[index]
    except (ValueError, IndexError):
        print("Invalid choice")
        return

    print(chosen)

    # Ask for new completion and/or priority
    new_completion_text = input("New Percentage: ").strip()
    if new_completion_text:
        try:
            chosen.completion_percentage = int(new_completion_text)
        except ValueError:
            print("Invalid completion value.")

    new_priority_text = input("New Priority: ").strip()
    if new_priority_text:
        try:
            chosen.priority = int(new_priority_text)
            chosen.sort_index = chosen.priority  # keep ordering consistent
        except ValueError:
            print("Invalid priority value (ignored).")

    print("Project updated:")
    print(chosen)



# ---------------------------- Utilities ------------------------------------ #
def _format_date(d: date) -> str:
    """Format a date using the program's standard format."""
    return d.strftime(DATE_FORMAT)


if __name__ == "__main__":
    main()
