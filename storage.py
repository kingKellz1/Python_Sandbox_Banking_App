import os
import datetime

TRANSACTION_SEPARATOR = "=" * 60

def save_profile(user):
	"""Save user profile data to a profile file."""
	filepath = f"users/{user['ProfileFile']}"
	with open (filepath, "w", encoding = "utf-8") as file:            
		for key, value in user.items():
			if key == "ProfileFile":
				continue
			file.write(f"{key}: {value}\n")

def save_transaction(transaction, user):
	"""Append a transaction record for a user to the daily transaction file."""
	os.makedirs(f"transactions/{user['UserID']}", exist_ok=True)
				
	today = datetime.datetime.now().strftime("%Y-%m-%d")
	
	filepath = f"transactions/{user['UserID']}/{today}.txt"
	with open (filepath, "a", encoding = "utf-8") as file:
		for key, value in transaction.items():
			file.write(f"{key:20}: {value}\n")
		file.write(f"\n{TRANSACTION_SEPARATOR}\n")
			
def get_transaction_id(user):
	"""Generate and return the next transaction ID for a user."""
	os.makedirs(f"transactions/{user['UserID']}", exist_ok=True)
	
	filepath = f"transactions/{user['UserID']}/counter.txt"
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
