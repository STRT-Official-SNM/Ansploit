from rich import print
from rich.console import Console
from rich.style import Style
from rich.layout import Layout
import time

console = Console(width=100)

main_msg = Style(color="blue", blink=True, bold=True)

print("Exploit main menu") 

console.print("Exploit main menu", style=main_msg, justify="center")

with console.status(" loading exploits", spinner="aesthetic"):
    time.sleep(2)

print("""
    """)

console.print("Enter the serial number of the attack to perform", style="red", justify="center")
