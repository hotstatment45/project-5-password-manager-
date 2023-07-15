print("====Welcom to password_store====")
print("what is the master password? ")
def view():
    with open('password.txt','r') as f:
        for line in f.readline():
            data = line.rstrip()
            user, passw=data.split("|")
            print(f"User:{user}, Password {passw}")


def add():
    name=input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt','a') as f:
        f.write(name + "|" + pwd  +"\n")



while True:
     mode = input("Would you like to add a new password or view exiting ones {view/add}? ").lower()
     if mode =="q":
         quit()
     if mode == "view":
         view()

     elif mode == "add":
         add()

     else:
         print("Invalid ")
