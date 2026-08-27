import customtkinter
from .. import login
from .. import register
from . import dashboard
from . import theme

def show_register():
    login_frame.grid_remove()
    
    register_frame = customtkinter.CTkFrame(app, fg_color=theme.PANEL_BG, corner_radius=theme.FRAME_RADIUS, border_width=1, border_color=theme.BORDER)
    register_frame.grid(row=0, column=0, columnspan=2, padx=50, pady=50, sticky="nsew")
    
    register_frame.grid_columnconfigure(0, weight=1)
    register_frame.grid_columnconfigure(1, weight=1)
    
    def go_back_to_login(register_frame):
        register_frame.destroy()
        login_frame.grid()
        login_frame.update_idletasks()
    
    title = customtkinter.CTkLabel(register_frame, text="CREATE ACCOUNT", font=("Arial", 24, "bold"), text_color=theme.TEXT_PRIMARY)
    title.grid(row=0, column=0, columnspan=2, pady=(20, 5))
    
    register_subtitle = customtkinter.CTkLabel(register_frame, text="Set up your banking profile", font=("Arial", 13), text_color=theme.TEXT_MUTED)
    register_subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 25))
    
    left_form = customtkinter.CTkFrame(register_frame, fg_color="transparent")
    left_form.grid(row=2, column=0, padx=(30, 15), pady=10, sticky="n")
    
    right_form = customtkinter.CTkFrame(register_frame, fg_color="transparent")
    right_form.grid(row=2, column=1, padx=(15, 30), pady=10, sticky="n")
    
    fname_label = customtkinter.CTkLabel(left_form, text="FIRST NAME:", text_color=theme.TEXT_SECONDARY, anchor="w")
    fname_label.pack(anchor="w", pady=(0, 5))
    fname_entry = customtkinter.CTkEntry(left_form, width=240, height=42, corner_radius=theme.ENTRY_RADIUS, fg_color=theme.CARD_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="First name")
    fname_entry.pack(pady=(0, 15))
    
    lname_label = customtkinter.CTkLabel(right_form, text="LAST NAME:", text_color=theme.TEXT_SECONDARY, anchor="w")
    lname_label.pack(anchor="w", pady=(0, 5))
    lname_entry = customtkinter.CTkEntry(right_form, width=240, height=42, corner_radius=theme.ENTRY_RADIUS, fg_color=theme.CARD_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="Last name")
    lname_entry.pack(pady=(0, 15))
    
    email_label = customtkinter.CTkLabel(left_form, text="EMAIL:", text_color=theme.TEXT_SECONDARY, anchor="w")
    email_label.pack(anchor="w", pady=(0, 5))
    email_entry = customtkinter.CTkEntry(left_form, width=240, height=42, corner_radius=theme.ENTRY_RADIUS, fg_color=theme.CARD_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="Email address")
    email_entry.pack(pady=(0, 15))
    
    username_register_label = customtkinter.CTkLabel(right_form, text="USERNAME:", text_color=theme.TEXT_SECONDARY, anchor="w")
    username_register_label.pack(anchor="w", pady=(0, 5))
    username_register_entry = customtkinter.CTkEntry(right_form, width=240, height=42, corner_radius=theme.ENTRY_RADIUS, fg_color=theme.CARD_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="Username")
    username_register_entry.pack(pady=(0, 15))
    
    password_register_label = customtkinter.CTkLabel(left_form, text="PASSWORD:", text_color=theme.TEXT_SECONDARY, anchor="w")
    password_register_label.pack(anchor="w", pady=(0, 5))
    password_register_entry = customtkinter.CTkEntry(left_form, width=240, height=42, show="*", corner_radius=theme.ENTRY_RADIUS, fg_color=theme.CARD_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="Password")
    password_register_entry.pack(pady=(0, 15))
    
    confirm_password_label = customtkinter.CTkLabel(right_form, text="CONFIRM PASSWORD:", text_color=theme.TEXT_SECONDARY, anchor="w")
    confirm_password_label.pack(anchor="w", pady=(0, 5))
    confirm_password_entry = customtkinter.CTkEntry(right_form, width=240, height=42, show="*", corner_radius=theme.ENTRY_RADIUS, fg_color=theme.CARD_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="Confirm password")
    confirm_password_entry.pack(pady=(0, 15))
    
    password_requirements = customtkinter.CTkLabel(register_frame, text=("Password requirements:\n""8+ characters • Uppercase • Lowercase • Number • Special character • No spaces"), font=("Arial", 11), text_color=theme.TEXT_MUTED)
    password_requirements.grid(row=3, column=0, columnspan=2, pady=(10, 5))
    
    register_result_label= customtkinter.CTkLabel(register_frame, text="")
    register_result_label.grid(row=4, column=0, columnspan=2, pady=5)
    
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
    
    create_account_button = customtkinter.CTkButton(register_frame, text="CREATE ACCOUNT", command=create_new_account, width=200, height=44, corner_radius=theme.BUTTON_RADIUS, fg_color=theme.PRIMARY, hover_color=theme.PRIMARY_HOVER, text_color=theme.TEXT_PRIMARY, font=("Arial", 13, "bold"))
    create_account_button.grid(row=5, column=1, padx=(10, 30), pady=(15, 30), sticky="w")
    
    back_login_button = customtkinter.CTkButton(register_frame, text="BACK TO LOGIN", command=lambda: go_back_to_login(register_frame), width=200, height=44, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_BG, border_width=1, border_color=theme.PRIMARY, text_color=theme.PRIMARY)
    back_login_button.grid(row=5, column=0, padx=(30, 10), pady=(15, 30), sticky="e")

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

