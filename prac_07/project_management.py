"""
Project Management Program – CP1404 Do-from-scratch Exercise
Menu:
  L)oad projects
  S)ave projects
  D)isplay projects
  F)ilter projects by date
  A)dd new project
  U)pdate project
  Q)uit

Design notes:
- Load default 'projects.txt' on start, then show menu.
- On quit, ask to save to default file.
- Use datetime for start dates.
- Sorting by priority for display groups; by date for filter view.
- Single SRP-style load/save functions used by both default and custom paths.

Structure: module docstring → imports → CONSTANTS → main() → helpers → guard.
"""
from __future__ import annotations

from pathlib import Path
from datetime import datetime, date
from typing import List

from project import Project

# ----- CONSTANTS -----
DEFAULT_FILE = Path("projects.txt")
DATE_FMT = "%d/%m/%Y"  # dd/mm/yyyy


def main() -> None:
    """Run the Project Management Program."""
    print("Welcome to Pythonic Project Management")
    projects: List[Project] = []

    # Load defaults if present
    if DEFAULT_FILE.exists():
        projects = load_projects(DEFAULT_FILE)
        print(f"Loaded {len(projects)} projects from {DEFAULT_FILE.name}")
    else:
        print("No default file found. You'll start with an empty project list.")

    MENU = (
        "- (L)oad projects\n"
        "- (S)ave projects\n"
        "- (D)isplay projects\n"
        "- (F)ilter projects by date\n"
        "- (A)dd new project\n"
        "- (U)pdate project\n"
        "- (Q)uit"
    )

    choice = input(MENU + "\n>>> ").strip().lower()
    while choice != "q":
        if choice == "l":
            filename_text = input("Filename to load: ").strip()
            filename = Path(filename_text) if filename_text else DEFAULT_FILE
            try:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            except FileNotFoundError:
                print("File not found.")
        elif choice == "s":
            filename_text = input("Filename to save: ").strip()
            filename = Path(filename_text) if filename_text else DEFAULT_FILE
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_string = input("Show projects that start after date (dd/mm/yy or dd/mm/yyyy): ").strip()
            try:
                filter_date = parse_date_loose(date_string)
                filtered = [p for p in projects if p.start_date >= filter_date]  # include same-day like sample
                for p in sorted(filtered, key=lambda x: x.date_key()):
                    print(p)
            except ValueError:
                print("Invalid date format.")
        elif choice == "a":
            print("Let's add a new project")
            new = input_new_project()
            if new is not None:
                projects.append(new)
                print("Project added.")
        elif choice == "u":
            if not projects:
                print("No projects to update.")
            else:
                for i, p in enumerate(projects):
                    print(f"{i} {p}")
                try:
                    index = int(input("Project choice: ").strip())
                    project = projects[index]
                except (ValueError, IndexError):
                    print("Invalid choice.")
                else:
                    print(project)
                    percent_text = input("New Percentage: ").strip()
                    priority_text = input("New Priority: ").strip()
                    new_percent = int(percent_text) if percent_text != "" else None
                    new_priority = int(priority_text) if priority_text != "" else None
                    project.update(new_percent, new_priority)
        else:
            print("Invalid choice")

        choice = input(MENU + "\n>>> ").strip().lower()

    # Quit – ask to save to default file
    save_choice = input(f"Would you like to save to {DEFAULT_FILE.name}? ").strip().lower()
    if save_choice in {"y", "yes"}:
        save_projects(DEFAULT_FILE, projects)
        print(f"Saved {len(projects)} projects to {DEFAULT_FILE.name}")
    print("Thank you for using custom-built project management software.")


# ----- HELPERS -----
def load_projects(path: Path) -> List[Project]:
    """Load projects from a tab-delimited file with header; return a list of Project objects."""
    projects: List[Project] = []
    with path.open("r", encoding="utf-8") as f:
        header = f.readline()  # consume header
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Expected fields: Name \t Start Date \t Priority \t Cost Estimate \t Completion Percentage
            name, date_text, priority_text, cost_text, percent_text = line.split("\t")
            start = parse_date_loose(date_text)
            project = Project(
                name=name,
                start_date=start,
                priority=int(priority_text),
                cost_estimate=float(cost_text),
                completion_percent=int(percent_text),
            )
            projects.append(project)
    return projects


def save_projects(path: Path, projects: List[Project]) -> None:
    """Save projects to a tab-delimited file with header."""
    with path.open("w", encoding="utf-8") as f:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=f)
        for p in projects:
            start_text = p.start_date.strftime(DATE_FMT)
            print(f"{p.name}\t{start_text}\t{p.priority}\t{p.cost_estimate}\t{p.completion_percent}", file=f)


def display_projects(projects: List[Project]) -> None:
    """Display incomplete and completed project groups, both sorted by priority ascending."""
    incomplete = sorted([p for p in projects if not p.is_complete()], key=lambda x: x.priority_key())
    complete = sorted([p for p in projects if p.is_complete()], key=lambda x: x.priority_key())
    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")
    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


def input_new_project() -> Project | None:
    """Prompt for new Project fields and return a Project, or None if cancelled."""
    name = input("Name: ").strip()
    if name == "":
        print("Cancelled.")
        return None
    date_text = input("Start date (dd/mm/yy or dd/mm/yyyy): ").strip()
    priority_text = input("Priority: ").strip()
    cost_text = input("Cost estimate: $").strip().lstrip("$")
    percent_text = input("Percent complete: ").strip()
    try:
        start = parse_date_loose(date_text)
        priority = int(priority_text)
        cost = float(cost_text)
        percent = int(percent_text)
    except ValueError:
        print("Invalid input; project not added.")
        return None
    return Project(name=name, start_date=start, priority=priority, cost_estimate=cost, completion_percent=percent)


def parse_date_loose(text: str) -> date:
    """Parse dd/mm/yy or dd/mm/yyyy into a date object."""
    text = text.strip()
    # try dd/mm/yyyy
    try:
        return datetime.strptime(text, "%d/%m/%Y").date()
    except ValueError:
        # try dd/mm/yy
        return datetime.strptime(text, "%d/%m/%y").date()


if __name__ == "__main__":
    main()
