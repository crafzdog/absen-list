from menu import Menu
from logic import login,load,register

# a main() function acts as entry point executed when the script is starts
def main():
    while True:

        print("================ MENU ================")
        print("1. Register Mahasiswa.")
        print("2. Login Data Mahasiswa.")
        print("0. Exit.")

        choice = input("\nMasukkan Menu yang anda pilih : ")

        match (choice):
            case Menu.Register.value:
                register()

            case Menu.Login.value:
                login()

            case Menu.EXIT.value:
                print(f"Exit...\n Cya ~~~")
                break


# ensures that the main() function is executed only when the script is run directly
if __name__ == "__main__":
    main()
