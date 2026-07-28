class Student:
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa
    def get_cgpa(self):
        return self.cgpa
stu1=Student("Rahul",9.0)
stu2=Student("Sita",8.4)
stu3=Student("Gita",9.2)

print(stu1.name)
print(stu2.name)
print(stu3.name)

print(stu1.get_cgpa())