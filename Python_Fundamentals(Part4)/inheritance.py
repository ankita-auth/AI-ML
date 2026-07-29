# class Employee:
#     start_time="10am"  #it can be made protected but not private
#     end_time="6pm"
#     def change_time(self,new_end_time):
#         self.end_time=new_end_time

# class Teacher(Employee):
#     def __init__(self, subject):
#         self.subject=subject

# class AdminStaff(Employee):
#     def __init__(self,role):
#         self.role=role

# t1=Teacher("Math")
# t1.change_time("5pm")
# print(t1.subject,t1.start_time,t1.end_time)

# staff1=AdminStaff("Manager")
# print(staff1.role)

#------------------------------------X---------------------------------------
#* Multi Level Inheritance
class Employee:
    start_time="10am"  
    end_time="6pm"

class AdminStaff(Employee):
    def __init__(self,role):
        self.role=role

class Accountant(AdminStaff):
    def __init__(self, salary,role):
        super().__init__(role)
        self.salary=salary

acc1=Accountant(25_000,"CA")

print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)

#-----------------------------X----------------------------------------
#* Multiple Inheritance
class Teacher:
    def __init__(self,salary):
        self.salary=salary
class Student:
    def __init__(self,gpa):
        self.gpa=gpa
class TA(Teacher,Student):
    def __init__(self, gpa,salary,name):
        super().__init__(salary)     #called attribute using super(no self needed)
        Student.__init__(self,gpa)   #called attribute using Class Name(self needed)
        self.name=name



