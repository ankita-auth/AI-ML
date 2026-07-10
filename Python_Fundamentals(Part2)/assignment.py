# #Q1
# salary=float(input("Enter your Salary:"))
# if salary<30000:
#     tax=0.05*salary
# elif salary<=70000:
#     tax=0.15*salary
# else:
#     tax=0.25*salary
# print("Final Tax rate=",tax)


# #Q2
# def even(a,b):
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i)

# a=int(input("Enter a: "))
# b=int(input("Enter b:"))
# even(a,b)


##Q3
# m=int(input("Enter a number: "))
# def fun(m):
#     s=""
#     while m!=0:
#         s+=str(m%10)
#         m//=10
#     for i in range(len(s)-1,-1,-1):
#         print(s[i]) 
# fun(m)

#Q4
# def count(n):
#     c=0
#     while(n!=0):
#         c=c+1
#         n//=10
#     return c
# n=int(input("Enter n:"))
# print(count(n))

# ##Q5
# def sum(n):
#     s=0
#     while(n!=0):
#         s+=(n%10)
#         n//=10
#     return s
# n=int(input("Enter n:"))
# print(sum(n))

# #Q6
# for i in range(15,101,15):
#     print(i)

##Q7
# while( True):
#     n=input("Enter")
#     if(int(n)>0):
#         print("Positive")
#     elif(int(n)<0):
#         print("Negative")
#     elif(n=="Quit"):
#         break
#     else:
#         print("Wrong Input")

##Q8

# def calculator(a,b,operation):
#     match operation:
#         case '+':
#             return a+b
#         case '-':
#             return a-b
#         case '*':
#             return a*b
#         case '/':
#             return a/b
#         case _:
#             return "Invalid value"
 

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# operator=input("Enter operator:")
# print(calculator(a,b,operator))

# ##Q9
# def prime(n):
#     if(n<2):
#         return False
#     if(n==2):
#         return True
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True
# n=int(input("Enter n:"))
# print(prime(n))

##Q10
# n=int(input("Enter a number"))
# s=10
# if(s>n):
#     print("Too Low")
# elif(s==n):
#     print("Correct")
# else:
#     print("Too High")