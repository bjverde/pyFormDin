from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text

class ConsoleFormatter:
    def __init__(self):
        self.console = Console()

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

    @staticmethod
    def print_error(msg):
        content = Text(f"❌ {msg}", style="bold red")
        panel = Panel(
            Align.center(content),
            title="[bold red]Erro[/]",
            border_style="red",
            padding=(1, 2)
        )
        console = Console()
        console.print(panel)
        print()        