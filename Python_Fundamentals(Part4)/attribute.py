class Student:
    college_name="ABC college" #class attribute
    PI=3.1
    def __init__(self,name,gpa):
        self.name=name #instance attribute
        self.gpa=gpa
        self.PI=3.14
stu1=Student("Rahul",9.2)

print(stu1.name)
print(Student.college_name) #can be invoked both from class and object name
print(stu1.college_name)
print(stu1.PI)  #instance attribute value will be printed
print(Student.PI)  #class attribute value will be printed