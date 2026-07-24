
#* Student Enrolments
#* Given a list of tuples with info(name, subject):
#*      ->list all unique course
#*      ->list students enrolled in English
#*      ->create dictionary(student,set of courses)

info = [
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
]
 
#*1
 
# unique_courses = set()
# for tup in info:
#     s.add(tup[1])
 
# print(unique_courses)
 
 
#*Note:  
#   for name,course in info:
#       print(name,course)
 
 
#*2
 
# for name,course in info:
#     if course == "English":
#           print(name)
 
 
#*3
 
dict = {}
for name,course in info:
    if dict.get(name) == None:
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
 
print(dict)
     