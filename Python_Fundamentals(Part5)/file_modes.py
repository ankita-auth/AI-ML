#f=open("sample.txt","r")#file object
#* Read Operations
#data=f.read()
# data=f.readline() #reads single line+\n
# print(data)
# data=f.readline()
# print(data)
# print(type(data)) #<class 'str'>
#--------------------X-----------------------
#* Read Operations
#f=open("sample.txt","w")#File will totally change and get overwrite
# f.write("Jibitesh is my Bestfriend\nWe both study together")


#f.close() #we need to close it everytime we open a file
#--------------------X-----------------------
#* Default Read Mode
# f=open("sample.txt") #default-read file object
# print(f.read())
# f.close()
#--------------------X-----------------------
#* Append Mode
# f=open("sample.txt","a")
# f.write("\nNew text being appended")
# f.close()
#--------------------X-----------------------
# f=open("sample1.txt","a")
# f.write("Some random text")
# f.close()
#--------------------X-----------------------
# f=open("sample2.txt","w")
# f.write("Some random text 1")
# f.close()
#--------------------X-----------------------
#* Error
# f=open("smaple1.txt","x")
# f.write("xyz")