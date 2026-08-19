import customtkinter

def go_back(account_frame, dashboard_frame):
    account_frame.grid_remove()
    dashboard_frame.grid()
    dashboard_frame.update_idletasks()

def view_account(app, user, dashboard_frame):
    dashboard_frame.grid_remove()
    account_frame = customtkinter.CTkFrame(app)
    account_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
    account_frame.grid_columnconfigure(0, weight=1)
    
    title = customtkinter.CTkLabel(account_frame, text="ACCOUNT DETAILS", font=("Arial", 24, "bold"))
    title.grid(row=0, column=0, columnspan=2, pady=20)
    
    personal_frame = customtkinter.CTkFrame(account_frame)
    personal_frame.grid(row=1, column=0, padx=40, pady=(10, 10), sticky="ew")
    
    balances_frame = customtkinter.CTkFrame(account_frame)
    balances_frame.grid(row=2, column=0, padx=40, pady=(10, 10), sticky="ew")
    
    balances_title = customtkinter.CTkLabel(balances_frame, text="ACCOUNT BALANCES", font=("Arial", 16, "bold"))
    balances_title.grid(row=0, column=0, columnspan=2, padx=20, pady=(8, 3), sticky="w")
    
    personal_title = customtkinter.CTkLabel(personal_frame, text="PERSONAL INFORMATION", font=("Arial", 16, "bold"))
    personal_title.grid(row=0, column=0, columnspan=2, padx=20, pady=(8, 3), sticky="w")
    
    name_label = customtkinter.CTkLabel(personal_frame, text="Name:", font=("Arial", 12, "bold"))
    name_label.grid(row=1, column=0, padx=(20, 10), pady=2, sticky="w")
    
    name_value = customtkinter.CTkLabel(personal_frame, text=f"{user['First name']} {user['Last name']}", font=("Arial", 12))
    name_value.grid(row=1, column=1, padx=10, pady=2, sticky="w")
    
    username_label = customtkinter.CTkLabel(personal_frame, text="Username:", font=("Arial", 12, "bold"))
    username_label.grid(row=2, column=0, padx=(20, 10), pady=2, sticky="w")

    username_value = customtkinter.CTkLabel(personal_frame, text=user["Username"], font=("Arial", 12))
    username_value.grid(row=2, column=1, padx=10, pady=2, sticky="w")

    email_label = customtkinter.CTkLabel(personal_frame,text="Email:", font=("Arial", 12, "bold"))
    email_label.grid(row=3, column=0, padx=(20, 10), pady=2, sticky="w")

    email_value = customtkinter.CTkLabel(personal_frame, text=user["Email"], font=("Arial", 12))
    email_value.grid(row=3, column=1, padx=10, pady=2, sticky="w")

    user_id_label = customtkinter.CTkLabel(personal_frame, text="User ID:", font=("Arial", 12, "bold"))
    user_id_label.grid(row=4, column=0, padx=(20, 10), pady=2, sticky="w")

    user_id_value = customtkinter.CTkLabel(personal_frame, text=user["UserID"], font=("Arial", 12))
    user_id_value.grid(row=4, column=1, padx=10, pady=2, sticky="w")
    
    checking_label = customtkinter.CTkLabel(balances_frame, text="Checking",font=("Arial", 12, "bold"))
    checking_label.grid(row=1, column=0, padx=(20, 10), pady=2, sticky="w")

    checking_value = customtkinter.CTkLabel(balances_frame, text=f"${user['CheckingBalance']:,.2f}", font=("Arial", 12))
    checking_value.grid(row=1, column=1, padx=10, pady=2, sticky="w")

    savings_label = customtkinter.CTkLabel(balances_frame,text="Savings", font=("Arial", 12, "bold"))
    savings_label.grid(row=2, column=0, padx=(20, 10), pady=2, sticky="w")

    savings_value = customtkinter.CTkLabel(balances_frame, text=f"${user['SavingsBalance']:,.2f}", font=("Arial", 12))
    savings_value.grid(row=2, column=1, padx=10, pady=2, sticky="w")
    
    back_button = customtkinter.CTkButton(account_frame, text="[BACK TO DASHBOARD]", command=lambda: go_back(account_frame, dashboard_frame))
    back_button.grid(row=3, column=0, pady=20)

def show_dashboard(app, user):
    """Display the user's dashboard"""
    dashboard_frame = customtkinter.CTkFrame(app)
    dashboard_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
    
    title = customtkinter.CTkLabel(dashboard_frame, text="BANK DASHBOARD", font=("Arial", 24, "bold"))
    title.pack(pady=30)
    
    welcome = customtkinter.CTkLabel(dashboard_frame, text=f"Welcome back, {user['First name']}!", font=("Arial", 16))
    welcome.pack(pady=10)
    
    accounts_frame = customtkinter.CTkFrame(dashboard_frame)
    accounts_frame.pack(pady=10, padx=20, fill="x")
    
    actions_frame = customtkinter.CTkFrame(dashboard_frame)
    actions_frame.pack(pady=20, padx=20, fill="x")
    
    actions_frame.grid_columnconfigure(0, weight=1)
    actions_frame.grid_columnconfigure(1, weight=1)
    actions_frame.grid_columnconfigure(2, weight=1)
    actions_frame.grid_columnconfigure(3, weight=1)
    
    checking_frame = customtkinter.CTkFrame(accounts_frame)
    checking_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    accounts_frame.grid_columnconfigure(0, weight=1)
    
    checking_title = customtkinter.CTkLabel(checking_frame, text="CHECKING", font=("Arial", 16, "bold"))
    checking_title.pack(pady=(15, 5))
    
    checking_balance = customtkinter.CTkLabel(checking_frame, text=f"${user['CheckingBalance']:,.2f}", font=("Arial", 16, "bold"))
    checking_balance.pack(pady=(5, 15))
    
    savings_frame = customtkinter.CTkFrame(accounts_frame)
    savings_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    accounts_frame.grid_columnconfigure(1, weight=1)
    
    savings_title = customtkinter.CTkLabel(savings_frame, text="SAVINGS", font=("Arial", 16, "bold"))
    savings_title.pack(pady=(15, 5))
    
    savings_balance = customtkinter.CTkLabel(savings_frame, text=f"${user['SavingsBalance']:,.2f}", font=("Arial", 16, "bold"))
    savings_balance.pack(pady=(5, 15))
    
    view_account_button = customtkinter.CTkButton(actions_frame, text="[VIEW ACCOUNT]", command=lambda: view_account(app, user, dashboard_frame))
    view_account_button.grid(row=0, column=0, padx=10, pady=10)
    
    deposit_button = customtkinter.CTkButton(actions_frame, text="[DEPOSIT]")
    deposit_button.grid(row=0, column=1, padx=10, pady=10)
    
    withdraw_button = customtkinter.CTkButton(actions_frame, text="[WITHDRAW]")
    withdraw_button.grid(row=0, column=2, padx=10, pady=10)
    
    transfer_button = customtkinter.CTkButton(actions_frame, text="[TRANSFER]")
    transfer_button.grid(row=0, column=3, padx=10, pady=10)
    
    transaction_history_button = customtkinter.CTkButton(actions_frame, text="[TRANSACTION HISTORY]")
    transaction_history_button.grid(row=1, column=1, padx=10, pady=10)
    
    logout_button = customtkinter.CTkButton(actions_frame, text="[LOGOUT]")
    logout_button.grid(row=1, column=2, padx=10, pady=10)