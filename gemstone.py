# -*- coding: utf-8 -*-
"""
Created on Fri May  9 13:32:58 2014

@author: akshay
"""

t=input()
assert t<=100 and t>=1
c=[]
#a=set(raw_input())
for i in range(0,t):
  b=set(raw_input())
  c.append(b)

a = set(b[0]).intersection(b[1:t])
print a