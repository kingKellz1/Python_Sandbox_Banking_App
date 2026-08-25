import hashlib
import pwinput
import random
import os
import re
from . import utils

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_DIR = os.path.join(BASE_DIR, "users")

os.makedirs(USERS_DIR, exist_ok=True)

def create_account(fname, lname, email, username, password, confirm):
    fname = fname.strip().capitalize()
    lname = lname.strip().capitalize()
    
    if not fname:
        return False, "First name cannot be blank"
    
    if not lname:
        return False, "Last name cannot be blank"
    
    email = email.strip()
    
    if not email:
        return False, "Email cannot be blank"
    
    if not (
		email.count("@") == 1
		and "." in email.split("@")[1]
		and " " not in email
	):
        return False, "Invalid email address"
    
    username = username.strip().lower()
    
    if not username:
        return False, "Username cannot be blank"
    
    if not any(char.isdigit() for char in username):
        return False, "Username must contain at least one number"
    
    for filename in os.listdir(USERS_DIR):
        if filename.startswith("."):
            continue
        filepath = os.path.join(USERS_DIR, filename)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                if line.strip() == f"Username: {username}":
                    return False, "Username already exists"
    
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain an uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain a lowercase letter"
    if not re.search(r"\d", password):
        return False, "Password must contain a number"
    if not re.search(r"[!@#$%^&*()_+=_]", password):
        return False, "Password must contain special characters"
    if " " in password:
        return False, "Password cannot contain spaces"
    if password != confirm:
        return False, "Passwords do not match"
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    while True:
        userid = str(random.randint(100000, 999999))
        filepath = os.path.join(USERS_DIR, f"{userid}.txt")
        if not os.path.exists(filepath):
            break
        
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
    
    filepath = os.path.join(USERS_DIR, f"{userid}.txt")
    with open(filepath, "w", encoding="utf-8") as profile:
        for key, value in user.items():
            profile.write(f"{key}: {value}\n")
            
    return True, user

def register():
	"""Prompts the user for their information to create an account"""
	while True:
		utils.clear_screen()
		fname = input("Enter first name: ").capitalize()
		if fname:
			break
		print("First name cannot be blank.")
		input("\nPress enter to try again...")
	while True:
		utils.clear_screen()
		lname = input("Enter last name: ").capitalize()
		if lname:
			break
		print("Last name cannot be blank.")
		input("\nPress enter to try again...")
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
		input("\nPress enter to try again...")
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
			input("\nPress enter to try again...")
		else:
			break

	#Collects password and checks if Password already exists
	while True:
		utils.clear_screen()
		print("================================")
		print("       PASSWORD CREATION")
		print("================================")
		print("\nPassword Requirements:")
		print("Password must be at least 8 characters long. \nIt must contain at least one uppercase letter, \none lowercase letter, one number, and one special character.")
		password = pwinput.pwinput("\nEnter your Password: " , mask = "*")
		
		if len(password) < 8:                                   #Checks character count
			print("Must be at least 8 characters")
			input("\nPress enter to try again...")
			continue
		if not re.search(r"[A-Z]", password):                   #Checks for uppercase letter
			print("Must contain an uppercase letter")
			input("\nPress enter to try again...")
			continue
		if not re.search(r"[a-z]", password):                   #Checks for lowercase letter
			print("Must contain a lowercase letter")
			input("\nPress enter to try again...")
			continue
		if not re.search(r"\d", password):                      #Checks for a digit
			print("Must contain a number")
			input("\nPress enter to try again...")
			continue
		if not re.search(r"[!@#$%^&*()_+=-]", password):        #Checks for a special character
			print("Must contain a special character")
			input("\nPress enter to try again...")
			continue
		if " " in password:                                     #Checks for spaces in the password
			print("Password cannot contain spaces!")
			input("\nPress enter to try again...")
			continue
		
		confirm = pwinput.pwinput("Enter Password Again: " ,  mask = "*")
		
		if password != confirm:
			print("Passwords do not match! Please try again!")
			input("\nPress enter to try again...")
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
	input("\nPress enter to return to the main menu...")