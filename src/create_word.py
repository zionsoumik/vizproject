#This code does the tf-idf generation of words for the relevant mddularity classes.
#It takes the modulairty class into account and generates the most relevant 10
#words for that class.

import csv
import json
from nltk import word_tokenize
from pprint import pprint
json_data=open("data_venice.json").read()
g=json.loads(json_data)
list=[]
character_list=[]
with open('venice-named.txt', newline='') as csvfile:
    k=csvfile.readlines()
for r in k:
    character_list.append(r.rstrip())
print("charactr:",type(character_list))
with open('venice_nodes.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list.append(row)
mod_list=[]
with open("venice.txt") as f:
    text1=f.read()
list_words=word_tokenize(text1.lower())
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
doclist=[]
# creates the individual documents according to modularity class
for mod in mod_list:
    ind=0
    str1=""
    for h in mod:
        for i in range (0,len(list_words)):
            k=word_tokenize(h)
            count=1
            if len(k)==1 and h==list_words[i]:
                num_index = 0
                while (count<6):
                    num_index=num_index+1
                    #print(type(list_words[i-count]))
                    if list_words[i-num_index] not in character_list:
                        str1=str1+ list_words[i-num_index]+" "
                        count=count+1
                num_index = 0
                while (count < 6):
                    num_index = num_index + 1
                    if list_words[i+num_index] not in character_list:
                        str1=str1+ list_words[i+num_index]+" "
                        count=count+1
            if len(k)!=1 and k[0]==list_words[i] and k[1]==list_words[i+1]:
                num_index = 0
                while (count<6):
                    num_index = num_index + 1
                    if list_words[i-num_index] not in character_list:
                        str1=str1+ list_words[i-num_index]+" "
                        count=count+1
                num_index = 0
                while (count < 6):
                    num_index = num_index + 1
                    if list_words[i+num_index+1] not in character_list:
                        str1=str1+ list_words[i+num_index+1]+" "
                        count=count+1
                # for j in range(i-5,i-1):
                #     print(list_words[j])
                #     str1=str1+ list_words[j]+" "
                # for j in range(i+2,i+6):
                #     print(list_words[j])
                #     str1=str1+ list_words[j]+" "
    doclist.append(str1)
# Source http://stevenloria.com/finding-important-words-in-a-document-using-tf-idf/
#creates the tfidf values
import math
from textblob import TextBlob as tb

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

print(doclist)
bloblist=[]
for doc in doclist:
    bloblist.append(tb(doc))

tfidf_words=[]

for i, blob in enumerate(bloblist):
    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    str2=""
    for word, score in sorted_words[:10]:
        str2=str2+word+"."
    tfidf_words.append(str2)
print(tfidf_words)

for k in list:
    k["top_words"]=tfidf_words[int(k["modularity_class"])]
print(list)

# with open('data_final.csv', 'w', newline='') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=list[0].keys())
#
#     writer.writeheader()
#     for row in list:
#         writer.writerow(row)

#generates the json files
for node in g["nodes"]:
    #node["attributes"]
    for i in range(0,len(tfidf_words)):
        if node["attributes"]["Modularity Class"]==str(i):
            node["attributes"]["top words"]=tfidf_words[i]
with open('data_final_venice.json', 'w') as outfile:
    json.dump(g, outfile)