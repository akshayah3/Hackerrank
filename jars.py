# -*- coding: utf-8 -*-
"""
Created on Sun May 11 20:05:52 2014

@author: akshay
"""

n,m=[int(x) for x in raw_input().split()]
sum1 = 0
for _ in range(m):
    a,b,k=[int(x) for x in raw_input().split() ]
    sum1+=(b-a+1)*k
print  (sum1/n)