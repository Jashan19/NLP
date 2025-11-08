import nltk
nltk.download('wordnet')
nltk.download('vader_lexicon')
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer
text="""Welcome to programming, from starting NLP to learning it is good thing. We must got to college. And, everday."""
demowords=["play","working","happiness","study","lonely"]
lemmatizer=WordNetLemmatizer()
stemmer=PorterStemmer()
for word in demowords:
    print(stemmer.stem(word), lemmatizer.lemmatize(word,"v"))
sia=SentimentIntensityAnalyzer()
print(sia.polarity_scores("Programming is fun"))