import csv
from pprint import pprint
#json_data=open("data.json").read()
#g=json.dumps(json_data)
list=[]
with open('data_macbeth.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list.append(row)
mod_list=[]
modularity_list=[set(),set(),set(),set(),set(),set(),set(),set()]
for r in list:
    #print(r["modularity_class"])
    #print(r["label"])
    modularity_list[int(r["modularity_class"])].add(r["label"])

    #print(r)
#print(modularity_list)
for el in modularity_list:
    if len(el)!=0:
        #print([x for x in el])
        mod_list.append([x for x in el])
#modularity_list1=modularity_list[:modularity_list.index(0)]
print(mod_list)
