import customtkinter
from .. import transactions

def go_back(account_frame, dashboard_frame):
    account_frame.grid_remove()
    dashboard_frame.grid()
    dashboard_frame.update_idletasks()
    
def show_deposit(app, user, dashboard_frame, checking_balance, savings_balance):
    dashboard_frame.grid_remove()
    user_selection = None
    
    def select_account(account):
        nonlocal user_selection
        user_selection = account
        
        result_label.configure(text="")
        
        if account == "Checking":
            checking_button.configure(fg_color="green")
            savings_button.configure(fg_color="gray")
        else:
            checking_button.configure(fg_color="gray")
            savings_button.configure(fg_color="green")
        
        amount_frame.grid()
    
    def make_deposit():
        amount = amount_entry.get()
        try:
            amount = float(amount)
        except ValueError:
            result_label.configure(text="Please enter a valid amount")
            return
        
        success, result = transactions.deposit(user, user_selection, amount)
        
        if success:
            result_label.configure(text=f"Deposit successfull!\nNew balance: ${result:,.2f}")
            amount_entry.delete(0, "end")
            
            if user_selection == "Checking":
                checking_balance.configure(text=f"${result:,.2f}")
            else:
                savings_balance.configure(text=f"${result:,.2f}")
        else:
            result_label.configure(text=result)
    
    deposit_frame = customtkinter.CTkFrame(app)
    deposit_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
    
    deposit_frame.grid_columnconfigure(0, weight=1)
    deposit_frame.grid_columnconfigure(1, weight=1)
    
    title = customtkinter.CTkLabel(deposit_frame, text="MAKE A DEPOSIT", font=("Arial", 24, "bold"))
    title.grid(row=0, column=0, columnspan=2, pady=20)
    
    account_label = customtkinter.CTkLabel(deposit_frame, text="SELECT ACCOUNT", font=("Arial", 16, "bold"))
    account_label.grid(row=1, column=0, columnspan=2, pady=(20, 10))
    
    checking_button = customtkinter.CTkButton(deposit_frame, text="[ CHECKING ]", command=lambda: select_account("Checking"))
    checking_button.grid(row=2, column=0, padx=10, pady=10)
    
    savings_button = customtkinter.CTkButton(deposit_frame, text="[ SAVINGS ]", command=lambda: select_account("Savings"))
    savings_button.grid(row=2, column=1, padx=10, pady=10)
    
    amount_frame = customtkinter.CTkFrame(deposit_frame)
    amount_frame.grid(row=4, column=0, columnspan=2, pady=10)
    
    amount_label = customtkinter.CTkLabel(amount_frame, text="AMOUNT")
    amount_label.grid(row=0, column=0, padx=10, pady=10)
    
    amount_entry = customtkinter.CTkEntry(amount_frame, width=200)
    amount_entry.grid(row=0, column=1, padx=10, pady=10)
    
    amount_frame.grid_remove()
    
    deposit_button = customtkinter.CTkButton(amount_frame, text="[ DEPOSIT ]", command=make_deposit)
    deposit_button.grid(row=0, column=2, padx=10, pady=10)
    
    result_label = customtkinter.CTkLabel(deposit_frame, text="")
    result_label.grid(row=5, column=0, columnspan=2, pady=5)
    
    back_button = customtkinter.CTkButton(deposit_frame, text="[BACK TO DASHBOARD]", command=lambda: go_back(deposit_frame, dashboard_frame))
    back_button.grid(row=6, column=0, columnspan=2, pady=20)

