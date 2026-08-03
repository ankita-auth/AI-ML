#AVAILABLE
# #* Q1
# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_number=account_number
#         self.owner_name=owner_name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#     def withdraw(self,amount):
#         if(amount<=self.balance):
#             self.balance-=amount
#         else:
#             print("Low Balance")
#     def check_balance(self):
#         print(f"Balance={self.balance}")
# b1=BankAccount(9652,"ankita",1000000000)
# b1.deposit(20000)
# b1.withdraw(10000)
# b1.check_balance()


# #* Q2
# class Book:
#     def __init__(self,title,author,list_of_reviews=None):
#         self.title=title
#         self.author=author
#         self.list_of_reviews=list_of_reviews
#     def add_review(self,review):
#         self.list_of_reviews.append(review)
#     def count_review(self):
#         return len(self.list_of_reviews)
#     def display_all_review(self):
#         print(self.list_of_reviews)
# b1=Book("BTS_TOUR","Ankita",["awesome","fabulous","Outstanding","Deserving"])
# b1.add_review("Can't say more")
# b1.count_review()
# b1.display_all_review()


#* Q3
# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.__name = name
#         self.__roll_no = roll_no
#         self.__marks = marks
 
#     def getter(self):
#         return self.__name,self.__roll_no,self.__marks
 
#     def setter(self,name,roll_no,marks):
#         if marks < 0:
#             print("marks can't be -ve")
#             return
#         elif name == "":
#             print("name can't be empty")
#             return
           
#         elif not(roll_no >=1 and roll_no<=100):
#             print("roll number has to be between 1 & 100")
#             return
 
#         self.__marks = marks
#         self.__name = name
#         self.__roll_no = roll_no
 
# s1 = Student("Jibitesh",33,95)
# s1.setter("ankita",21,-2)
# print(s1.getter())


#* Q4
# class Shape:
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
        
#     def area(self):
#         return self.radius*self.radius*3.14
# class Rectangle(Shape):
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#     def area(self):
#         return self.breadth*self.length
# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height
#     def area(self):
#         return 0.5*self.base*self.height
# c=Circle(45)
# r=Rectangle(2,4)
# t=Triangle(41,22)
# print(c.area())
# print(r.area())
# print(t.area())


#* Q5
# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
    
# class Car(Vehicle):
#     def __init__(self,brand,model,seats):
#         super().__init__(brand,model)
#         self.seats=seats
#     def __str__(self):
#             return f"Car Brand: {self.brand},Model: {self.model},Seats: {self.seats}"

# class Bike(Vehicle):
#     def __init__(self,brand,model,engine):
#         super().__init__(brand,model)
#         self.engine=engine
#     def __str__(self):
#                 return f"Car Brand: {self.brand},Model: {self.model},Engine: {self.engine}"
# c=Car("Toyoto","Camry",5)
# print(c)
# b=Bike("Toyoto","Camry","xyz")
# print(b)

   
#* Q6
# from abc import ABC,abstractmethod
# class Employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     @abstractmethod
#     def calculate_salary(self):
#         pass
# class Intern(Employee):
#     def __init__(self,name,id,stipend):
#         super().__init__(name, id)
#         self.stipend=stipend
#     def calculate_salary(self):
#         return self.stipend
# class FullTimeEmployee(Employee):
#     def __init__(self,name,id,monthly_salary):
#         super().__init__(name, id)
#         self.monthly_salary=monthly_salary
#     def calculate_salary(self):
#         return self.monthly_salary*12
# class ContractEmployee(Employee):
#     def __init__(self,name,id,hourly_rate,hour_worked):
#         super().__init__(name, id)
#         self.hourly_rate=hourly_rate
#         self.hourly_worked=hour_worked
#     def calculate_salary(self):
#         return self.hourly_rate*self.hourly_worked
# f1=FullTimeEmployee("Ankita","2345",100000000000000000000)
# print(f1.calculate_salary())
      

#* Q7
# class Person:
#     def __init__(self,name,age=2,address="S. Korea"):
#            self.name=name
#            self.age=age
#            self.address=address
#*    Dunder Method
#     def __repr__(self):
#         return f"name= {self.name} age={self.age} address={self.address}"
# p=Person("Ankita",4)
# k=Person("Ankita",2,"hu")
# print(p)
# print(k)


#* Q8
# class Player():
#     Player_count=0
#     def __init__(self,name,level):
#         self.name=name
#         self.level=level
#         Player.Player_count=Player.Player_count+1
#     @classmethod
#     def NoOfPlayer(cls):
#         print(cls.Player_count)
# p1=Player("Ankita",100)
# p2=Player("Jibitesh",0)
# p3=Player("Lucky",-100)
# p1.NoOfPlayer()
    

#* Q9(MRO->Method Resolution Order)
# class Herbivore:
#     def __init__(self,plant):
#         self.plant=plant
#     def herbi(self):
#         print(self.plant)
# class Carnivore:
#     def __init__(self,prey):
#         self.prey=prey
#     def carni(self):
#         print(self.prey)
# class Omnivore:
#     def __init__(self,food):
#         self.food=food
#     def omni(self):
#         print(self.food)
# class Bear(Herbivore,Carnivore,Omnivore):
#     def __init__(self, plant,prey,food):
#         Herbivore.__init__(self,plant)
#         Carnivore.__init__(self,prey)
#         Omnivore.__init__(self,food)
#         print(Bear.__mro__)

# b=Bear("Carrot","Chicken","Maggi")
# b.omni()
# b.herbi()
# b.carni()


#* 10
class User:
    Users=0
    def __init__(self,user_name):
        self.user_name=user_name
        User.Users+=1
    def __repr__(self):
        return f"Username= {self.user_name}"

class Message:
    def __init__(self,text):
        self.text=text
    def showText(self):
        print(self.text)
    

class ChatRoom(User,Message):
    
    def __init__(self, user_name):
        User.__init__(self,user_name)
    def NoOfUsers(cls):
        return User.Users
    def printText(self,text):
        return Message.text
u1=User("Jibitesh")
u2=User("Lucky")
m=Message("Hehe")
c=ChatRoom("Jibitesh","Lucky")
print(c.NoOfUsers())
print(c.printText("Hehe"))




    



