class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public
        #self._balance=balance #(protected)
        self.__balance=balance #private-data mangling(forceful print)

    def get_balnce(self): #getter
        return self.__balance
    
    def set_balance(self,newbalance): #setter
        self.__balance=newbalance
        
acc1=BankAccount("Rahul Kumar",100_000)
acc1.set_balance(200_000)
#print(acc1.name,acc1._balance)
print(acc1.name,acc1.BankAccount__balance)

