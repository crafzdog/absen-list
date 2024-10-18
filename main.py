from menu import Menu
from logic import login,load,register
from user_option import user_option

# a main() function acts as entry point executed when the script is starts
def main():
    while True:

        print("================ MENU ================")
        print("1. Register Mahasiswa.")
        print("2. Login Data Mahasiswa.")
        print("0. Exit.")

        choice = input("\nMasukkan Menu yang anda pilih : ").lower()

        if not handle_menu_option(choice):
            break

def handle_menu_option(user_input: str) -> int:
    match (user_input):
        case _ if user_input in Menu.Register.value:
            register()
            return 1;
        case _ if user_input in Menu.Login.value:
            login()
            return 1;
        case _ if user_input in Menu.EXIT.value:
            return 0;


# ensures that the main() function is executed only when the script is run directly
if __name__ == "__main__":
    main()
