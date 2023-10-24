users = {"adam":"1234", "Admin":"Admin"}
username = input("Please Type Your Username: ").lower()
password = input("Please Type Your password: ").lower()

if username in users and users[username] == password:
        print("Login successful")

else:
    print ("username or password incorect please try again")
    exit()