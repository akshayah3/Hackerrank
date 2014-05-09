# -*- coding: utf-8 -*-
"""
Created on Fri May  9 15:30:42 2014

@author: akshay
"""

a = int(raw_input())
for i in range(0,a):
    b = int(raw_input())
    if b%2==0:
        print b**2/4
    else:
        print (b**2 -1)/4
