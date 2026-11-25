import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# usage: python diwali_card.py [name] [output svg file]
name = sys.argv[1] if len(sys.argv) > 1 else "Friend"
out = sys.argv[2] if len(sys.argv) > 2 else "diwali_card.svg"

console = Console(record=True, width=50)

table = Table(show_header=True, header_style="bold orange1")
table.add_column("Day")
table.add_column("What happens")
table.add_row("1", "Dhanteras")
table.add_row("2", "Naraka Chaturdashi")
table.add_row("3", "Lakshmi Puja")
table.add_row("4", "Govardhan Puja")
table.add_row("5", "Bhai Dooj")

console.print(Panel(f"Happy Diwali, [bold red]{name}[/bold red]!", border_style="gold1"))
console.print(table)

console.save_svg(out, title="Diwali card")
print("saved", out)
