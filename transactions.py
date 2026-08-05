import storage
import datetime
import utils

def user_deposit(user):
	"""Function to handle deposits into the user's account."""
	
	account = utils.select_account()
	if account is None:
		return
		
	while True:
		try:
			utils.clear_screen()
			deposit_amount = float(input("Enter deposit amount: $"))
		except ValueError:
			print("\nEnter a valid amount")
			continue
		
		if deposit_amount <= 0:
			print("\nDeposit must be greater than $0")
			continue
	
		balance_key = utils.get_balance_key(account)
  
		user[balance_key] += deposit_amount
		current_balance = user[balance_key]
			
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
		input("\nPress enter to return...")
		return

def user_withdrawal(user):
	"""Function to handle withdrawals from the user's account."""
	
	account = utils.select_account()
	if account is None:
		return
		
	balance_key = utils.get_balance_key(account)
 
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

		if withdrawal_amount > user[balance_key]:
			print(f"\nInsufficient funds in {account} account")
			continue
	
		user[balance_key] -= withdrawal_amount
		current_balance = user[balance_key]
			
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
		input("\nPress enter to return...")
		return