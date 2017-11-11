import string

__author__ = 'ebc'
#-*-coding:utf-8-*-

from nltk import stem,word_tokenize
from itertools import product
from string import punctuation

# hash table for words
def words2dict(filename,a_dict):
    thefile = open(filename, 'r')
    lines=thefile.readlines()
    for word in lines:
        word=word.strip().lower()
        a_dict[word]=a_dict.get(word,0)+1

    thefile.close()
    return a_dict

# Mike is connected to mark and daniel, n times
# {("daniel,mark"):1,}
def text2graph(filename,slice_len,graph_dict,words_hash):

    thefile=open(filename,'r')
    punctuation=list(string.punctuation)

    line=thefile.readline()
    word_slice=[]
    word_count=0
    total_count=0
    print "enter"
    while (line!=""):
        total_count+=1
        if (total_count%1000)==0:
            print total_count
        words=word_tokenize(line)
        for word in words:
            if word in punctuation:
                continue
            word_count +=1
            # lowercase the word
            word=word.lower()
            # remove affixes
            word=stem.WordNetLemmatizer().lemmatize(word)
            if (words_hash.get(word,None)!=None):
                word_slice.append(word)

            if word_count==slice_len:
                if len(word_slice)>1:
                    print word_slice
                    for r in product(word_slice, word_slice):
                        r=tuple(sorted(list(r)))
                        graph_dict[r]=graph_dict.setdefault(r,0)+1
                word_count=0
                word_slice=[]
        line = thefile.readline().decode('utf-8')

    thefile.close()

    return graph_dict


words_filename="emma_named.txt"
text_filename="emma.txt"
slice_len=10
graph_dict={}
words_hash={}
words_hash=words2dict(words_filename,words_hash)
print "done"
print words_hash.keys()[0]
print words_hash.keys()[10]
graph_dict=text2graph(text_filename,slice_len,graph_dict,words_hash)
print len(graph_dict)

