from nltk import corpus
import nltk
from nltk.corpus import wordnet
from nltk.corpus import words as wn
from nltk import word_tokenize
macbeth=[]
words=set()
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
import string
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
#s = "string. With. Punctuation?" # Sample string
#out = s.translate(string.maketrans("",""), string.punctuation)
file=open("venice.txt",'r')
text=file.read()
sentences=nltk.sent_tokenize(text)
print(sentences)
named=set()
for sent in sentences:
    if sent.isupper():
        named.add(sent)
    pos=nltk.pos_tag(word_tokenize(sent))
    #print(pos)
    for i in range(0,len(pos)):
        if pos[i][0].isupper() and pos[i+1][0].isupper() and len(pos[i][0])>1 and len(pos[i+1][0])>1 and pos[i+1][1]=="NNP":
            named.add(pos[i][0]+" "+pos[i+1][0])
            i=i+1
        elif pos[i][0].isupper() and pos[i][1]=="NNP" and len(pos[i][0])>1:
            named.add(pos[i][0])
        elif pos[i][0][0].isupper() and pos[i][1] == "NNP" and len(pos[i][0])>1:
            named.add(pos[i][0])
print(named)
print(len(named))
thefile=open("venice-named.txt",'w')
# with open('Macbeth.txt','r') as f:
#     for line in f:
#         for word in line.split():
#             out = word.translate(word.maketrans("", "" , string.punctuation))
#             if len(out)!=0 and (out not in stop):
#                 macbeth.append(out)
# print(macbeth)
# all_wwords=[]
# pos=nltk.pos_tag(macbeth)
# print(pos)
# for word in pos:
#     if word[1]=="NNP":
#         all_wwords.append(word[0])
# print(all_wwords)
# import string
# thefile=open("macbeth-named.txt",'w')
invalidChars = set(string.punctuation.replace("_", ""))
for word in named:
    #print(type(word))
    if not any(char in invalidChars for char in word):
        if word.isupper():
            words.add(word.lower())
        elif word[0].isupper():
            if not (wordnet_lemmatizer.lemmatize(word.lower()) in wn.words()):
                if len(wordnet.synsets(wordnet_lemmatizer.lemmatize(word.lower())))==0:
                    words.add(word.lower())
for item in list(words):
  thefile.write("%s\n" % item)

