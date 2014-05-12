# -*- coding: utf-8 -*-
"""
Created on Tue May 13 00:41:14 2014

@author: akshay
"""

def answer(n):
    x=0
    y=0
    while (n-5*x)%3 != 0 and y >= 0:
        x += 1
        y = (n-5*x)/3

    y = (n-5*x)/3
    if y < 0:
        return "-1"

    return "".join('5' for i in range(3*y)) + "".join('3' for j in range(5*x))