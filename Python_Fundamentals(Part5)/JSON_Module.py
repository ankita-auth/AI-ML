import json

# json_str = '{"name" : "Jibitesh","isTeacher" : true}'
#json_str = '{"name" : "Jibitesh","isTeacher" : null}'
#print(type(json_str))

#*json.loads()
#py_obj = json.loads(json_str)
#print(type(py_obj), py_obj)

#*O/P: 
# <class 'dict'> {'name': 'Jibitesh', 'isTeacher': True}
#<class 'dict'> {'name': 'Jibitesh', 'isTeacher': None}


#---------------------x-----------------------------------

#*json.dumps()
#py_obj = {
#    "name" : "jibitesh",
#    "isTeacher" : True
#}

#json_str=json.dumps(py_obj)
#print(type(json_str),json_str)

#* O/P:
# <class 'str'> {"name": "jibitesh", "isTeacher": true}

#---------------------x-----------------------------------
#*json.load()

# with open("data.json","r") as f:
#     py_obj=json.load(f)
#     print(type(py_obj))

#* Output=><class 'dict'>


#---------------------x-----------------------------------
#*json.dump()
d={
    "name":"Ankita",
    "subject":["ai-ml","math"],
    "is Student":True
}#this is python value
with open("data.json","w") as f:
    json.dump(d,f,indent=4,sort_keys=True) #* 1st parameter should be python obj then file
  



