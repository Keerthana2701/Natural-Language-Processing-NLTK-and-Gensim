# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 21:30:04 2020

@author: Vikee
"""


import re

string = "Hey how are you doing my o is 99988828282 and ID is 34343"


a=re.findall('\d+',string)

b= re.search(r"([a-zA-Z]+) (\d+)" , "I was born on May 27")
print("the search string is: % s" % (b.group(0))) 
print("the search string is: % s" % (b.group(1))) 
print("the search string is: % s" % (b.group(2))) 

patterns = ['doctor', 'teacher']
text = 'is she a doctor? the job of a doctor is really incredible'
for pattern in patterns:
    print('Looking for "%s" in "%s" ->' % (pattern, text), end=' ')
    if re.search(pattern, text):
        print('found a match!')
else:
    print('no match')
    
    
list = ['hey123', 'helokeerthu','heysaru3344sha','welcome']
for a in list:
    b=re.match("(h\w+)",a)
    if b:
        print(b.groups())
        
        
        
        
s = "she is the best student in the class"
s1="class"
s2= " school"
res=re.sub(s1,s2,s)

d=(re.split(r'\s','let us learn french'))