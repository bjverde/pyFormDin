import os

from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule
from rich.align import Align
from rich.text import Text

class ConsoleFormatter:
    def __init__(self):
        self.console = Console()
        self.orange_btc = "\033[38;2;255;165;0m"

    def clear(self):
        import os
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def print_banner(self, versao, description, autor, link):
        content = Text()
        content.append(f"pyDefi v{versao}\n", style="bold cyan")
        content.append(f"{description}\n", style="yellow")
        content.append(f"Autor: {autor}\n", style="green")
        content.append(f"Link: {link}", style="green")

        panel = Panel(
            Align.center(content),
            title="[bold magenta]pyDefi[/]",
            border_style="bright_blue",
            padding=(1, 2)
        )
        self.console.print(panel)
        print()

    def print_msg(self, msg, styleText, icon, showIcon=True):
        icon = icon if showIcon else ""
        console = Console()
        console.print(Rule())  # Linha simples
        if isinstance(msg, (list, tuple)):
            for linha in msg:
                content = Text(f"{icon} {linha}", style=styleText, justify="left")
                console.print(content)
        else:
            content = Text(f"{icon} {msg}", style=styleText, justify="left")
            console.print(content)
        print()

    def print_ok(self, msg, showIcon=True):
        self.print_msg(msg, "bold green", "✅", showIcon)

    def print_info(self, msg, showIcon=True):
        self.print_msg(msg, "bold blue", "ℹ️", showIcon)

    def print_warning(self, msg, showIcon=True):
        self.print_msg(msg, "bold yellow", "⚠️", showIcon)

    def print_error(self, msg, showIcon=True):
        self.print_msg(msg, "bold red", "❌", showIcon)