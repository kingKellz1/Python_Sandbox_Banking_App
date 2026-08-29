import customtkinter
from .. import transactions
from .. import transfer
from .. import transaction_history
from . import theme

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
            checking_button.configure(
                fg_color=theme.PRIMARY,
                text_color=theme.TEXT_PRIMARY
            )
            savings_button.configure(
                fg_color="transparent",
                text_color=theme.TEXT_SECONDARY
            )
        else:
            checking_button.configure(
                fg_color="transparent",
                text_color=theme.TEXT_SECONDARY
            )
            savings_button.configure(
                fg_color=theme.PRIMARY,
                text_color=theme.TEXT_PRIMARY
            )
        amount_frame.grid()
    
    def make_deposit():
        amount = amount_entry.get()
        try:
            amount = float(amount)
        except ValueError:
            result_label.configure(text="Please enter a valid amount", text_color=theme.DANGER)
            return
        
        success, result = transactions.deposit(user, user_selection, amount)
        
        if success:
            result_label.configure(text=f"Deposit successful!\nNew balance: ${result:,.2f}", text_color=theme.SUCCESS)
            amount_entry.delete(0, "end")
            
            if user_selection == "Checking":
                checking_balance.configure(text=f"${result:,.2f}")
            else:
                savings_balance.configure(text=f"${result:,.2f}")
        else:
            result_label.configure(text=result, text_color=theme.DANGER)
    
    deposit_frame = customtkinter.CTkFrame(app, fg_color=theme.PANEL_BG, corner_radius=theme.FRAME_RADIUS, border_width=1, border_color=theme.BORDER)
    deposit_frame.grid(row=0, column=0, columnspan=2, padx=40, pady=40, sticky="nsew")
    
    deposit_frame.grid_columnconfigure(0, weight=1)
    deposit_frame.grid_columnconfigure(1, weight=1)
    
    title = customtkinter.CTkLabel(deposit_frame, text="MAKE A DEPOSIT", font=("Arial", 26, "bold"), text_color=theme.TEXT_PRIMARY)
    title.grid(row=0, column=0, columnspan=2, pady=(30, 5))
    
    subtitle = customtkinter.CTkLabel(deposit_frame, text="Add funds to one of your accounts", font=("Arial", 13), text_color=theme.TEXT_MUTED)
    subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 25))
    
    account_frame = customtkinter.CTkFrame(deposit_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    account_frame.grid(row=2, column=0, columnspan=2, padx=40, pady=(10, 10), sticky="ew")
    
    account_frame.grid_columnconfigure(0, weight=1)
    account_frame.grid_columnconfigure(1, weight=1)
    
    account_label = customtkinter.CTkLabel(account_frame, text="SELECT ACCOUNT", font=("Arial", 14, "bold"), text_color=theme.TEXT_MUTED)
    account_label.grid(row=0, column=0, columnspan=2, pady=(20, 15))
    
    checking_button = customtkinter.CTkButton(account_frame, text="CHECKING", command=lambda: select_account("Checking"), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_HOVER, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_SECONDARY, font=("Arial", 12, "bold"))
    checking_button.grid(row=1, column=0, padx=(20, 10), pady=(0, 20), sticky="ew")
    
    savings_button = customtkinter.CTkButton(account_frame, text="SAVINGS", command=lambda: select_account("Savings"), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_HOVER, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_SECONDARY, font=("Arial", 12, "bold"))
    savings_button.grid(row=1, column=1, padx=(10, 20), pady=(0, 20), sticky="ew")
    
    amount_frame = customtkinter.CTkFrame(deposit_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    amount_frame.grid(row=3, column=0, columnspan=2, padx=40, pady=10, sticky="ew")
    amount_frame.grid_columnconfigure(0, weight=1)
    
    amount_label = customtkinter.CTkLabel(amount_frame, text="AMOUNT", font=("Arial", 14, "bold"), text_color=theme.TEXT_MUTED)
    amount_label.grid(row=0, column=0, pady=(20, 10))
    
    amount_entry = customtkinter.CTkEntry(amount_frame, width=260, height=44, corner_radius=theme.ENTRY_RADIUS, fg_color=theme.PANEL_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="$0.00", justify="center", font=("Arial", 14))
    amount_entry.grid(row=1, column=0, pady=10)
    
    amount_frame.grid_remove()
    
    deposit_button = customtkinter.CTkButton(amount_frame, text="DEPOSIT", command=make_deposit, width=260, height=44, corner_radius=theme.BUTTON_RADIUS, fg_color=theme.PRIMARY, hover_color=theme.PRIMARY_HOVER, text_color=theme.TEXT_PRIMARY, font=("Arial", 13, "bold"))
    deposit_button.grid(row=2, column=0, pady=(10, 20))
    
    result_label = customtkinter.CTkLabel(deposit_frame, text="", font=("Arial", 13, "bold"), text_color=theme.TEXT_SECONDARY)
    result_label.grid(row=4, column=0, columnspan=2, pady=(10, 5))
    
    back_button = customtkinter.CTkButton(deposit_frame, text="BACK TO DASHBOARD", command=lambda: go_back(deposit_frame, dashboard_frame), width=220, height=42, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_BG, border_width=1, border_color=theme.PRIMARY, text_color=theme.PRIMARY, font=("Arial", 12, "bold"))
    back_button.grid(row=5, column=0, columnspan=2, pady=(15, 30))

def show_withdraw(app, user, dashboard_frame, checking_balance, savings_balance):
    dashboard_frame.grid_remove()
    user_selection = None
    
    def select_account(account):
        nonlocal user_selection
        user_selection = account
        
        result_label.configure(text="")
        
        if account == "Checking":
            checking_button.configure(
                fg_color=theme.PRIMARY,
                text_color=theme.TEXT_PRIMARY
            )
            savings_button.configure(
                fg_color="transparent",
                text_color=theme.TEXT_SECONDARY
            )
        else:
            checking_button.configure(
                fg_color="transparent",
                text_color=theme.TEXT_SECONDARY
            )
            savings_button.configure(
                fg_color=theme.PRIMARY,
                text_color=theme.TEXT_PRIMARY
            )
        amount_frame.grid()
    
    def make_withdrawal():
        amount = amount_entry.get()
        
        try:
            amount = float(amount)
        except ValueError:
            result_label.configure(text="Please enter a valid amount.", text_color=theme.DANGER)
            return
        
        success, result = transactions.withdraw(user, user_selection, amount)
        
        if success:
            result_label.configure(text=f"Withdrawal successful!\nNew Balance: ${result:,.2f}", text_color=theme.SUCCESS)
            amount_entry.delete(0, "end")
            
            if user_selection == "Checking":
                checking_balance.configure(text=f"${result:,.2f}")
            else:
                savings_balance.configure(text=f"${result:,.2f}")
        else:
            result_label.configure(text=result, text_color=theme.DANGER)
    
    withdraw_frame = customtkinter.CTkFrame(app, fg_color=theme.PANEL_BG, corner_radius=theme.FRAME_RADIUS, border_width=1, border_color=theme.BORDER)
    withdraw_frame.grid(row=0, column=0, columnspan=2, padx=40, pady=40, sticky="nsew")
    
    withdraw_frame.grid_columnconfigure(0, weight=1)
    withdraw_frame.grid_columnconfigure(1, weight=1)
    
    title = customtkinter.CTkLabel(withdraw_frame, text="MAKE A WITHDRAWAL", font=("Arial", 26, "bold"), text_color=theme.TEXT_PRIMARY)
    title.grid(row=0, column=0, columnspan=2, pady=(30, 5))
    
    subtitle = customtkinter.CTkLabel(withdraw_frame, text="Withdraw funds from one of your accounts", font=("Arial", 13), text_color=theme.TEXT_MUTED)
    subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 25))
    
    account_frame = customtkinter.CTkFrame(withdraw_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    account_frame.grid(row=2, column=0, columnspan=2, padx=40, pady=(10, 10), sticky="ew")
    
    account_frame.grid_columnconfigure(0, weight=1)
    account_frame.grid_columnconfigure(1, weight=1)
    
    account_label = customtkinter.CTkLabel(account_frame, text="SELECT ACCOUNT", font=("Arial", 14, "bold"), text_color=theme.TEXT_MUTED)
    account_label.grid(row=0, column=0, columnspan=2, pady=(20, 15))
    
    checking_button = customtkinter.CTkButton(account_frame, text="CHECKING", command=lambda: select_account("Checking"), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_HOVER, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_SECONDARY, font=("Arial", 12, "bold"))
    checking_button.grid(row=1, column=0, padx=(20, 10), pady=(0, 20), sticky="ew")
    
    savings_button = customtkinter.CTkButton(account_frame, text="SAVINGS", command=lambda: select_account("Savings"), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_HOVER, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_SECONDARY, font=("Arial", 12, "bold"))
    savings_button.grid(row=1, column=1, padx=(10, 20), pady=(0, 20), sticky="ew")
    
    amount_frame = customtkinter.CTkFrame(withdraw_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    amount_frame.grid(row=3, column=0, columnspan=2, padx=40, pady=10, sticky="ew")
    amount_frame.grid_columnconfigure(0, weight=1)
    
    amount_label = customtkinter.CTkLabel(amount_frame, text="WITHDRAWAL AMOUNT", font=("Arial", 14, "bold"), text_color=theme.TEXT_MUTED)
    amount_label.grid(row=0, column=0, pady=(20, 10))
    
    amount_entry = customtkinter.CTkEntry(amount_frame, width=260, height=44, corner_radius=theme.ENTRY_RADIUS, fg_color=theme.PANEL_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="$0.00", justify="center", font=("Arial", 14))
    amount_entry.grid(row=1, column=0, pady=10)
    
    withdraw_action_button = customtkinter.CTkButton(amount_frame, text="WITHDRAW", command=make_withdrawal, width=260, height=44, corner_radius=theme.BUTTON_RADIUS, fg_color=theme.PRIMARY, hover_color=theme.PRIMARY_HOVER, text_color=theme.TEXT_PRIMARY, font=("Arial", 13, "bold"))
    withdraw_action_button.grid(row=2, column=0, pady=(10, 20))
    
    amount_frame.grid_remove()
    
    result_label = customtkinter.CTkLabel(withdraw_frame, text="", font=("Arial", 13, "bold"), text_color=theme.TEXT_SECONDARY)
    result_label.grid(row=4, column=0, columnspan=2, pady=(10, 5))
    
    back_button = customtkinter.CTkButton(withdraw_frame, text="BACK TO DASHBOARD", command=lambda: go_back(withdraw_frame, dashboard_frame), width=220, height=42, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_BG, border_width=1, border_color=theme.PRIMARY, text_color=theme.PRIMARY, font=("Arial", 12, "bold"))
    back_button.grid(row=5, column=0, columnspan=2, pady=(15, 30))

def show_transfer(app, user, dashboard_frame, checking_balance, savings_balance):
    dashboard_frame.grid_remove()
    from_account = None
    to_account = None
    def select_from(account):
        nonlocal from_account, to_account
        from_account = account
        to_account = None
        
        amount_frame.grid_remove()
        
        to_checking_button.configure(
            fg_color="transparent",
            text_color=theme.TEXT_SECONDARY
        )
        to_savings_button.configure(
            fg_color="transparent",
            text_color=theme.TEXT_SECONDARY
        )
        
        if account == "Checking":
            from_checking_button.configure(
                fg_color=theme.PRIMARY,
                text_color=theme.TEXT_PRIMARY
            )
            from_savings_button.configure(
                fg_color="transparent",
                text_color=theme.TEXT_SECONDARY
            )
        else:
            from_checking_button.configure(
                fg_color="transparent",
                text_color=theme.TEXT_SECONDARY
            )
            from_savings_button.configure(
                fg_color=theme.PRIMARY,
                text_color=theme.TEXT_PRIMARY
            )
        
        if account == "Checking":
            to_checking_button.configure(state="disabled")
            to_savings_button.configure(state="normal")
        else:
            to_checking_button.configure(state="normal")
            to_savings_button.configure(state="disabled")
        
        to_frame.grid()
        
        result_label.configure(text="")
        
    def select_to(account):
        nonlocal to_account
        to_account = account
        
        if account == "Checking":
            to_checking_button.configure(
                fg_color=theme.PRIMARY,
                text_color=theme.TEXT_PRIMARY
            )
            to_savings_button.configure(
                fg_color="transparent",
                text_color=theme.TEXT_SECONDARY
            )
        else:
            to_checking_button.configure(
                fg_color="transparent",
                text_color=theme.TEXT_SECONDARY
            )
            to_savings_button.configure(
                fg_color=theme.PRIMARY,
                text_color=theme.TEXT_PRIMARY
            )
            
        amount_frame.grid()
        
        result_label.configure(text="")
        
    def make_transfer():
        amount = amount_entry.get()
        
        try:
            amount = float(amount)
        except ValueError:
            result_label.configure(text="Please enter a valid amount.", text_color=theme.DANGER)
            return
        
        success, result = transfer.transfer(user, from_account, to_account, amount)
        
        if success:
            result_label.configure(text=(f"Transfer successful!\n"f"{from_account} Balance: ${result['FromBalance']:,.2f}\n"f"{to_account} Balance: ${result['ToBalance']:,.2f}"), text_color=theme.SUCCESS)
            amount_entry.delete(0, "end")
            
            if from_account == "Checking":
                checking_balance.configure(text=f"${result['FromBalance']:,.2f}")
                savings_balance.configure(text=f"${result['ToBalance']:,.2f}")
            else:
                savings_balance.configure(text=f"${result['FromBalance']:,.2f}")
                checking_balance.configure(text=f"${result['ToBalance']:,.2f}")
        else:
            result_label.configure(text=result, text_color=theme.DANGER)
    
    transfer_frame = customtkinter.CTkFrame(app, fg_color=theme.PANEL_BG, corner_radius=theme.FRAME_RADIUS, border_width=1, border_color=theme.BORDER)
    transfer_frame.grid(row=0, column=0, columnspan=2, padx=40, pady=40, sticky="nsew")
    
    transfer_frame.grid_columnconfigure(0, weight=1)
    transfer_frame.grid_columnconfigure(1, weight=1)
    
    title = customtkinter.CTkLabel(transfer_frame, text="TRANSFER FUNDS", font=("Arial", 26, "bold"), text_color=theme.TEXT_PRIMARY)
    title.grid(row=0, column=0, columnspan=2, pady=(30, 5))
    
    subtitle = customtkinter.CTkLabel(transfer_frame, text="Move money between your accounts", font=("Arial", 13), text_color=theme.TEXT_MUTED)
    subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 25))
    
    from_frame = customtkinter.CTkFrame(transfer_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    from_frame.grid(row=2, column=0, columnspan=2, padx=40, pady=(10, 10), sticky="ew")
    
    from_frame.grid_columnconfigure(0, weight=1)
    from_frame.grid_columnconfigure(1, weight=1)
    
    from_label = customtkinter.CTkLabel(from_frame, text="FROM ACCOUNT", font=("Arial", 14, "bold"), text_color=theme.TEXT_MUTED)
    from_label.grid(row=0, column=0, columnspan=2, pady=(20, 15))
    
    from_checking_button = customtkinter.CTkButton(from_frame, text="CHECKING", command=lambda: select_from("Checking"), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_HOVER, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_SECONDARY, font=("Arial", 12, "bold"))
    from_checking_button.grid(row=1, column=0, padx=(20, 10), pady=(0, 20), sticky="ew")
    
    from_savings_button = customtkinter.CTkButton(from_frame, text="SAVINGS", command=lambda: select_from("Savings"), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_HOVER, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_SECONDARY, font=("Arial", 12, "bold"))
    from_savings_button.grid(row=1, column=1, padx=(10, 20), pady=(0, 20), sticky="ew")
    
    to_frame = customtkinter.CTkFrame(transfer_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    to_frame.grid(row=3, column=0, columnspan=2, padx=40, pady=10, sticky="ew")
    
    to_frame.grid_columnconfigure(0, weight=1)
    to_frame.grid_columnconfigure(1, weight=1)
    
    to_label = customtkinter.CTkLabel(to_frame, text="TO ACCOUNT", font=("Arial", 14, "bold"), text_color=theme.TEXT_MUTED)
    to_label.grid(row=0, column=0, columnspan=2, pady=(20, 15))
    
    to_checking_button = customtkinter.CTkButton(to_frame, text="CHECKING", command=lambda: select_to("Checking"), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_HOVER, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_SECONDARY, font=("Arial", 12, "bold"))
    to_checking_button.grid(row=1, column=0, padx=(20, 10), pady=(0, 20), sticky="ew")
    
    to_savings_button = customtkinter.CTkButton(to_frame, text="SAVINGS", command=lambda: select_to("Savings"), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_HOVER, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_SECONDARY, font=("Arial", 12, "bold"))
    to_savings_button.grid(row=1, column=1, padx=(10, 20), pady=(0, 20), sticky="ew")
    
    to_frame.grid_remove()
    
    amount_frame = customtkinter.CTkFrame(transfer_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    amount_frame.grid(row=4, column=0, columnspan=2, padx=40, pady=10, sticky="ew")
    amount_frame.grid_columnconfigure(0, weight=1)
    
    amount_label = customtkinter.CTkLabel(amount_frame, text="TRANSFER AMOUNT", font=("Arial", 14, "bold"), text_color=theme.TEXT_MUTED)
    amount_label.grid(row=0, column=0, pady=(20, 10))
    
    amount_entry=customtkinter.CTkEntry(amount_frame, width=260, height=44, corner_radius=theme.ENTRY_RADIUS, fg_color=theme.PANEL_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="$0.00", justify="center", font=("Arial", 14))
    amount_entry.grid(row=1, column=0, pady=10)
    
    transfer_action_button = customtkinter.CTkButton(amount_frame, text="TRANSFER", command=make_transfer, width=260, height=44, corner_radius=theme.BUTTON_RADIUS, fg_color=theme.PRIMARY, hover_color=theme.PRIMARY_HOVER, text_color=theme.TEXT_PRIMARY, font=("Arial", 13, "bold"))
    transfer_action_button.grid(row=2, column=0, pady=(10, 20))
    
    amount_frame.grid_remove()
    
    result_label = customtkinter.CTkLabel(transfer_frame, text="", font=("Arial", 13, "bold"), text_color=theme.TEXT_SECONDARY)
    result_label.grid(row=5, column=0, columnspan=2, pady=(10, 5))
    
    back_button = customtkinter.CTkButton(transfer_frame, text="BACK TO DASHBOARD", command=lambda: go_back(transfer_frame, dashboard_frame), width=220, height=42, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_BG, border_width=1, border_color=theme.PRIMARY, text_color=theme.PRIMARY, font=("Arial", 12, "bold"))
    back_button.grid(row=6, column=0, columnspan=2, pady=(15, 30))

def show_transaction_history(app, user, dashboard_frame):
    dashboard_frame.grid_remove()
    
    history_frame = customtkinter.CTkFrame(app, fg_color=theme.PANEL_BG, corner_radius=theme.FRAME_RADIUS, border_width=1, border_color=theme.BORDER)
    history_frame.grid(row=0, column=0, columnspan=2, padx=40, pady=40, sticky="nsew")
    history_frame.grid_columnconfigure(0, weight=1)
    history_frame.grid_rowconfigure(2, weight=1)
    
    title = customtkinter.CTkLabel(history_frame, text="TRANSACTION HISTORY", font=("Arial", 26, "bold"), text_color=theme.TEXT_PRIMARY)
    title.grid(row=0, column=0, pady=(30, 5))
    
    subtitle = customtkinter.CTkLabel(history_frame, text="Review your account activity", font=("Arial", 13), text_color=theme.TEXT_MUTED)
    subtitle.grid(row=1, column=0, pady=(0, 25))
    
    dates = transaction_history.get_transaction_dates(user)
    if not dates:
        no_history_label = customtkinter.CTkLabel(history_frame, text="No transaction history available.", font=("Arial", 13), text_color=theme.TEXT_MUTED)
        no_history_label.grid(row=2, column=0, pady=20)
    else:
        dates_frame = customtkinter.CTkScrollableFrame(history_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER, height=430)
        dates_frame.grid(row=2, column=0, padx=40, pady=(10, 10), sticky="nsew")
        dates_frame.grid_columnconfigure(0, weight=1)
    
        dates_title = customtkinter.CTkLabel(dates_frame, text="SELECT A DATE", font=("Arial", 14, "bold"), text_color=theme.TEXT_MUTED)
        dates_title.grid(row=0, column=0, pady=(20, 15))
    
    def open_transaction_date(transaction_date):
        success, result = transaction_history.get_transactions(user, transaction_date)
        if not success:
            return
        
        history_frame.grid_remove()
        
        details_frame = customtkinter.CTkFrame(app, fg_color=theme.PANEL_BG, corner_radius=theme.FRAME_RADIUS, border_width=1, border_color=theme.BORDER)
        details_frame.grid(row=0, column=0, columnspan=2, padx=40, pady=40, sticky="nsew")
        details_frame.tkraise()
        
        details_title = customtkinter.CTkLabel(details_frame, text=f"TRANSACTION DETAILS", font=("Arial", 26, "bold"), text_color=theme.TEXT_PRIMARY)
        details_title.pack(pady=(30, 5))
        
        details_date = customtkinter.CTkLabel(details_frame, text=transaction_date, font=("Arial", 13), text_color=theme.TEXT_MUTED)
        details_date.pack(pady=(0, 20))
        
        transactions_frame = customtkinter.CTkScrollableFrame(details_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER, height=430)
        transactions_frame.pack(padx=40, pady=(10, 10), fill="both", expand=True)
        
        def toggle_transaction_details(details_frame):
            if details_frame.winfo_ismapped():
                details_frame.grid_remove()
            else:
                details_frame.grid()
        
        for transaction in result:
            transaction_card = customtkinter.CTkFrame(transactions_frame, fg_color=theme.PANEL_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
            transaction_card.pack(padx=10, pady=8, fill="x")
            
            transaction_type = transaction["Transaction Type"]
            amount = float(transaction["Amount"])
            
            type_label = customtkinter.CTkLabel(transaction_card, text=transaction_type.upper(), font=("Arial", 14, "bold"), text_color=theme.TEXT_PRIMARY, cursor="hand2")
            type_label.grid(row=0, column=0, padx=20, pady=(16, 5), sticky="w")
            
            amount_label = customtkinter.CTkLabel(transaction_card, text=f"${amount:,.2f}", font=("Arial", 16, "bold"), text_color=theme.TEXT_PRIMARY, cursor="hand2")
            amount_label.grid(row=0, column=1, padx=20, pady=(16, 5), sticky="e")
            
            description_label = customtkinter.CTkLabel(transaction_card, text=transaction["Description"], font=("Arial", 12), text_color=theme.TEXT_SECONDARY, cursor="hand2")
            description_label.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 12), sticky="w")
            
            details_info_frame = customtkinter.CTkFrame(transaction_card, fg_color="transparent")
            details_info_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 15), sticky="ew")
            
            time_label = customtkinter.CTkLabel(details_info_frame, text=f"Time: {transaction['Time']}", font=("Arial", 11), text_color=theme.TEXT_MUTED)
            time_label.pack(side="left")
            
            transaction_id_label = customtkinter.CTkLabel(details_info_frame, text=f"Transaction #{transaction['Transaction ID']}", font=("Arial", 11), text_color=theme.TEXT_MUTED)
            transaction_id_label.pack(side="right")
            
            details_info_frame.grid_remove()
            
            type_label.bind("<Button-1>", lambda event, frame=details_info_frame: toggle_transaction_details(frame))
            
            amount_label.bind("<Button-1>", lambda event, frame=details_info_frame: toggle_transaction_details(frame))
            
            description_label.bind("<Button-1>", lambda event, frame=details_info_frame: toggle_transaction_details(frame))
            
            transaction_card.grid_columnconfigure(0, weight=1)
            transaction_card.grid_columnconfigure(1, weight=1)
        
        back_history_button = customtkinter.CTkButton(details_frame, text="BACK TO HISTORY", command=lambda: go_back(details_frame, history_frame), width=220, height=42, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_BG, border_width=1, border_color=theme.PRIMARY, text_color=theme.PRIMARY, font=("Arial", 12, "bold"))
        back_history_button.pack(pady=(10, 30))
        
        details_frame.update_idletasks()
    if dates:
        for index, transaction_date in enumerate(dates):
            date_button = customtkinter.CTkButton(dates_frame, text=transaction_date, command=lambda date=transaction_date: open_transaction_date(date), height=42, corner_radius=theme.BUTTON_RADIUS, fg_color=theme.PANEL_BG, hover_color=theme.CARD_HOVER, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, font=("Arial", 12, "bold"))
            date_button.grid(row=index + 1, column=0, padx=20, pady=5, sticky="ew")
    
        dates_frame.grid_columnconfigure(0, weight=1)
    
    back_button = customtkinter.CTkButton(history_frame, text="BACK TO DASHBOARD", command=lambda: go_back(history_frame, dashboard_frame), width=220, height=42, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_BG, border_width=1, border_color=theme.PRIMARY, text_color=theme.PRIMARY, font=("Arial", 12, "bold"))
    back_button.grid(row=3, column=0, pady=(15, 30))

