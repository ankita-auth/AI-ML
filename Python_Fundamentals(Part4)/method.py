class Laptop:
    storage_type="ssd"
    def __init__(self,RAM,storage):
        self.RAM=RAM
        self.storage=storage
    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

    @classmethod
    def get_storage_type(cls):
        print(f"storage type={cls.storage_type}")
    @staticmethod
    def calc_discount(price,discount):
        final_price=price-(discount*price/100)
        print(f"discounted price={final_price}")
l1=Laptop("16gb","512gb")
l2=Laptop("16gb","256gb")

l1.get_info()
Laptop.get_storage_type()
l1.get_storage_type()

l1.calc_discount(40_000,10)