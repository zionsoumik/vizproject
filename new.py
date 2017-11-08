from nltk import corpus
from nltk.corpus import words as wn
words=set()
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
emma=corpus.gutenberg.words('melville-moby_dick.txt')
import string
thefile=open("melville-moby_dick_named.txt",'w')
invalidChars = set(string.punctuation.replace("_", ""))
for word in emma:
    print(word)
    if not any(char in invalidChars for char in word):
        if word[0].isupper():
            if not (wordnet_lemmatizer.lemmatize(word.lower()) in wn.words()):
                words.add(word)
for item in list(words):
  thefile.write("%s\n" % item)