
# This is a demo file
# to store some words
# for the Python activity
# that is to be solved by us.


#* Q->Find the word "Python" from "sample.txt" file.If found then print in which line found.

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

# data=True
# line=1
# with open("sample.txt","r") as f:
#     while data:
#         data=f.readline()

#         if("Python" in data):
#             print(f"word found at line {line}")
#             break
#         print(data)
#         line+=1