# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:42:19 2020

@author: Vikee
"""


# Frequency Distribution -NLTK


import nltk

files = nltk.corpus.gutenberg.fileids()

data = nltk.corpus.gutenberg.words("shakespeare-caesar.txt")

## how many times each word occurs

data_freqdist = nltk.FreqDist(data)

a=data_freqdist["The"]

# most commonly used 15 words

b=data_freqdist.most_common(15)


# words that were used only once 

c=data_freqdist.hapaxes()