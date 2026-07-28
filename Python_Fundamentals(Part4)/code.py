class Student:
    subject="Python"
    college="ABC"
    year="4th year"
stu1=Student()
stu2=Student()
print(stu1) #output-<__main__.Student object at 0x000001E418078590>
print(stu2) #output-<__main__.Student object at 0x00000276BECA8550>

print(stu1.subject, stu1.college, stu1.year) #output-Python ABC 4th year
