import os
import utils

DATES_PER_PAGE = 10
MAIN_MENU_OPTION = "M"

def get_transaction_dates(user):
    """Return a list of dates for which transaction files exist for the user."""
    transaction_dir = f"transactions/{user['UserID']}"
    if not os.path.exists(transaction_dir):
        return []
    dates = []
    for filename in os.listdir(transaction_dir):
        if filename == "counter.txt":
            continue
        date_only = filename.split(".")[0]  # Extracts the date part from the filename
        dates.append(date_only)
    dates.sort(reverse=True)  # Sort dates in descending order
    return dates

def display_transaction_dates(user):
    """Display a paginated list of transaction dates for the user."""
    utils.clear_screen()
    page_number = 1
    dates = get_transaction_dates(user)
    if not dates:
        print("\nNo transaction history available.")
        return
    while True:
        utils.clear_screen()
        start = (page_number - 1) * DATES_PER_PAGE
        end = start + DATES_PER_PAGE
        menu_option_number = 1
        current_dates = dates[start:end]
        print("=============TRANSACTION HISTORY=============\n")
        for transaction_date in current_dates:
            print(f"{menu_option_number}. {transaction_date}")
            menu_option_number += 1
        
        if len(dates) > end:
            print("N. Next")
        if page_number > 1:
            print("P. Previous")
        print("M. Main Menu")
        
        choice = input("What would you like to do: ").upper()
        if choice == "N" and len(dates) > end:
            page_number += 1
            continue
        elif choice == "P" and page_number > 1:
            page_number -= 1
            continue
        elif choice == "M":
            return
        else:
            try:
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(current_dates):
                    selected_date = current_dates[choice_index]
                    view_transactions(user, selected_date)
                else:
                    input("Invalid option. Press enter to try again")
            except ValueError:
                input("Invalid option. Press enter to try again")
def view_transactions(user, transaction_date):
    """Display the transactions for a specific date."""
    transaction_file = f"transactions/{user['UserID']}/{transaction_date}.txt"       #Path to the transaction file for the given date
    
    if not os.path.exists(transaction_file):
        print("\nNo transaction history available")
        return
    
    utils.clear_screen()
    print(f"=====TRANSACTIONS FOR {transaction_date}=====\n")
    with open(transaction_file, 'r') as file:
        transactions = file.readlines()
        if not transactions:
            print("No transactions recorded")
            return
        for transaction in transactions:
            print(transaction.strip())
    input("\nPress Enter to return to the transaction history menu...")