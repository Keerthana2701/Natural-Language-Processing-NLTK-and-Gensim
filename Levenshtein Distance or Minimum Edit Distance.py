# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:39:57 2020

@author: Vikee
"""

import numpy

def levenshteinDistanceDP(token1, token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1] # if 2 characters at end of 2 prefixesa re equal,then the distance is equal to the value in the top-left corner of the 2 x 2 matrix.
            else:   # If the two characters are not equal, then the distance in the current cell is equal to the minimum of the three existing values in the 2 x 2 matrix after adding a cost of 1
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    print(distances, len(token1), len(token2))
    return distances[len(token1)][len(token2)]

distance = levenshteinDistanceDP("Keerthana", "Keerthaanaa")