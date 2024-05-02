master_pwd = input("Type your master password: ")


def password_mgr():
    option = input("Do you want to add a new password or view the existing ones? (add/view)")

    def add_pass():
        user_name = input("type the username ")
        password = input("type the password ")

        with open("passwords.txt", "a") as f:
            f.write(user_name + "|" + password + "\n")

    def view_pass():
        with open("passwords.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                usr, passw = data.split("|")
                print("Username :", usr, "Password :", passw)
        
    if(option == "add"):
        add_pass()
    elif(option == "view"):
        view_pass()
    else:
        print("Invalid option")

if(master_pwd == "qwerty"):
    password_mgr()
else:
    print("Wrong Password!, quitting....")