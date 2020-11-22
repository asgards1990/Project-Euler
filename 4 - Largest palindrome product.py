# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:06:23 2020

@author: ys199
"""

def isPalindrome (n):
    x = n
    rev = 0
    while (x>0) :
        rev =rev*10 + x%10
        x //= 10
    if rev == n :
        return True
    else :
        return False
    
#print(isPalindrome (9009))
r = 0
for i in range(100,1000):
    for j in range(i,1000):
        product = i *j
        if isPalindrome(product):
            r = max(r, product)
            
print(r)