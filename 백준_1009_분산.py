# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 17:44:18 2023

@author: jtcle
"""

T = int(input())

for _ in range(T):
    a, b =map(int, input().split())
    
    av = a % 10
    
    if av == 0:
        print(10)
    elif av == 1 or av == 5 or av == 6:
        print(av)
    elif av == 4 or a ==9:
        if b % 2 == 0:
            print(av**2%10)
        elif b % 2== 1:
            print(av)
    else:
        bv = b % 4
        if bv == 0:
            print(av**4%10)
        else:
            print(av**bv%10)