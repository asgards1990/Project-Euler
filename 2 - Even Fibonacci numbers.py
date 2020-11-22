# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:57:15 2020

@author: ys199
"""

#notice that odd+even = odd and odd + odd = even, even fibonacci numbers is 
#one every 3rd term starting at second term (so position 1)


fibb = 2
term_1 = 0
term_2 = 1
r = 0
while fibb < 4000000:
    r += fibb
    term_1 = fibb +term_2
    term_2 = fibb + term_1
    fibb = term_1 + term_2
    
print(r)