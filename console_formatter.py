# pyDefi/utils/banner.py
import sys
import os

# Adiciona o diretório pai ao sys.path para importar __about__
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from __about__ import __version__, __author__, __description__,__github__

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