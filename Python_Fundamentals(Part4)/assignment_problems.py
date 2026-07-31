
#* Q1
class BankAccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance-=amount
        else:
            print("Low Balance")
    def check_balance(self):
        print(f"Balance={self.balance}")
b1=BankAccount(9652,"ankita",1000000000)
b1.deposit(20000)
b1.withdraw(10000)
b1.check_balance()

    
        

