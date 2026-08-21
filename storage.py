import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_DIR = os.path.join(BASE_DIR, "users")
TRANSACTIONS_DIR = os.path.join(BASE_DIR, "transactions")
TRANSACTION_SEPARATOR = "=" * 60

def save_profile(user):
	"""Save user profile data to a profile file."""
	filepath = os.path.join(USERS_DIR, user["ProfileFile"])
	with open (filepath, "w", encoding = "utf-8") as file:            
		for key, value in user.items():
			if key == "ProfileFile":
				continue
			file.write(f"{key}: {value}\n")

def save_transaction(transaction, user):
	"""Append a transaction record for a user to the daily transaction file."""
	user_transactions_dir = os.path.join(TRANSACTIONS_DIR, user["UserID"])
	os.makedirs(user_transactions_dir, exist_ok=True)
				
	today = datetime.datetime.now().strftime("%Y-%m-%d")
	
	filepath = os.path.join(user_transactions_dir,f"{today}.txt")
	with open (filepath, "a", encoding = "utf-8") as file:
		for key, value in transaction.items():
			file.write(f"{key:20}: {value}\n")
		file.write(f"\n{TRANSACTION_SEPARATOR}\n")
			
def get_transaction_id(user):
	"""Generate and return the next transaction ID for a user."""
	user_transactions_dir = os.path.join(TRANSACTIONS_DIR, user["UserID"])
	os.makedirs(user_transactions_dir, exist_ok=True)
	
	filepath = os.path.join(user_transactions_dir, "counter.txt")
	if not os.path.exists(filepath):
		transaction_number = 1
		with open (filepath, "w", encoding = "utf-8") as file:
			file.write(str(transaction_number))

		transaction_id = f'{transaction_number:06d}'
		return transaction_id
	else:
		with open (filepath, "r", encoding = "utf-8") as file:
			transaction_number = int(file.read())
		transaction_number += 1
		with open (filepath, "w", encoding = "utf-8") as file:
			file.write(str(transaction_number))
		transaction_id = f'{transaction_number:06d}'
		return transaction_id

def create_transaction_base(transaction_id):
	"""Create the base transaction dictionary."""
	current_datetime = datetime.datetime.now()
 
	transaction_date = current_datetime.strftime("%Y-%m-%d")
	transaction_time = current_datetime.strftime("%H:%M:%S")
 
	transaction = {
		"Transaction ID": transaction_id,
		"Date": transaction_date,
		"Time": transaction_time
	}
	return transaction
