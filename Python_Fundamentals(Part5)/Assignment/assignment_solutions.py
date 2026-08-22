
#* Q1->
# with open("names.txt","w") as f:
#     for i in range(5):
#         n=input("Enter name ")
#         f.write(n+ "\n")
# with open("names.txt","r") as f:
#     data=f.read
#     print(data)

#* Q2->
# with open("log.txt","a") as f:
#     f.write("Program run successfully")
# with open("log.txt","r") as f:
#     print(f.read())

#* Q3->
# l=[5,10,15,20,25]
# l=[i for i in l if (i>15) ]
# print(l)

#* Q4->
#* Created cities.json file
# import json
# d={
#     "Kolkata":100000,
#     "Odisha":20000,
#     "Bihar":300000000
# }
# with open("cities.json","w") as f:
#     json.dump(d,f,indent=4,sort_keys=True)

#* Load JSON and print each city and poopulation
# with open("cities.json","r") as f:
#     py_obj=json.load(f)
#     print(py_obj)
# city=input("Enter a city name:")
# population=int(input("Enter that city population: "))
# d.update({city:population})
# with open("cities.json","w") as f:
#     json.dump(d,f,indent=4,sort_keys=True)

#* Q5->
# try:
#     with open("data.txt","r") as f:
#         data=f.read()
        
# except Exception as e: 
#     print(e) 
#     print("File not found")
# else:
#     print(data)







    