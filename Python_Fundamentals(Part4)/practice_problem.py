
#* Product store
#Design & create an online store for Products (name, price).Track total products being created.Create a static method to calculate discount on each product based on a % parameter.

class Products:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Products.count+=1

    def get_info(self):
        print(f"price of {self.name} is Rs. {self.price}")

    @classmethod
    def total_products(cls):
        return cls.count
    
    @staticmethod
    def discount(price,dis):
        return dis*price/100
p1=Products("sampoo",100)
p2=Products("Ball",50)
print(Products.total_products())
print(p1.discount(p1.price,25))



    