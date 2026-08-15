import customtkinter

def show_dashboard(app, user):
    """Display the user's dashboard"""
    
    dashboard_frame = customtkinter.CTkFrame(app)
    dashboard_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
    
    title = customtkinter.CTkLabel(
        dashboard_frame, 
        text="BANK DASHBOARD", 
        font=("Arial", 24, "bold")
    )
    title.pack(pady=30)
    
    welcome = customtkinter.CTkLabel(
        dashboard_frame,
        text=f"Welcome back, {user['First name']}!",
        font=("Arial", 16)
    )
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
    
    checking_title = customtkinter.CTkLabel(
        checking_frame,
        text="CHECKING",
        font=("Arial", 16, "bold")
    )
    checking_title.pack(pady=(15, 5))
    
    checking_balance = customtkinter.CTkLabel(
        checking_frame,
        text=f"${user['CheckingBalance']:,.2f}",
        font=("Arial", 16, "bold")
        )
    checking_balance.pack(pady=(5, 15))
    
    savings_frame = customtkinter.CTkFrame(accounts_frame)
    savings_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    accounts_frame.grid_columnconfigure(1, weight=1)
    
    savings_title = customtkinter.CTkLabel(
        savings_frame,
        text="SAVINGS",
        font=("Arial", 16, "bold")
    )
    savings_title.pack(pady=(15, 5))
    
    savings_balance = customtkinter.CTkLabel(
        savings_frame,
        text=f"${user['SavingsBalance']:,.2f}",
        font=("Arial", 16, "bold")
    )
    savings_balance.pack(pady=(5, 15))
    
    view_account_button = customtkinter.CTkButton(
        actions_frame,
        text="[VIEW ACCOUNT]"
    )
    view_account_button.grid(row=0, column=0, padx=10, pady=10)
    
    deposit_button = customtkinter.CTkButton(
        actions_frame,
        text="[DEPOSIT]"
    )
    deposit_button.grid(row=0, column=1, padx=10, pady=10)
    
    withdraw_button = customtkinter.CTkButton(
        actions_frame,
        text="[WITHDRAW]"
    )
    withdraw_button.grid(row=0, column=2, padx=10, pady=10)
    
    transfer_button = customtkinter.CTkButton(
        actions_frame,
        text="[TRANSFER]"
    )
    transfer_button.grid(row=0, column=3, padx=10, pady=10)
    
    transaction_history_button = customtkinter.CTkButton(
        actions_frame,
        text="[TRANSACTION HISTORY]"
    )
    transaction_history_button.grid(row=1, column=1, padx=10, pady=10)
    
    logout_button = customtkinter.CTkButton(
        actions_frame,
        text="[LOGOUT]"
    )
    logout_button.grid(row=1, column=2, padx=10, pady=10)