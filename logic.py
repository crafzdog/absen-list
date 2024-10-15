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
        print(username,password)
        break

def login():
    i=int(0)
    data_acc = []
    with open("acc.txt","r") as file:
        data_acc = file.readlines()

    login_log = False

    while True :
        print("========= Login ==========")
        username = str(input("Nama Akun = "))
        password = str(input("Password Akun = "))
        
        for idx in range(0, len(data_acc),2):
            stored_user = data_acc[idx].strip().split(" = ")[1]
            stored_pass = data_acc[idx + 1].strip().split(" = ")[1]

            print(f"Stored user : {stored_user},Stored pass : {stored_pass}")

            if username == stored_user and password == stored_pass:
                login_log = True
                break
        
        if login_log == True:
            print(f"hello {username}, W K B")
            break
        else:
            i += 1

        if i == 1:
            print("Username atau Password salah")
        elif i == 2:
            print("CODINGAN ERROR")
        else:
            print("JAN MAKSA BLOK")
    return login_log

        # for entry in data_acc:
        #     if(f"username = {username}" in entry and f"password = {password}" in entry):
        #         login_log = True
        #         break
        # if login_log == True :
        #     print(f"hallow {username} W K B")
        # else:
        #     i= i+1

        # if i == 1 :
        #     a1 = f"username = {username} password {password}"
        #     print("Username atau Password salah")
        #     print(a1)
        # elif i == 2:
        #     print("CODINGAN ERROR")
        # else:
        #     print("JAN MAKSA BLOK")
        #     break
