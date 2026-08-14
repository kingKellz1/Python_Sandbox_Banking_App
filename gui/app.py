import customtkinter
from .. import login
from . import dashboard

def handle_login():
    username_value = username.get()
    password_value = password.get()
    success, result = login.login(username_value, password_value)
    if success:
        error_label.configure(text="")
        login_frame.grid_remove()
        dashboard.show_dashboard(app, result)
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

register_button = customtkinter.CTkButton(login_frame, text="[ REGISTER ]")
register_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10)

app.mainloop()