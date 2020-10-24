# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 08:21:47 2020

@author: Vikee
"""


import nltk

sentence = "I like to eat more chocolates than Ramya"
token = nltk.word_tokenize(sentence)
token

a=nltk.pos_tag(token)


# We can get more details about any POS tag using help funciton of NLTK as follows.
nltk.help.upenn_tagset("PRP$")

nltk.help.upenn_tagset("NN")

nltk.help.upenn_tagset("NNP")