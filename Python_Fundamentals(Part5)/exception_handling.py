try:
    x=int(input("Enter the number"))
    ans=10/x
# except ZeroDivisionError:
#     print("divide by zero not allowed")
except Exception as e: 
    print(e)           #* to print particular exception
else:
    print(f"ans:{ans}")
finally:
    print("Jibitesh")


