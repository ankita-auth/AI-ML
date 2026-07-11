# word='python'
# print(len(word))
# word1="I Love"
# print(word+word1)

# word="Python"
# print(word[0])

# word[2]='h'
# print(word[2])

#------------------------X------------------------
#Slicing
# word="I study from School"
# print(word[13:19])
# print(word[4:])
# print(word[:len(word)])
# print(word[:])
# word="python"
# print(word[-4:-2])


#------------------------X------------------------
#Formatting

# a=5
# b=6
# sum=a+b
# #normal formatting
# print("language is {}".format("python"))
# print("sum of {} and {} is {}".format(a,b,sum))

# #index based formatting
# print("sum of {1} and {0} is {2}".format(a,b,sum))

# #value based formatting
# print("{a}values of vars {a} & {b}".format(a=5, b=10))

#------------------------X------------------------
#f-string
a=5
b=10
print(f"avg of {a} & {b} is {(a+b)/2}")
