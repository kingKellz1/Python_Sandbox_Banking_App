from . import storage
import datetime
from . import utils

def deposit(user, account, amount):
    if amount <= 0:
        return False, "Deposit must be greater than $0"
    balance_key = utils.get_balance_key(account)
    user[balance_key] += amount
    current_balance = user[balance_key]
    transaction_id = storage.get_transaction_id(user)
    transaction = storage.create_transaction_base(transaction_id)
    
    transaction["Description"] = f"Deposit to {account} account"
    transaction["Account Selected"] = account
    transaction["Transaction Type"] = "Deposit"
    transaction["Amount"] = amount
    transaction["Balance"] = current_balance
    
    storage.save_transaction(transaction, user)
    storage.save_profile(user)
    
    return True, current_balance

def user_deposit(user):
    """Function to handle deposits into the user's account."""
    
    account = utils.select_account()
    if account is None:
        return
        
    while True:
        utils.clear_screen()
        amount = input("Enter deposit amount (or B to go back): $").strip()
        if amount.lower() == 'b':
            return

        try:
            deposit_amount = float(amount)
        except ValueError:
            print("\nEnter a valid amount")
            input("\nPress enter to try again...")
            continue
        
        if deposit_amount <= 0:
            print("\nDeposit must be greater than $0")
            input("\nPress enter to try again...")
            continue
    
        balance_key = utils.get_balance_key(account)
  
        user[balance_key] += deposit_amount
        current_balance = user[balance_key]
            
        transaction_id = storage.get_transaction_id(user)
        
        transaction = storage.create_transaction_base(transaction_id)
        
        transaction["Description"] = f"Deposit to {account} account"
        transaction["Account Selected"] = account
        transaction["Transaction Type"] = "Deposit"
        transaction["Amount"] = deposit_amount
        transaction["Balance"] = current_balance
        
        storage.save_transaction(transaction, user)
        storage.save_profile(user)
  
        print("\nDeposit Successful!")
        print(f"\n{account} Balance: ${float(current_balance):,.2f}")
        input("\nPress enter to return...")
        return

def withdraw(user, account, amount):
    balance_key = utils.get_balance_key(account)
    
    if amount <= 0:
        return False, "Withdrawal must be greater than $0"
    if amount > user[balance_key]:
        return False, f"Insufficient funds in {account} account"
    
    user[balance_key] -= amount
    current_balance = user[balance_key]
    
    transaction_id = storage.get_transaction_id(user)
    transaction = storage.create_transaction_base(transaction_id)
    
    transaction["Description"] = f"Withdrawal from {account} account"
    transaction["Account Selected"] = account
    transaction["Transaction Type"] = "Withdrawal"
    transaction["Amount"] = amount
    transaction["Balance"] = current_balance
    
    storage.save_transaction(transaction, user)
    storage.save_profile(user)
    
    return True, current_balance

def user_withdrawal(user):
    """Function to handle withdrawals from the user's account."""
    
    account = utils.select_account()
    if account is None:
        return
        
    balance_key = utils.get_balance_key(account)
    if user[balance_key] <= 0:
        print(f"\nInsufficient funds in {account} account")
        input("\nPress enter to return...")
        return

    while True:
        utils.clear_screen()
        amount = input("Enter Withdrawal amount (or B to go back): $").strip()
        if amount.lower() == 'b':
            return

        try:
            withdrawal_amount = float(amount)
        except ValueError:
            print("\nEnter a valid amount")
            input("\nPress enter to try again...")
            continue
        
        if withdrawal_amount <= 0:
            print("\nWithdrawal must be greater than $0")
            input("\nPress enter to try again...")
            continue

        if withdrawal_amount > user[balance_key]:
            print(f"\nInsufficient funds in {account} account")
            input("\nPress enter to try again...")
            continue
    
        user[balance_key] -= withdrawal_amount
        current_balance = user[balance_key]
            
        transaction_id = storage.get_transaction_id(user)

        transaction = storage.create_transaction_base(transaction_id)

        transaction["Description"] = f"Withdrawal from {account} account"
        transaction["Account Selected"] = account
        transaction["Transaction Type"] = "Withdrawal"
        transaction["Amount"] = withdrawal_amount
        transaction["Balance"] = current_balance
        
        storage.save_transaction(transaction, user)
        storage.save_profile(user)

        print("\nWithdrawal Successful!")
        print(f"\n{account} Balance: ${float(current_balance):,.2f}")
        input("\nPress enter to return...")
        return