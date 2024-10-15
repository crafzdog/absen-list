def load():
    with open("acc.txt","r")as file:
        return file.read().splitlines() if file.readable() else []
    
data_acc = load()

def register():
    while True :
        print("========= Register =========")
        username = str(input("Ketikan Username = "))
        password = str(input("Ketikan Password = "))

        if any(f"username == '{username}'" in entry.lower() for entry in data_acc):
            print(f"Akun [{username}] Sudah terdaftar")
            break

        with open("acc.txt" , "a")as file:
            file.write(f"username = {username}\n")
            file.write(f"password = {password}\n\n")

        print(f"Akun Dengan Nama {username} telah didaftarkan")
        break

def login():
    i=int(0)
    while True :
        print("========= Login ==========")
        username = str(input("Nama Akun = "))
        password = str(input("Password Akun = "))

        login_log = False
        
        for entry in data_acc:
            if(f"username = {username}" in entry and f"password = {password}" in entry):
                login_log = True
                break
        if login_log == True :
            print(f"hallow {username} W K B")
        else:
            i= i+1

        if i == 1 :
            print("Username atau Password salah")
        elif i == 2:
            print("CODINGAN ERROR")
        else:
            print("JAN MAKSA BLOK")
            break
