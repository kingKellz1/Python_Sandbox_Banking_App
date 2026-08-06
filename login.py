import os
import hashlib
import pwinput

def login():
	"""Function to handle user login."""
	username = input("Username : ").lower()
	username_found = False
	matching_file = None
	stored_hash = None
	fname = None
	userid = None
	checking_balance = None
	savings_balance = None
	
	for filename in os.listdir("users"):
		# Skips hidden files like .DS_Store
		if filename.startswith("."):
			continue

		# Specify utf-8 encoding and ignore unreadable bytes
		with open(f"users/{filename}", "r", encoding = "utf-8", errors = "ignore") as file:
			found_in_this_file = False
			temp_hash = None
			temp_fname = None
			temp_lname = None
			temp_email = None
			temp_checking = None
			temp_savings = None

			for line in file:
				line = line.strip()
				if line == f"Username: {username}":
					found_in_this_file = True
				elif line.startswith("PasswordHash:"):
					temp_hash = line.split(": ")[1]
				elif line.startswith("First name:"):
					temp_fname = line.split(": ")[1]
				elif line.startswith("Last name:"):
					temp_lname = line.split(": ")[1]
				elif line.startswith("Email:"):
					temp_email = line.split(": ")[1]
				elif line.startswith("CheckingBalance:"):
					temp_checking = float(line.split(": ")[1])
				elif line.startswith("SavingsBalance:"):
					temp_savings = float(line.split(": ")[1])
		
			if found_in_this_file:
				username_found = True
				matching_file = filename
				userid = matching_file.split(".")[0]  # Extracts the user ID from the filename
				stored_hash = temp_hash
				fname = temp_fname
				checking_balance = temp_checking
				savings_balance = temp_savings
				lname = temp_lname
				email = temp_email
				break  # Stops checking the remaining files

	if not username_found:
		print("Username not found")
		return None
	else:
		#print(f"Username found in {matching_file}")
		password = pwinput.pwinput("Enter your Password: " , mask = "*")
		hashed_password = hashlib.sha256(password.encode()).hexdigest()

		if stored_hash is None:
			print("No password set for this user or file might be damaged.")
			input("\nPress enter to return...")
			return None
		elif stored_hash == hashed_password:
			user = {
				"UserID": userid,
				"First name": fname,
				"Last name": lname,
				"Email": email,
				"Username": username,
				"PasswordHash": stored_hash,
				"CheckingBalance": checking_balance,
				"SavingsBalance": savings_balance,
				"ProfileFile": matching_file
				}
			return user
		else:
			print("Incorrect password")
			return None