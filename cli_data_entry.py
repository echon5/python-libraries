"""Collect and save a small, curated fairy tale dataset in the terminal."""
import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

# Create the Rich console and choose where the data will be saved.
console = Console()
output_file = Path("curated_fairy_tales.json")

# Example records shown to the user before they add their own.
tales = [
    {
        "title": "Cinderella",
        "origin": "France (Charles Perrault's version)",
        "first_published_year": 1697,
        "cultural_note": "Versions of this story appear across many cultures, "
        "usually about kindness being rewarded.",
    },
    {
        "title": "Hansel and Gretel",
        "origin": "Germany (Brothers Grimm)",
        "first_published_year": 1812,
        "cultural_note": "Reflects fears of famine and abandonment, "
        "with children outwitting a threatening adult.",
    },
]


def display_tales(tale_records):
    """Show a list of fairy tale records in a Rich table."""
    table = Table(title="Curated Fairy Tales")
    table.add_column("Title", style="magenta")
    table.add_column("Origin", style="green")
    table.add_column("First Published", style="cyan")
    table.add_column("Cultural Note")
    for tale in tale_records:
        table.add_row(
            tale["title"],
            tale["origin"],
            str(tale["first_published_year"]),
            tale["cultural_note"],
        )
    console.print(table)


def ask_required(prompt):
    """Keep asking until the user types something (not blank)."""
    while True:
        answer = console.input(prompt).strip()
        if answer:
            return answer
        console.print("[red]This field can't be empty. Try again.[/red]")


def ask_year(prompt):
    """Keep asking until the user types a valid year."""
    while True:
        answer = console.input(prompt).strip()
        if answer.isdigit() and 1 <= int(answer) <= 2100:
            return int(answer)
        console.print("[red]Please enter a year using digits, like 1812.[/red]")


def collect_tale():
    """Ask for each field and return one fairy tale record."""
    return {
        "title": ask_required("[bold]Fairy tale title:[/bold] "),
        "origin": ask_required(
            "[bold]Culture or country of origin (and collector, if known):[/bold] "
        ),
        "first_published_year": ask_year(
            "[bold]Year first published or written down:[/bold] "
        ),
        "cultural_note": ask_required(
            "[bold]What does this tale show about its culture?[/bold] "
        ),
    }


def confirm_tale(tale):
    """Show one record and return True if the user says it's correct."""
    console.print("\n[bold cyan]Please review your entry:[/bold cyan]")
    display_tales([tale])
    answer = console.input("Is this correct? Enter yes or no: ").strip().lower()
    return answer in ["yes", "y"]


console.print("[bold cyan]Here is some example data:[/bold cyan]")
display_tales(tales)

# Keep collecting tales until the user says they're done.
while True:
    console.print("\n[bold cyan]Add a new fairy tale[/bold cyan]")
    new_tale = collect_tale()

    # If the entry is wrong, re-enter it until the user confirms.
    while not confirm_tale(new_tale):
        console.print("[yellow]Let's enter the fairy tale again.[/yellow]\n")
        new_tale = collect_tale()

    tales.append(new_tale)
    console.print("[green]Fairy tale added.[/green]")

    another = console.input("\nAdd another fairy tale? Enter yes or no: ").strip().lower()
    if another not in ["yes", "y"]:
        break

# Save everything to a JSON file only after the user has confirmed their entries.
output_file.write_text(json.dumps(tales, indent=4), encoding="utf-8")

console.print("\n[bold green]Your fairy tale data has been saved.[/bold green]")
console.print(f"File saved at {output_file.resolve()}")