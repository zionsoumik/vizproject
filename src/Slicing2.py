file=open("venice.txt")
import csv

import itertools
text=file.read()
with open("venice-named.txt") as f:
    text1=f.readlines()
names = [x.strip() for x in text1]
names_dict=[]
g={}
count=0
acts=text.split('\n\n')
for name in names:
    g={}
    #print(count)
    g["id"]=count
    g["label"]=name
    #print(g)
    names_dict.append(g)
    count=count+1
edges_dict=[]
ed={}
#print(names_dict)
l=list(itertools.combinations(range(len(names_dict)), 2))
for pair in l:
    ed={}
    ed["source"]=pair[0]
    ed["target"]=pair[1]
    ed["weight"]=0
    edges_dict.append(ed)
# for act in acts:
#     #print(act.lower())
#     if names_dict[edges_dict[7]]["label"] in act.lower() and names_dict[12]["label"] in  act.lower():
#         print("yes")
#print(edges_dict)
for pair in edges_dict:
    #print(pair)
    #print(pair[0])
    #print(pair[1])
    for act in acts:
        #print(names_dict[pair["source"]]["label"])
        #print(names_dict[pair["target"]]["label"])
        #print(act)
        #print(act.count(names_dict[pair[0]]["label"]))
        s1=act.lower().count(names_dict[pair["source"]]["label"])
        s2=act.lower().count(names_dict[pair["target"]]["label"])
        #print(s1,s2)
        #print(pair["weight"])
        #if names_dict[pair["source"]]["label"] in act.lower() and names_dict[pair["target"]]["label"] in act.lower():
            #print("yes")
        pair["weight"]=pair["weight"]+min(s1,s2)
final_edge=[]
for edge in edges_dict:
    #print(edge)
    if edge['weight']!=0:
        final_edge.append(edge)
print(final_edge)

keys = names_dict[0].keys()
with open('id_name_venice.csv', 'w',newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(names_dict)

keys = final_edge[0].keys()
with open('edges_venice.csv', 'w',newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(final_edge)
