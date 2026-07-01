username=input("Enter username:")
password=input("Enter Password")
if (username=="admin" and password=="pass"):
    print("success")
else:
    if(username!="admin"):
        print("Wrong username")
    else:
        print("Wrong Password")
        