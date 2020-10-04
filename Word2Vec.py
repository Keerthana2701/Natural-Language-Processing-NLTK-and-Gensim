# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 15:13:37 2020

@author: Vikee
"""


import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import re

paragraph = """ The ambition of     the greatest man of our generation has been to wipe every tear     from every eye (200). That may be beyond us, but as long as there are tears and suffering, so long our work will not be over.

And so we have to labour and to work, and work hard, to give reality to our dreams to make India great by 2000. Those dreams are for India, but they are also for the world, for all the nations and peoples are too closely knit together today for anyone of them to imagine that it can live apart.

Peace has been said to be indivisible; so is freedom, so is prosperity now, and so also is disaster in this one world that can no longer be split into isolated fragments."""

# Preprocessing the data
text = re.sub(r'\[[0-9]*\]',' ',paragraph)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)


sentences = nltk.sent_tokenize(text)

words = [nltk.word_tokenize(sentence) for sentence in sentences]

# remove stop words from this

for i in range(len(words)):
    words[i] = [word for word in words[i] if word not in stopwords.words('english')]
    
    
   # Training the Word2Vec model

model = Word2Vec(words, min_count=1)



words1 = model.wv.vocab

# Finding Word Vectors  - vector of that particular word 
vector = model.wv['dreams']   # gives vector of 100 dimensions

# Most similar words to work
similar = model.wv.most_similar('work')


