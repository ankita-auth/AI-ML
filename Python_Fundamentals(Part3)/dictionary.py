info={
    "name":"Ankita",
    "cgpa":9.2,
    "subjects":["maths","science"],
    3.14:"PI"
}
print(type(info))
print(info["name"])
print(info[3.14])

info["cgpa"]=9.6
print(info)

print(info.keys())

print(type(info.keys()))

dict_keys=list(info.keys())
print(dict_keys)

dict_values=list(info.values())
print(dict_values)
print(type(dict_values))