app = customtkinter.CTk(fg_color=theme.APP_BG)

app.title("Bank Management")
app.geometry("720x820")
app.minsize(650, 760)
login_frame = customtkinter.CTkFrame(app, fg_color=theme.PANEL_BG, corner_radius=theme.FRAME_RADIUS, border_width=1, border_color=theme.BORDER)
login_frame.grid(row=0, column=0, columnspan=2, padx=70, pady=60)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)

title = customtkinter.CTkLabel(login_frame, text="BANKING MANAGEMENT", font=("Arial", 24, "bold"), text_color=theme.TEXT_PRIMARY)
title.grid(row=0, column=0, columnspan=2, pady=20, padx=10)

subtitle = customtkinter.CTkLabel(login_frame, text="Secure access to your accounts", font=("Arial", 13), text_color=theme.TEXT_MUTED)
subtitle.grid(row=1, column=0, columnspan=2, pady=(0, 20))

form_frame = customtkinter.CTkFrame(login_frame, fg_color="transparent")
form_frame.grid(row=2, column=0, columnspan=2, padx=40, pady=(20, 10))

username_label = customtkinter.CTkLabel(form_frame, text="USERNAME:", width=110, anchor="e", text_color=theme.TEXT_PRIMARY)
username_label.grid(row=0, column=0, padx=(0, 15), pady=10)
username = customtkinter.CTkEntry(form_frame, width=280, height=42, corner_radius=theme.ENTRY_RADIUS, fg_color=theme.CARD_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="Enter your username")
username.grid(row=0, column=1, pady=10)

password_label = customtkinter.CTkLabel(form_frame, text="PASSWORD:", width=110, anchor="e", text_color=theme.TEXT_PRIMARY)
password_label.grid(row=1, column=0, padx=(0, 15), pady=10)
password = customtkinter.CTkEntry(form_frame, width=280, height=42, show="*", corner_radius=theme.ENTRY_RADIUS, fg_color=theme.CARD_BG, border_color=theme.BORDER, text_color=theme.TEXT_PRIMARY, placeholder_text="Enter your password")
password.grid(row=1, column=1, pady=10)

login_button = customtkinter.CTkButton(login_frame, text="LOGIN", command=handle_login, width=280, height=44, corner_radius=theme.BUTTON_RADIUS, fg_color=theme.PRIMARY, hover_color=theme.PRIMARY_HOVER, text_color=theme.TEXT_PRIMARY, font=("Arial", 14, "bold"))
login_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

error_label = customtkinter.CTkLabel(login_frame, text="")
error_label.grid(row=5, column=0, columnspan=2, pady = 5, padx=10)

no_account = customtkinter.CTkLabel(login_frame, text="Don't have an account?", text_color=theme.TEXT_SECONDARY)
no_account.grid(row=6, column=0, padx=(20, 10), pady=(20, 25), sticky="e")

register_button = customtkinter.CTkButton(login_frame, text="CREATE ACCOUNT", command=show_register, width=160, height=40, corner_radius=theme.BUTTON_RADIUS, fg_color="transparent", hover_color=theme.CARD_BG, border_width=1, border_color=theme.PRIMARY, text_color=theme.PRIMARY)
register_button.grid(row=6, column=1, padx=(10, 20), pady=(20, 25), sticky="w")

app.mainloop()