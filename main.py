import utils
import login
import register
import dashboard
import pwinput

while True:
    utils.clear_screen()
    print("================================")
    print("       BANK MANAGEMENT")
    print("================================")

    try:
        menu_selection = int(input("\n\n1. Login \n2. Register\n3. Exit \n\n\nSelection:"))
    except ValueError:
        print("Invalid input. Please enter a number corresponding to the menu options.")
        input("\nPress enter to continue...")
        continue
    if menu_selection == 1:
        utils.clear_screen()
        username = input("Enter Username: ").strip()
        password = pwinput.pwinput("Enter Password: ", mask="*")
        success, result = login.login(username, password)
        if success:
            utils.clear_screen()
            dashboard.dashboard(result)
        else:
            print(result)
            input("\nPress enter to continue...")
    elif menu_selection == 2:
        utils.clear_screen()
        register.register()

    elif menu_selection == 3:
        utils.clear_screen()
        print("Goodbye!")
        break
    else:
        print("Invalid selection. Please try again.")
        input("\nPress enter to continue...")