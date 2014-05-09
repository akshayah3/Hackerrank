# -*- coding: utf-8 -*-
"""
Created on Fri May  9 16:17:17 2014

@author: akshay
"""

T = int(raw_input())
for i in range (0,T):
    A,B,C1 = [int(x) for x in raw_input().split(' ')]
    
    answer = 0
    answer += (A//B)
    Wrappers = answer

    while Wrappers/C1:  
        Chocolates = Wrappers/C1  
        Wrappers = Wrappers%C1 + Chocolates  
        answer += Chocolates
    
    print answer