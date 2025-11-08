import nltk
nltk.download('stopwords')
text="""Welcome to programming, from starting NLP to learning it is good thing. We must got to college. And, everday."""
demowords=["play","working","happiness","study"]
from nltk.corpus import stopwords
stop_words=stopwords.words('english')
#print(stop_words)
from nltk.tokenize import word_tokenize, sent_tokenize
words=word_tokenize(text)
#print(words)
tokenize_words_without_stopwords=[]
for word in words:
    if word not in stop_words:
        tokenize_words_without_stopwords.append(word)
print(tokenize_words_without_stopwords)
print(set(words)-set(tokenize_words_without_stopwords))