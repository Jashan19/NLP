from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
docs=["the cast on the mat", " the dogs sat on floor","cats and dogs"]
tfidf=TfidfVectorizer().fit_transform(docs)
sim=cosine_similarity(tfidf)
print(sim)