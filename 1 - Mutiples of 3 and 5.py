# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:36:50 2020

@author: ys199
"""

print('enter the upper bound, inclusive, under which you want multiples of 3s and 5s added')
n = int(input())-1
r = 0
it = 0
rg = n//3

for k in range(rg):
    it += 3
    r += it


it = 0
rg = n//5
print(rg)
for k in range(rg):
    it += 5
    r += it


it = 0
rg = n//15
for k in range(rg):
    it += 15
    r -= it
    
    
print(r)