# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:57:55 2023

@author: jtcle
"""

#터렛문제

import math

n = int(input())

for _ in range(n):
    x1,x2,y1,y2,r1,r2 = list(map(int, input().split()))
    
    터렛거리 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    # sqrt 제곱근 구하기
    
    if 터렛거리==0 and r1 == r2:
        # 두 터렛이 같은 위치, 같은 사거리, 무한대의 경우수
        print(-1)
    elif abs(r1-r2) == 터렛거리 or r1 + r2 == 터렛거리:
        # 터렛 사거리 원이 한 점에서 만남
        print(1)
    elif abs(r1-r2) <= 터렛거리 <= r1 + r2:
        # 터렛 사거리 두 점에서 만남
        print(2)
    else:
        print(0)