import os
import time
from rich import print
from rich.console import Console
from rich.style import Style
from rich.layout import Layout


console = Console(width=100)

Layout(name='footer', size=10)

wl_msg = Style(color="blue", blink=False, bold=True)

os.system("clear")

console.print("AnSploit", style=wl_msg, justify="center")

time.sleep(2)

with console.status(" [Starting Ansploit framework]", spinner="point"):
    time.sleep(3)
    
print("Starting Ansploit framework")
print("Sucessfully started")

time.sleep(1)

os.system("clear")

os.system("python main.py")




#ip = input("Please enter local or private IP of victim : ")
#os.system("adb tcpip 5555")
#os.system("adb connect "+ip+":5555")
#print("Connection established")
