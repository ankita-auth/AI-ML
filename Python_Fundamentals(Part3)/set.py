s={1,2,2,3}
# print(s)  #* {1,2,3}

# print(type(s))   #* <class 'set'>

# print(len(s))    #* 3


# empty_set={}     #* Dictionay not a set, output->{}
# print(empty_set)

# empty_set=set()  #*output->set()
# print(empty_set)


#* Method
#*1
# s.add(5)
# print(s)

#*2
# s.remove(1)
# print(s)

#*3
# s.clear()
# print(s) #* output-> set()

#*4
# s.pop()
# print(s)


s1={1,2,3,4,5}
s2={4,5,8,9,10}
#*5
print(s1.union(s2))

#*6
print(s1.intersection(s2))




