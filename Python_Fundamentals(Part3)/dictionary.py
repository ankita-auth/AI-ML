info={
    "name":"Ankita",
   "cgpa":9.2,
   "subjects":["maths","science"],
    3.14:"PI"
}

# print(type(info))
# print(info["name"])
# print(info[3.14])
# info["cgpa"]=9.6
# print(info)
#------------------------X--------------------------
#*Method
 
# *d.keys()
# print(info.keys())
# print(type(info.keys()))
# dict_keys=list(info.keys())
# print(dict_keys)

#*d.values()
# dict_values=list(info.values())
# print(dict_values)
# print(type(dict_values))

#*d.items()
# print(info.items())
# print(type(info.items()))
for key,values in info.items():
    print(key,values)

#*d.get(val)
#print(info["cgpa2"])
# print(info.get("cgpa2"))
# print("end of code")

#*d.update(new_item)
# info.update({
#     "city":"delhi"
# })
# print(info)



