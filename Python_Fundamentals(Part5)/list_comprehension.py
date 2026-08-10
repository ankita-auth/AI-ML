
#* Without List Comprehension
# square=[]
# for i in range(6):
#     square.append(i*i)
# print(square)

#* Using List Comprehension
square=[i*i for i in range(6)]
print(square)

#* Including Condition
square=[i*i for i in range(6) if i%2!=0]
print(square)

#* Q->Replace negative numbers with 0 using list comprehension=>[-2,-4,3,5,2,-1]
nums=[-2,-4,3,5,2,-1]
nums=[i if i>0 else 0 for i in nums ]
print(nums)

#* Q->words=["hello","python","apna"] Convert to Upper case
words=["hello","python","apna"]
words=[val.upper() for val in words]
print(words)