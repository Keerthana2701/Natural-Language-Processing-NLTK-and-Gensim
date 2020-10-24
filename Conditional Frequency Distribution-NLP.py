# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:56:30 2020

@author: Vikee
"""

# frequency distribution -count  for single variable 
# calculate count for multiple variables

import nltk
from nltk.probability import ConditionalFreqDist
names =[("group A","Keer"),("group A","vig"),("group A","sar"),("group B","sha"),("group B","pun"),("group B","pun")]
names

# freq distibution

namefreq=nltk.FreqDist(names)

# conditional freq dis

namecfreq=nltk.ConditionalFreqDist(names)


cfdist = ConditionalFreqDist() 

# Of words starting with 'a', how many are 3 characters long?

for word in 'apple and arm'.split():
    cfdist['a'].freq(3)