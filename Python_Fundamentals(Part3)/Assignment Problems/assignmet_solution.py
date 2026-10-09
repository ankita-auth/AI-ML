
#* Q1
# str=input("Enter a string")
# str1=""
# for ch in range(len(str)-1,-1,-1):
#     str1+=str[ch]
# if(str1==str):
#     print("Palindrom")
# else:
#     print("Not Palindrom")

#                     OR

# str = input("Enter the String: ")
# str1 = str[::-1]
# if str1 == str:
#     print("Pallindrome")
# else:
#     print("Not Pallindrome")
 

#* Q2
# l=[25,14,4,60,50]
# s=0
# for i in l:
#     s+=i
# avg=s/len(l)
# print(avg)

#* Q3
# n1=int(input("Enter length of first list"))
# n2=int(input("Enter length of  second list"))
# list1=[]
# list2=[]
# for i in range(n1):
#     list1.append(int(input("Enter element of list1")))
# for j in range(n2):
#     list2.append(int(input("Enter element of list2")))
# list3=list1+list2
# list3.sort()
# print(list3)


#* Q4
# t=(2,4,9,8,15,0)
# le=[]
# lo=[]
# for i in t:
#     if(i%2==0):
#         le.append(i)
#     else:
#         lo.append(i)
# te=tuple(le)
# to=tuple(lo)
# print(te)
# print(to)

#* Q5
# d={}
# c=input("Enter A,B,C,D:\nA-Add a Student\nB-Update Marks\nC-Search for a Student\nD-Display all Students and Marks\n").upper()
# match c:
#     case "A":
#         n=input("Enter a student name:")
#         m=int(input("Enter Marks of this Student"))
#         d.update({n:m})
#     case "B":
#         n=input("Enter name of Student whose marks you want to update:")
#         m=int(input("Enter updated Marks of this Student"))

#         if n in d():
#             d[n]=m
#         else:
#             print("Name not present")
#     case "C":
#          n=input("Enter name of Student which is needed to be searched:")
#          if n in d():
#              print("student Found.")
#          else:
#              print("Student Not Found.")
#     case "D":
#         print(d)
#     case _:
#         print("Invalid character")

#* Q6
# dict={}
# words=["apple","banana","kiwi","cherry","mango"]
# for i in words:
#     #dict.update({i:len(i)})
#     dict[i]=len(i)
# print(dict)

#* Q7
# str=input("Enter a String")
# c=0
# for i in str:
#     if(i==" "):
#         c+=1
# print(c)

#* Q8
# list1 = []
# list2 = []
# a = int(input("Enter the length of list1: "))
# b = int(input("Enter the length of list2: "))
# for i in range(a):
#     list1.append(input("Enter the no in list1: "))
# for i in range(b):
#     list2.append(input("Enter the no in list2: "))j
# x = set(list1)
# y = set(list2)
# list3 = list(x.intersection(y))
# if len(list3) == 0:
#     print("No share Element")
# else:
#     print("Share element exist")
 
#* Q9
# list = []
# a = int(input("Enter the length  of list: "))
# for i in range(a):
#     list.append(input("Enter the no in list: "))
# seen=set()
# duplicate=set()
# for i in list:
#     if i in seen:
#         duplicate.add(i)
#     else:
#         seen.add(i)
# print(duplicate)

#* Q10
# str=input("Enter a String")
# s=set(str)
# l=len(s)
# print(s)
# print(l)




    
    

