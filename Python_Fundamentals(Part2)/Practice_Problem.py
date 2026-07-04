#Set1
# #Q1
# n=int(input("Enter a number"))
# res="Multiple of 5" if (n%5==0) else "Not a multiple of 5"
# print(res)

# #Q2
# m=int(input("Enter a number"))
# ans="Even" if (m%2==0) else "Odd"
# print(ans)

#------------------------------------X--------------------------
# #set2
# #Q1
# a=int(input("Enter a number:"))
# i=1
# while i<=10:
#     print(a," X ",i," = ",(a*i))
#     i+=1

# #Q2
# j=0
# while j<=10:
#     j+=1
#     if j%2==0:
#         continue
#     print(j)
   

# #Q3
# word=input("Enter a word")
# c=0
# for i in word:
#     if i in "aeiouAEIOU":
#         c+=1
# print("Count of Vowels in ",word," is ",c)



# #Q4
# b=int(input("Enter a number:"))
# s=0
# for i in range(1,b+1):
#     s+=i
# print("Sum=",s)

#------------------------------------X--------------------------

#set3
#Q1
def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
c=int(input("Enter a number:"))
factorial=fact(c)
print(factorial)

#Q2
#status=lambda a,b,c:max(a,b,c)

def large(a,b,c):
    if (a>=b) and (a>=c):
        return a
    elif (b>=c):
        return b
    else:
        return c
a1= int(input("Enter a number:"))
b1=int(input("Enter a number:"))
c1=int(input("Enter a number:"))
print("Largest=",large(a1,b1,c1))
