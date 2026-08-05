import os

def clear_screen():
    """Clear the terminal screen on Windows, macOS and Linux"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")