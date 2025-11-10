from sklearn.feature_extraction.text import CountVectorizer
docs=["the cast on the mat", " the dogs sat on floor","cats and dogs"]
vec= CountVectorizer()
X=vec.fit_transform(docs)
print(X.toarray())
print(vec.get_feature_names_out())