import customtkinter
from .. import login
from .. import register
from . import dashboard

def show_register():
    login_frame.grid_remove()
    
    register_frame = customtkinter.CTkFrame(app)
    register_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
    
    register_frame.grid_columnconfigure(0, weight=1)
    register_frame.grid_columnconfigure(1, weight=1)
    
    def go_back_to_login(register_frame):
        register_frame.destroy()
        login_frame.grid()
        login_frame.update_idletasks()
    
    title = customtkinter.CTkLabel(register_frame, text="CREATE ACCOUNT", font=("Arial", 24, "bold"))
    title.grid(row=0, column=0, columnspan=2, pady=(20, 15))
    
    fname_label = customtkinter.CTkLabel(register_frame, text="FIRST NAME:")
    fname_label.grid(row=1, column=0, padx=10, pady=8, sticky="e")
    fname_entry = customtkinter.CTkEntry(register_frame, width=250)
    fname_entry.grid(row=1, column=1, padx=10, pady=8, sticky="w")
    
    lname_label = customtkinter.CTkLabel(register_frame, text="LAST NAME:")
    lname_label.grid(row=2, column=0, padx=10, pady=8, sticky="e")
    lname_entry = customtkinter.CTkEntry(register_frame, width=250)
    lname_entry.grid(row=2, column=1, padx=10, pady=8, sticky="w")
    
    email_label = customtkinter.CTkLabel(register_frame, text="EMAIL:")
    email_label.grid(row=3, column=0, padx=10, pady=8, sticky="e")
    email_entry = customtkinter.CTkEntry(register_frame, width=250)
    email_entry.grid(row=3, column=1, padx=10, pady=8, sticky="w")
    
    username_register_label = customtkinter.CTkLabel(register_frame, text="USERNAME:")
    username_register_label.grid(row=4, column=0, padx=10, pady=8, sticky="e")
    username_register_entry = customtkinter.CTkEntry(register_frame, width=250)
    username_register_entry.grid(row=4, column=1, padx=10, pady=8, sticky="w")
    
    password_register_label = customtkinter.CTkLabel(register_frame, text="PASSWORD:")
    password_register_label.grid(row=5, column=0, padx=10, pady=8, sticky="e")
    password_register_entry = customtkinter.CTkEntry(register_frame, width=250, show="*")
    password_register_entry.grid(row=5, column=1, padx=10, pady=8, sticky="w")
    
    confirm_password_label = customtkinter.CTkLabel(register_frame, text="CONFIRM PASSWORD:")
    confirm_password_label.grid(row=6, column=0, padx=10, pady=8, sticky="e")
    confirm_password_entry = customtkinter.CTkEntry(register_frame, width=250, show="*")
    confirm_password_entry.grid(row=6, column=1, padx=10, pady=8, sticky="w")
    
    password_requirements = customtkinter.CTkLabel(register_frame, text=("Password requirements:\n""At least 8 characters • Uppercase • Lowercase\n""Number • Special character • No spaces"), font=("Arial", 11), justify="left")
    password_requirements.grid(row=7, column=0, columnspan=2, pady=(5, 10))
    
    register_result_label= customtkinter.CTkLabel(register_frame, text="")
    register_result_label.grid(row=8, column=0, columnspan=2, pady=5)
    
    def create_new_account():
        fname = fname_entry.get()
        lname = lname_entry.get()
        email = email_entry.get()
        username_value = username_register_entry.get()
        password_value = password_register_entry.get()
        confirm_value = confirm_password_entry.get()
        
        success, result = register.create_account(
            fname,
            lname,
            email,
            username_value,
            password_value,
            confirm_value
        )
        
        if success:
            register_result_label.configure(
                text=f"Account created successfully!\nReturn back to login to log in to your account\nUser ID: {result['UserID']}",
                text_color="green"
            )
            
            fname_entry.delete(0, "end")
            lname_entry.delete(0, "end")
            email_entry.delete(0, "end")
            username_register_entry.delete(0, "end")
            password_register_entry.delete(0, "end")
            confirm_password_entry.delete(0, "end")
        else:
            register_result_label.configure(
                text=result,
                text_color="red"
            )
    
    create_account_button = customtkinter.CTkButton(register_frame, text="[ CREATE ACCOUNT ]", command=create_new_account)
    create_account_button.grid(row=9, column=1, padx=10, pady=(10, 5))
    
    back_login_button = customtkinter.CTkButton(register_frame, text="[ BACK TO LOGIN ]", command=lambda: go_back_to_login(register_frame))
    back_login_button.grid(row=9, column=0, padx=10, pady=(10, 5))

def handle_login():
    username_value = username.get()
    password_value = password.get()
    success, result = login.login(username_value, password_value)
    if success:
        error_label.configure(text="")
        username.delete(0, "end")
        password.delete(0, "end")
        login_frame.grid_remove()
        dashboard.show_dashboard(app, result, login_frame)
    else:
        error_label.configure(text=result, text_color="red") # Text displays in a red color

app = customtkinter.CTk()

app.title("Bank Management")
app.geometry("800x600")
login_frame = customtkinter.CTkFrame(app)
login_frame.grid(row=0, column=0, columnspan=2, pady=10)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

title = customtkinter.CTkLabel(login_frame, text="BANKING MANAGEMENT", font=("Arial", 24, "bold"))
title.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

username_label = customtkinter.CTkLabel(login_frame, text="USERNAME:")
username = customtkinter.CTkEntry(login_frame, width=250)
username_label.grid(row=1, column=0, pady=10, padx=10, sticky="e")
username.grid(row=1, column=1, pady=10, padx=10)

password_label = customtkinter.CTkLabel(login_frame, text="PASSWORD: ")
password = customtkinter.CTkEntry(login_frame, show="*", width=250)
password_label.grid(row=2, column=0, pady=10, padx=10, sticky="e")
password.grid(row=2, column=1, pady=10, padx=10)

login_button = customtkinter.CTkButton(login_frame, text="[ LOGIN ]", command=handle_login)
login_button.grid(row=3, column=0, columnspan=2, pady=10, padx=10)

error_label = customtkinter.CTkLabel(login_frame, text="")
error_label.grid(row=4, column=0, columnspan=2, pady = 5, padx=10)

no_account = customtkinter.CTkLabel(login_frame, text="Don't have an account?")
no_account.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

register_button = customtkinter.CTkButton(login_frame, text="[ REGISTER ]", command=show_register)
register_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

app.mainloop()