import json
json_data=open("data.json").read()
print(json_data)
g=json.loads(json_data)
print(type(g))
print(type(g["nodes"]))
#print(json_data["nodes"])