username = "admin"
password = "admin"

name = "Sumit"
if 3 > 3:
    print("Yes it is")
else:
    print("No it is")

login_username = input("Enter Username :  ")
login_password = input("Enter Password : ")

if login_username == username:
    if login_password == password:
        print("Welcome")
    else:
        print("Incorrect Password")
else:
    print("Invalid username")

if login_username == username and login_password == password:
    print("Welcome")
else:
    print("Invalid Credentials")


if login_username == "" or login_password == "":
    print("Please enter all fieilds")

if (not 5 > 3):
    print("Yes")
else:
    print("No")

age = int(input("Age : "))

if age >= 18 and age <= 65:
    print("You can drive")
elif name == "Sumit":
    print("Sumit can drive")
else:
    print("You can't")