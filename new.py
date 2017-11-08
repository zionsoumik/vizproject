from nltk import corpus
from nltk.corpus import words as wn
words=set()
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
emma=corpus.gutenberg.words('carroll-alice.txt')
import string
thefile=open("char6.txt",'w')
invalidChars = set(string.punctuation.replace("_", ""))
for word in emma:
    print(word)
    if not any(char in invalidChars for char in word):
        if word[0].isupper():
            if not (wordnet_lemmatizer.lemmatize(word.lower()) in wn.words()):
                words.add(word)
for item in list(words):
  thefile.write("%s\n" % item)