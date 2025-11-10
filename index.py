import nltk
import matplotlib.pyplot as plt
nltk.download('punkt_tab')
text="""Welcome to programming, from starting NLP to learning it is good thing. We must got to college. And, everday."""
from nltk.tokenize import word_tokenize
print(word_tokenize(text))
from nltk.tokenize import sent_tokenize
print(sent_tokenize(text))
from nltk.probability import FreqDist
fd=FreqDist(word_tokenize(text))
print(fd.most_common(4))
fd.plot(30, cumulative=False)
plt.show()
