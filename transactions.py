import storage
import datetime
import utils

def user_deposit(user):
	"""Function to handle deposits into the user's account."""
	account = None
	
	while True:
		utils.clear_screen()
		print("========== DEPOSIT ==========")
		print("1. Checking\n2. Savings\n3. Back")
		print("=============================")
		
		try:
			user_selection = int(input("\nSelection: "))
		except ValueError:
			print("Invalid input. Please enter a number corresponding to the menu options.")    
			continue
					
		if user_selection == 1:
			account = "Checking"
		elif user_selection == 2:
			account = "Savings"
		elif user_selection == 3:
			break
		else:
			print("\nInvalid selection, please try again")
			continue
		
		print(f"\nDeposit account selected: {account}")
		while True:
			utils.clear_screen()
			try:
				deposit_amount = float(input("Enter deposit amount: $"))
			except ValueError:
				print("\nEnter a valid amount")
				continue
			
			if deposit_amount <= 0:
				print("\nDeposit must be greater than $0")
				continue
		
			if account == "Checking":
				user["CheckingBalance"] += deposit_amount
				current_balance = user["CheckingBalance"]
			elif account == "Savings":
				user["SavingsBalance"] += deposit_amount
				current_balance = user["SavingsBalance"]
			else:
				print("\nInvalid account selection.")
				return
				
			transaction_id = storage.get_transaction_id(user)
			
			dtime = datetime.datetime.now()
			
			date = dtime.strftime("%Y-%m-%d")
			time = dtime.strftime("%H:%M:%S")
			
			transaction = {
				"Transaction ID": transaction_id,
				"Date": date,
				"Time": time,
				"Description": f"Deposit to {account} account",
				"Account Selected": account,
				"Transaction Type": "Deposit",
				"Amount": deposit_amount,
				"Balance": current_balance
			}
			
			storage.save_transaction(transaction, user)
			storage.save_profile(user)
			print("\nDeposit Successful!")
			print(f"\n{account} Balance: ${float(current_balance):,.2f}")
			input("\nPress Enter to return to the transaction history menu...")
			return

def user_withdrawal(user):
	"""Function to handle withdrawals from the user's account."""
	account = None
	
	while True:
		utils.clear_screen()
		print("========== WITHDRAWAL ==========")
		print("1. Checking\n2. Savings\n3. Back")
		print("=============================")
		
		try:
			user_selection = int(input("\nSelection: "))
		except ValueError:
			print("Invalid input. Please enter a number corresponding to the menu options.")    
			continue
					
		if user_selection == 1:
			account = "Checking"
		elif user_selection == 2:
			account = "Savings"
		elif user_selection == 3:
			break
		else:
			print("\nInvalid selection, please try again")
			continue
		
		print(f"\nWithdrawal account selected: {account}")
		while True:
			utils.clear_screen()
			try:
				withdrawal_amount = float(input("Enter withdrawal amount: $"))
			except ValueError:
				print("\nEnter a valid amount")
				continue
			
			if withdrawal_amount <= 0:
				print("\nWithdrawal must be greater than $0")
				continue
			elif account == "Checking" and withdrawal_amount > user["CheckingBalance"]:
				print("\nInsufficient funds in Checking account")
				continue
			elif account == "Savings" and withdrawal_amount > user["SavingsBalance"]:
				print("\nInsufficient funds in Savings account")
				continue
		
			if account == "Checking":
				user["CheckingBalance"] -= withdrawal_amount
				current_balance = user["CheckingBalance"]
			elif account == "Savings":
				user["SavingsBalance"] -= withdrawal_amount
				current_balance = user["SavingsBalance"]
			else:
				print("\nInvalid account selection.")
				return
				
			transaction_id = storage.get_transaction_id(user)
			
			dtime = datetime.datetime.now()
			
			date = dtime.strftime("%Y-%m-%d")
			time = dtime.strftime("%H:%M:%S")
			
			transaction = {
				"Transaction ID": transaction_id,
				"Date": date,
				"Time": time,
				"Description": f"Withdrawal from {account} account",
				"Account Selected": account,
				"Transaction Type": "Withdrawal",
				"Amount": withdrawal_amount,
				"Balance": current_balance
			}
			
			storage.save_transaction(transaction, user)
			storage.save_profile(user)
			print("\nWithdrawal Successful!")
			print(f"\n{account} Balance: ${float(current_balance):,.2f}")
			input("\nPress Enter to go back to the menu...")
			return