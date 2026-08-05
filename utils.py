import os

def clear_screen():
    """Clear the terminal screen on Windows, macOS and Linux"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
        
def select_account():
    """Prompt the user to select an account and return the selected account or None if they choose to go back."""
    while True:
        print("1. Checking\n2. Savings\n3. Back")
        
        try:
            user_selection = int(input("Enter the number corresponding to your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")
            continue
            
        if user_selection == 1:
            return "Checking"
        elif user_selection == 2:
            return "Savings"
        elif user_selection == 3:
            return None
        else:
            print("\nInvalid selection, please try again")
            continue
        
def get_balance_key(account):
    """Return the balance key for the given account type."""
    if account == "Checking":
        return "CheckingBalance"
    elif account == "Savings":
        return "SavingsBalance"
    else:
        raise ValueError("Invalid account type. Must be 'Checking' or 'Savings'.")