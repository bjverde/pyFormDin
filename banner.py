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

console = Console()

def print_banner():
    """
    Exibe um banner bonito no terminal usando Rich.
    """
    # Cria o conteúdo do painel
    content = Text()
    content.append(f"pyDefi v{__version__}\n", style="bold cyan")
    content.append(f"{__description__}\n", style="yellow")
    content.append(f"Autor: {__author__}\n", style="green")
    content.append(f"GitHub: {__github__}", style="green")

    # Cria o painel com título e borda estilizada
    panel = Panel(
        Align.center(content),
        title="[bold magenta]pyDefi[/]",
        border_style="bright_blue",
        padding=(1, 2)
    )

    console.print(panel)
    print()