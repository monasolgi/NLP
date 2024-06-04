import nltk
#nltk.download()
#nltk.download('punkt')
from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
text = ("This is a long text containing various words and sentences"
        ". It discusses different topics and provides examples.")

tokens=word_tokenize(text)
tags=pos_tag(tokens)

print(tags)