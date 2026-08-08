with open("sample.txt","r") as f:
    c=0
    found=False
    data=f.readline()
    while(data!="\n"):
        c+=1
        if "Python" in data:
            print("Python word found.")
            print("Found in line:",c)
            found=True
            break
        data=f.readline()
    if(found==False):
        print("Not found")

#----------------------------X------------------------------------

# with open("sample.txt","r") as f:
#     data = list(f.readlines())
#     a = False
#     line = 0
#     for i in data:
#         if "\n" in i:
#             line+=1
#         if "Python" in i:
#            print("Exist")
#            print(f"Line: {line}")
#            a = True
#            break
 
#     if a == False:
#         print("Doesn't Exist")