import hashlib
import pwinput
import random
import os
import re
import utils

os.makedirs("users", exist_ok=True)

def register():
	"""Prompts the user for their information to create an account"""
	while True:
		utils.clear_screen()
		fname = input("Enter first name: ").capitalize()
		if fname:
			break
		print("First name cannot be blank.")
	while True:
		utils.clear_screen()
		lname = input("Enter last name: ").capitalize()
		if lname:
			break
		print("Last name cannot be blank.")
	while True:
		utils.clear_screen()
		email = input("Enter email: ").strip()
		if not email:
			print("Email cannot be blank")
			continue
		if (
			email.count("@") == 1
			and "." in email.split("@")[1]
			and " " not in email
		):
			break
		print("Invalid email address. Please try again")
	while True:
		utils.clear_screen()
		username = input("Enter username : ").strip().lower()
		if not username:
			print("Username cannot be blank.")
			continue
		username_found = False
		for filename in os.listdir("users"):
			if filename.startswith("."):
				continue
			with open(f"users/{filename}", "r", encoding = "utf-8", errors = "ignore") as file:
				for line in file:
					if line.strip() == f"Username: {username}":
						username_found = True
						break
				if username_found:
					break
				
		if username_found:
			print("Username already exists")
		else:
			break

	#Collects password and checks if Password already exists
	while True:
		utils.clear_screen()
		password = pwinput.pwinput("Enter your Password: " , mask = "*")
		
		if len(password) < 8:                                   #Checks character count
			print("Must be at least 8 characters")
			continue
		if not re.search(r"[A-Z]", password):                   #Checks for uppercase letter
			print("Must contain an uppercase letter")
			continue
		if not re.search(r"[a-z]", password):                   #Checks for lowercase letter
			print("Must contain a lowercase letter")
			continue
		if not re.search(r"\d", password):                      #Checks for a digit
			print("Must contain a number")
			continue
		if not re.search(r"[!@#$%^&*()_+=-]", password):        #Checks for a special character
			print("Must contain a special character")
			continue
		if " " in password:                                     #Checks for spaces in the password
			print("Password cannot contain spaces!")
			continue
		
		confirm = pwinput.pwinput("Enter Password Again: " ,  mask = "*")
		
		if password != confirm:
			print("Passwords do not match! Please try again!")
			continue
		break

	#Creates a hashed password and stores it so the original is never saved
	hashed_password = hashlib.sha256(password.encode()).hexdigest()

	while True:
		userid = str(random.randint(100000, 999999))
		if not os.path.exists(f"users/{userid}.txt"):
			break

	#Creates a dictionary and writes the user information to a text file
	user = {
		"UserID": userid,
		"First name": fname,
		"Last name": lname,
		"Email": email,
		"Username": username,
		"PasswordHash": hashed_password,
		"CheckingBalance": 0.00,
		"SavingsBalance": 0.00
	}
		
	with open(f"users/{userid}.txt", "w", encoding = "utf-8") as profile:
		for key, value in user.items():
			profile.write(f"{key}: {value}\n")
	
	utils.clear_screen()
	print("================================")        
	print("Account Created Successfully!\n")
	print(f"Welcome, {fname}!\n")
	print(f"Your User ID is: {userid}\n")
	print("You may now log in with your username and password.")
	print("================================")  