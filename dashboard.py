import utils
import transactions
import transaction_history
import transfer

def dashboard(user):
    """Function to display the user dashboard and handle user actions."""
    while True:
        utils.clear_screen()
        print("=============================")
        print("      BANK DASHBOARD")
        print("=============================")
        
        print(f"Welcome back, {user['First name']}!")
        
        print("1. View Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Logout")
        
        try:
            user_selection = int(input("What would you like to do: "))
        except ValueError:
                print("Invalid input. Please enter a number corresponding to the menu options.")    
                continue
        if user_selection == 1:
            utils.clear_screen()
            print("===========================================")
            print("ACCOUNT INFORMATION")
            print("===========================================")
            print(f"Name: {user['First name']}")
            print(f"User ID: {user['UserID']}")
            print(f"Username: {user['Username']}")
            print(f"Checking Balance: ${float(user['CheckingBalance']):,.2f}")
            print(f"Savings Balance: ${float(user['SavingsBalance']):,.2f}")
            print("===========================================")
            input("\nPress enter to return to the dashboard...")
            
        elif user_selection == 2:
            utils.clear_screen()
            transactions.user_deposit(user)
        elif user_selection == 3:
            utils.clear_screen()
            transactions.user_withdrawal(user)
        elif user_selection == 4:
            utils.clear_screen()
            transfer.user_transfer(user)
        elif user_selection == 5:
            utils.clear_screen()
            transaction_history.display_transaction_dates(user)
        elif user_selection == 6:
            utils.clear_screen()
            print("Logging out...")
            break
        else:
            print("Invalid selection, please try again")