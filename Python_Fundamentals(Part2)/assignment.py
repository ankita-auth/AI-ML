# #Q1
# salary=int(input("Enter your Salary:"))
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


#Q3
m=int(input("Enter a number: "))
s=""
while m!=0:
    s+=str(m%10)
    m//=10
for i in s:
    print(i)