def show_withdraw(app, user, dashboard_frame, checking_balance, savings_balance):
    dashboard_frame.grid_remove()
    user_selection = None
    
    def select_account(account):
        nonlocal user_selection
        user_selection = account
        result_label.configure(text="")
        
        if account == "Checking":
            checking_button.configure(fg_color="green")
            savings_button.configure(fg_color="gray")
        else:
            checking_button.configure(fg_color="gray")
            savings_button.configure(fg_color="green")
        
        amount_frame.grid()
    
    def make_withdrawal():
        amount = amount_entry.get()
        
        try:
            amount = float(amount)
        except ValueError:
            result_label.configure(text="Please enter a valid amount.")
            return
        
        success, result = transactions.withdraw(user, user_selection, amount)
        
        if success:
            result_label.configure(text=f"Withdrawal successful!\nNew Balance: ${result:,.2f}")
            amount_entry.delete(0, "end")
            
            if user_selection == "Checking":
                checking_balance.configure(text=f"${result:,.2f}")
            else:
                savings_balance.configure(text=f"${result:,.2f}")
        else:
            result_label.configure(text=result)
    
    withdraw_frame = customtkinter.CTkFrame(app)
    withdraw_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
    
    withdraw_frame.grid_columnconfigure(0, weight=1)
    withdraw_frame.grid_columnconfigure(1, weight=1)
    
    title = customtkinter.CTkLabel(withdraw_frame, text="MAKE A WITHDRAWAL", font=("Arial", 24, "bold"))
    title.grid(row=0, column=0, columnspan=2, pady=20)
    
    account_label = customtkinter.CTkLabel(withdraw_frame, text="SELECT ACCOUNT", font=("Arial", 16, "bold"))
    account_label.grid(row=1, column=0, columnspan=2, pady=(20, 10))
    
    checking_button = customtkinter.CTkButton(withdraw_frame, text="[ CHECKING ]", command=lambda: select_account("Checking"))
    checking_button.grid(row=2, column=0, padx=10, pady=10)
    
    savings_button = customtkinter.CTkButton(withdraw_frame, text="[ SAVINGS ]", command=lambda: select_account("Savings"))
    savings_button.grid(row=2, column=1, padx=10, pady=10)
    
    amount_frame = customtkinter.CTkFrame(withdraw_frame)
    amount_frame.grid(row=4, column=0, columnspan=2, pady=10)
    
    amount_label = customtkinter.CTkLabel(amount_frame, text="AMOUNT")
    amount_label.grid(row=0, column=0, padx=10, pady=10)
    
    amount_entry = customtkinter.CTkEntry(amount_frame, width=200)
    amount_entry.grid(row=0, column=1, padx=10, pady=10)
    
    withdraw_action_button = customtkinter.CTkButton(amount_frame, text="[ WITHDRAW ]", command=make_withdrawal)
    withdraw_action_button.grid(row=0, column=2, padx=10, pady=10)
    
    amount_frame.grid_remove()
    
    result_label = customtkinter.CTkLabel(withdraw_frame, text="")
    result_label.grid(row=5, column=0, columnspan=2, pady=5)
    
    back_button = customtkinter.CTkButton(withdraw_frame, text="[BACK TO DASHBOARD]", command=lambda: go_back(withdraw_frame, dashboard_frame))
    back_button.grid(row=6, column=0, columnspan=2, pady=20)

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
    
    deposit_button = customtkinter.CTkButton(actions_frame, text="[DEPOSIT]", command=lambda: show_deposit(app, user, dashboard_frame, checking_balance, savings_balance))
    deposit_button.grid(row=0, column=1, padx=10, pady=10)
    
    withdraw_button = customtkinter.CTkButton(actions_frame, text="[WITHDRAW]", command=lambda: show_withdraw(app, user, dashboard_frame, checking_balance, savings_balance))
    withdraw_button.grid(row=0, column=2, padx=10, pady=10)
    
    transfer_button = customtkinter.CTkButton(actions_frame, text="[TRANSFER]")
    transfer_button.grid(row=0, column=3, padx=10, pady=10)
    
    transaction_history_button = customtkinter.CTkButton(actions_frame, text="[TRANSACTION HISTORY]")
    transaction_history_button.grid(row=1, column=1, padx=10, pady=10)
    
    logout_button = customtkinter.CTkButton(actions_frame, text="[LOGOUT]")
    logout_button.grid(row=1, column=2, padx=10, pady=10)