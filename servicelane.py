# -*- coding: utf-8 -*-
"""
Created on Fri May  9 13:18:21 2014

@author: akshay
"""

in1=map(int,raw_input().split())
N=in1[0]
T=in1[1]
a=map(int,raw_input().split())
for i in range(0,T):
    index=map(int,raw_input().split())
    print min(a[index[0]:index[1]+1])
