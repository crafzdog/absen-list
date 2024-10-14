from menu import Menu


# a main() function acts as entry point executed when the script is starts
def main():
    while True:

        print("================ MENU ================")
        print("1. Tambah Data Mahasiswa.")
        print("2. Daftar Data Mahasiswa.")
        print("3. Exit.")

        choice = input("\nMasukkan Menu yang anda pilih : ")

        match (choice):
            case Menu.TAMBAH.value:
                print("Tambah Siswa...")

            case Menu.DAFTAR.value:
                print("Daftar Mahasiswa...")

            case Menu.EXIT.value:
                print("Exit...")
                break


# ensures that the main() function is executed only when the script is run directly
if __name__ == "__main__":
    main()
