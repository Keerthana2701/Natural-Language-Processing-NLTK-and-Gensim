# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 16:16:46 2020

@author: Vikee
"""


from pyphonetics import Soundex

soundex = Soundex()
a=soundex.phonetics('Allowed')
b=soundex.phonetics('Aloud')
c=soundex.sounds_like('Allowed', 'Aloud')