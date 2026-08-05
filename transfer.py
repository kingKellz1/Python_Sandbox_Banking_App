import storage
import datetime
import utils

def user_transfer(user):
    """Function to handle transfers between the user's account."""
    from_account = None
    to_account = None
    
    while True:
        utils.clear_screen()
        print("========== TRANSFER ==========")
        print("1. Checking\n2. Savings\n3. Back to Dashboard")
        print("=============================")
        
        try:
            user_selection = int(input("\nSelect account to transfer FROM: "))
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")    
            continue
                    
        if user_selection == 1:
            from_account = "Checking"
        elif user_selection == 2:
            from_account = "Savings"
        elif user_selection == 3:
            return # Go back to dashboard
        else:
            print("\nInvalid selection, please try again")
            print("\nPress Enter to continue...")
            continue
        
        while True:
            utils.clear_screen()
            print("========== TRANSFER ==========")
            print("1. Checking\n2. Savings\n3. Back to FROM account selection")
            print("=============================")
            
            try:
                user_selection = int(input("\nSelect account to transfer TO: "))
            except ValueError:
                print("Invalid input. Please enter a number corresponding to the menu options.")    
                print("\nPress Enter to continue...")
                continue
            
            if user_selection == 1:
                to_account = "Checking"
            elif user_selection == 2:
                to_account = "Savings"
            elif user_selection == 3:
                break # Go back to FROM account selection
            else:
                print("\nInvalid selection, please try again")
                print("\nPress Enter to continue...")
                continue
            
            if from_account == to_account:
                print("Unable to transfer to the same account. Please select a different account!")
                print("\nPress Enter to continue...")
                continue
            
            break # Exits the inner loop if valid accounts are selected
        
        if user_selection == 3:
            continue # Go back to FROM account selection

        utils.clear_screen()
        print(f"Transfer FROM: {from_account}")
        print(f"Transfer TO: {to_account}")
        
        while True:
            try:
                transfer_amount = float(input(f"Enter the amount to transfer from {from_account} to {to_account}: $"))
            except ValueError:
                print("\nInvalid Input. Please enter a valid number for the transfer amount")
                continue
            
            if transfer_amount <= 0:
                print("\nTransfer amount must be greater than $0. Please try again")
                continue
            
            from_balance_key = f"{from_account}Balance"
            to_balance_key = f"{to_account}Balance"
            
            if transfer_amount > user[from_balance_key]:
                print(f"Insufficient funds in {from_account}")
                continue
            
            elif transfer_amount > 10000:
                print("Transfer amount exceeds the maximum limit of $10,000. Please enter a smaller amount")
                continue

            # Perform the transfer
            user[from_balance_key] -= transfer_amount
            user[to_balance_key] += transfer_amount
            
            transaction_id = storage.get_transaction_id(user)
            
            dtime = datetime.datetime.now()
            date = dtime.strftime("%Y-%m-%d")
            time = dtime.strftime("%H:%M:%S")
            
            transaction = {
                "TransactionID": transaction_id,
                "Date": date,
                "Time": time,
                "Description": f"Transfer from {from_account} to {to_account}",
                "TransactionType": "Transfer",
                "From": from_account,
                "To": to_account,
                "Amount": transfer_amount,
                "FromBalance": user[from_balance_key],
                "ToBalance": user[to_balance_key]
            }
            
            storage.save_transaction(transaction, user)
            storage.save_profile(user)
            
            print(f"\nTransfer Successful!")
            print("================================")
            print(f"Type:       Transfer")
            print(f"From:       {from_account}")
            print(f"To:         {to_account}")
            print(f"Amount:     ${transfer_amount:.2f}")
            print(f"{from_account} Balance: ${user[from_balance_key]:.2f}")
            print(f"{to_account} Balance:   ${user[to_balance_key]:.2f}")
            print("================================")
            
            input("\nPress Enter to return to the Dashboard...")
            return  # Return to the dashboard after a successful transfer