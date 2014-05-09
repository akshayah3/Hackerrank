# -*- coding: utf-8 -*-
"""
Created on Fri May  9 13:32:58 2014

@author: akshay
"""

t=input()
assert t<=100 and t>=1
a=set(raw_input())
for _ in range(t-1):
  b=set(raw_input())
  a = a.intersection(b)
print len(a)