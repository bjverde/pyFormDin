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

    def print_rule(self, msg=None, style=None, align="left", characters="_"):
        """
        Exibe uma linha horizontal (Rule) no console, opcionalmente com texto centralizado e estilo personalizado.

        Args:
            msg (str, optional): Texto a ser exibido na linha. Se None, apenas a linha é mostrada.
            style (str, optional): Estilo/cor da linha e do texto (ex: "bold green").
            align (str, optional): Alinhamento do texto na linha ("left", "center", "right"). Default: "left".
            characters (str, optional): Caractere(s) usados para desenhar a linha. Default: "_".
        """
        rule = Rule(msg, style=style, align=align, characters=characters)
        self.console.print(rule)

    def print_msg(self, msg, styleText, icon, showIcon=True):
        """
        Exibe uma mensagem formatada no console, com ícone, cor e alinhamento à esquerda.

        Args:
            msg (str or list/tuple): Mensagem a ser exibida. Pode ser uma string ou uma lista/tupla de strings (cada linha será impressa separadamente).
            styleText (str): Estilo/cor do texto (ex: "bold green", "bold red").
            icon (str): Ícone Unicode a ser exibido antes da mensagem (ex: "✅", "❌").
            showIcon (bool, optional): Se True, exibe o ícone; se False, omite. Default: True.

        Exibe uma linha horizontal antes da mensagem usando Rule.
        """
        icon = icon if showIcon else ""
        console = Console()
        console.print(Rule())  # Linha simples
        if isinstance(msg, (list, tuple)):
            for linha in msg:
                content = Text(f"{icon}  {linha}", style=styleText, justify="left")
                console.print(content)
        else:
            content = Text(f"{icon}  {msg}", style=styleText, justify="left")
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