def view_account(app, user, dashboard_frame):
    dashboard_frame.grid_remove()
    account_frame = customtkinter.CTkFrame(app, fg_color=theme.PANEL_BG, corner_radius=theme.FRAME_RADIUS, border_width=1, border_color=theme.BORDER)
    account_frame.grid(row=0, column=0, columnspan=2, padx=40, pady=40, sticky="nsew")
    account_frame.grid_columnconfigure(0, weight=1)
    
    title = customtkinter.CTkLabel(account_frame, text="ACCOUNT DETAILS", font=("Arial", 26, "bold"), text_color=theme.TEXT_PRIMARY)
    title.grid(row=0, column=0, pady=(30, 5))
    
    subtitle = customtkinter.CTkLabel(account_frame, text="Your personal and account information", font=("Arial", 13), text_color=theme.TEXT_MUTED)
    subtitle.grid(row=1, column=0, pady=(0, 20))
    
    personal_frame = customtkinter.CTkFrame(account_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    personal_frame.grid(row=2, column=0, padx=40, pady=(10, 10), sticky="ew")
    
    balances_frame = customtkinter.CTkFrame(account_frame, fg_color="transparent")
    balances_frame.grid(row=3, column=0, padx=40, pady=(5, 10), sticky="ew")
    
    balances_frame.grid_columnconfigure(0, weight=1)
    balances_frame.grid_columnconfigure(1, weight=1)
    
    balances_title = customtkinter.CTkLabel(balances_frame, text="ACCOUNT BALANCES", font=("Arial", 14, "bold"), text_color=theme.TEXT_MUTED)
    balances_title.grid(row=0, column=0, columnspan=2, pady=(0, 10))
    
    checking_card = customtkinter.CTkFrame(balances_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    checking_card.grid(row=1, column=0, padx=(0, 10), sticky="nsew")
    
    personal_title = customtkinter.CTkLabel(personal_frame, text="PERSONAL INFORMATION", font=("Arial", 14, "bold"), text_color=theme.TEXT_MUTED)
    personal_title.grid(row=0, column=0, columnspan=2, pady=(20, 15))
    
    personal_frame.grid_columnconfigure(0, weight=1)
    personal_frame.grid_columnconfigure(1, weight=1)
    
    personal_frame.grid_rowconfigure(1, weight=1)
    personal_frame.grid_rowconfigure(2, weight=1)
    
    name_card = customtkinter.CTkFrame(personal_frame, fg_color=theme.PANEL_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER, height=110)
    name_card.grid(row=1, column=0, padx=(20, 10), pady=(5, 10), sticky="nsew")
    name_card.grid_propagate(False)
    
    name_card.grid_rowconfigure(0, weight=1)
    name_card.grid_rowconfigure(1, weight=1)
    name_card.grid_columnconfigure(0, weight=1)
    
    name_label = customtkinter.CTkLabel(name_card, text="NAME", font=("Arial", 11, "bold"), text_color=theme.TEXT_MUTED)
    name_label.grid(row=0, column=0, pady=(15, 5))
    
    name_value = customtkinter.CTkLabel(name_card, text=f"{user['First name']} {user['Last name']}", font=("Arial", 14, "bold"), text_color=theme.TEXT_PRIMARY)
    name_value.grid(row=1, column=0, pady=(5, 15))
    
    username_card = customtkinter.CTkFrame(personal_frame, fg_color=theme.PANEL_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER, height=110)
    username_card.grid(row=1, column=1, padx=(10, 20), pady=(5, 10), sticky="nsew")
    username_card.grid_propagate(False)
    
    username_card.grid_rowconfigure(0, weight=1)
    username_card.grid_rowconfigure(1, weight=1)
    username_card.grid_columnconfigure(0, weight=1)
    
    username_label = customtkinter.CTkLabel(username_card, text="USERNAME", font=("Arial", 11, "bold"), text_color=theme.TEXT_MUTED)
    username_label.grid(row=0, column=0, pady=(15, 5))

    username_value = customtkinter.CTkLabel(username_card, text=user["Username"], font=("Arial", 14, "bold"), text_color=theme.TEXT_PRIMARY)
    username_value.grid(row=1, column=0, pady=(5, 15))

    email_card = customtkinter.CTkFrame(personal_frame, fg_color=theme.PANEL_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER, height=110)
    email_card.grid(row=2, column=0, padx=(20, 10), pady=(10, 20), sticky="nsew")
    email_card.grid_propagate(False)
    
    email_card.grid_rowconfigure(0, weight=1)
    email_card.grid_rowconfigure(1, weight=1)
    email_card.grid_columnconfigure(0, weight=1)

    email_label = customtkinter.CTkLabel(email_card,text="EMAIL", font=("Arial", 11, "bold"), text_color=theme.TEXT_MUTED)
    email_label.grid(row=0, column=0, pady=(15, 5))
    
    email_value = customtkinter.CTkLabel(email_card, text=user["Email"], font=("Arial", 14, "bold"), text_color=theme.TEXT_PRIMARY)
    email_value.grid(row=1, column=0, pady=(5, 15))
    
    user_id_card = customtkinter.CTkFrame(personal_frame, fg_color=theme.PANEL_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER, height=110)
    user_id_card.grid(row=2, column=1, padx=(10, 20), pady=(10, 20), sticky="nsew")
    user_id_card.grid_propagate(False)
    
    user_id_card.grid_rowconfigure(0, weight=1)
    user_id_card.grid_rowconfigure(1, weight=1)
    user_id_card.grid_columnconfigure(0, weight=1)

    user_id_label = customtkinter.CTkLabel(user_id_card, text="USER ID", font=("Arial", 11, "bold"), text_color=theme.TEXT_MUTED)
    user_id_label.grid(row=0, column=0, pady=(15, 5))

    user_id_value = customtkinter.CTkLabel(user_id_card, text=user["UserID"], font=("Arial", 14, "bold"), text_color=theme.TEXT_PRIMARY)
    user_id_value.grid(row=1, column=0, pady=(5, 15))
    
    checking_label = customtkinter.CTkLabel(checking_card, text="CHECKING",font=("Arial", 12, "bold"), text_color=theme.TEXT_MUTED)
    checking_label.pack(pady=(20, 5))

    checking_value = customtkinter.CTkLabel(checking_card, text=f"${user['CheckingBalance']:,.2f}", font=("Arial", 24, "bold"), text_color=theme.TEXT_PRIMARY)
    checking_value.pack(pady=(5, 20))
    
    savings_card = customtkinter.CTkFrame(balances_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    savings_card.grid(row=1, column=1, padx=(10, 0), sticky="nsew")

    savings_label = customtkinter.CTkLabel(savings_card,text="SAVINGS", font=("Arial", 12, "bold"), text_color=theme.TEXT_MUTED)
    savings_label.pack(pady=(20, 5))

    savings_value = customtkinter.CTkLabel(savings_card, text=f"${user['SavingsBalance']:,.2f}", font=("Arial", 24, "bold"), text_color=theme.TEXT_PRIMARY)
    savings_value.pack(pady=(5, 20))
    
    back_button = customtkinter.CTkButton(account_frame, text="BACK TO DASHBOARD", command=lambda: go_back(account_frame, dashboard_frame), width=220, height=42, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_BG, border_width=1, border_color=theme.PRIMARY, text_color=theme.PRIMARY, font=("Arial", 12, "bold"))
    back_button.grid(row=4, column=0, pady=(15, 30))

def show_dashboard(app, user, login_frame):
    """Display the user's dashboard"""
    dashboard_frame = customtkinter.CTkFrame(app, fg_color=theme.PANEL_BG, corner_radius=theme.FRAME_RADIUS, border_width=1, border_color=theme.BORDER)
    dashboard_frame.grid(row=0, column=0, columnspan=2, padx=40, pady=40, sticky="nsew")
    
    def logout():
        dashboard_frame.destroy()
        login_frame.grid()
        login_frame.update_idletasks()
    
    title = customtkinter.CTkLabel(dashboard_frame, text="BANK DASHBOARD", font=("Arial", 26, "bold"), text_color=theme.TEXT_PRIMARY)
    title.pack(pady=(30, 5))
    
    welcome = customtkinter.CTkLabel(dashboard_frame, text=f"Welcome back, {user['First name']}!", font=("Arial", 14), text_color=theme.TEXT_MUTED)
    welcome.pack(pady=(0, 20))
    
    accounts_frame = customtkinter.CTkFrame(dashboard_frame, fg_color="transparent")
    accounts_frame.pack(pady=(10, 5), padx=30, fill="x")
    
    actions_frame = customtkinter.CTkFrame(dashboard_frame, fg_color="transparent")
    actions_frame.pack(pady=(5, 10), padx=30, fill="x")
    
    for column in range(6):
        actions_frame.grid_columnconfigure(column, weight=1)
    
    checking_frame = customtkinter.CTkFrame(accounts_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    checking_frame.grid(row=0, column=0, padx=(0, 10), pady=10, sticky="nsew")
    accounts_frame.grid_columnconfigure(0, weight=1)
    
    checking_title = customtkinter.CTkLabel(checking_frame, text="CHECKING", font=("Arial", 13, "bold"), text_color=theme.TEXT_MUTED)
    checking_title.pack(pady=(20, 5))
    
    checking_balance = customtkinter.CTkLabel(checking_frame, text=f"${user['CheckingBalance']:,.2f}", font=("Arial", 26, "bold"), text_color=theme.TEXT_PRIMARY)
    checking_balance.pack(pady=(5, 20))
    
    savings_frame = customtkinter.CTkFrame(accounts_frame, fg_color=theme.CARD_BG, corner_radius=theme.CARD_RADIUS, border_width=1, border_color=theme.BORDER)
    savings_frame.grid(row=0, column=1, padx=(10, 0), pady=10, sticky="nsew")
    accounts_frame.grid_columnconfigure(1, weight=1)
    
    savings_title = customtkinter.CTkLabel(savings_frame, text="SAVINGS", font=("Arial", 13, "bold"), text_color=theme.TEXT_MUTED)
    savings_title.pack(pady=(20, 5))
    
    savings_balance = customtkinter.CTkLabel(savings_frame, text=f"${user['SavingsBalance']:,.2f}", font=("Arial", 26, "bold"), text_color=theme.TEXT_PRIMARY)
    savings_balance.pack(pady=(5, 20))
    
    actions_title = customtkinter.CTkLabel(actions_frame, text="QUICK ACTIONS", font=("Arial", 13, "bold"), text_color=theme.TEXT_MUTED)
    actions_title.grid(row=0, column=0, columnspan=6, pady=(0, 10))
    
    view_account_button = customtkinter.CTkButton(actions_frame, text="VIEW ACCOUNT", command=lambda: view_account(app, user, dashboard_frame), height=42, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_BG, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_SECONDARY, font=("Arial", 12, "bold"))
    view_account_button.grid(row=2, column=0, columnspan=3, padx=(0, 6), pady=6, sticky="ew")
    
    deposit_button = customtkinter.CTkButton(actions_frame, text="DEPOSIT", command=lambda: show_deposit(app, user, dashboard_frame, checking_balance, savings_balance), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color=theme.PRIMARY, hover_color=theme.PRIMARY_HOVER, text_color=theme.TEXT_PRIMARY, font=("Arial", 13, "bold"))
    deposit_button.grid(row=1, column=0, columnspan=2, padx=(0, 6), pady=6, sticky="ew")
    
    withdraw_button = customtkinter.CTkButton(actions_frame, text="WITHDRAW", command=lambda: show_withdraw(app, user, dashboard_frame, checking_balance, savings_balance), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color=theme.PRIMARY, hover_color=theme.PRIMARY_HOVER, text_color=theme.TEXT_PRIMARY, font=("Arial", 13, "bold"))
    withdraw_button.grid(row=1, column=2, columnspan=2, padx=6, pady=6, sticky="ew")
    
    transfer_button = customtkinter.CTkButton(actions_frame, text="TRANSFER", command=lambda: show_transfer(app, user, dashboard_frame, checking_balance, savings_balance), height=44, corner_radius=theme.BUTTON_RADIUS, fg_color=theme.PRIMARY, hover_color=theme.PRIMARY_HOVER, text_color=theme.TEXT_PRIMARY, font=("Arial", 13, "bold"))
    transfer_button.grid(row=1, column=4, columnspan=2, padx=(6, 0), pady=6, sticky="ew")
    
    transaction_history_button = customtkinter.CTkButton(actions_frame, text="TRANSACTION HISTORY", command=lambda: show_transaction_history(app, user, dashboard_frame), height=42, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_BG, border_width=1, border_color=theme.BORDER, text_color=theme.TEXT_SECONDARY, font=("Arial", 12, "bold"))
    transaction_history_button.grid(row=2, column=3, columnspan=3, padx=(6, 0), pady=6, sticky="ew")
    
    logout_frame = customtkinter.CTkFrame(actions_frame, fg_color="transparent")
    logout_frame.grid(row=3, column=0, columnspan=6, pady=(15, 5), sticky="ew")
    
    logout_button = customtkinter.CTkButton(logout_frame, text="LOGOUT", command=logout, width=180, height=40, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.DANGER, border_width=1, border_color=theme.DANGER, text_color=theme.DANGER, font=("Arial", 12, "bold"))
    logout_button.pack()