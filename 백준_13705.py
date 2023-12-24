# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:07:12 2023

@author: jtcle
"""

import numpy as np

def sinf(x):
    return A*x + B*np.sin(x) - C 



# 이진탐색 알고리즘 사용
# 배열의 중간값을 target과 비교하는 방법

A, B, C = map(int, input().split())
l, r = 0, 10**6
x = (l+r)/2

# 절대 오차를 기준으로 반복
while (np.abs(r-1) >= 10**(-9)):
    if (sinf(x)>0):
        r = x
    else:
        l = x
        x = (l+r)/2
        
print(x)