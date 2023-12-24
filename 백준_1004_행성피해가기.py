# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 16:01:12 2023

@author: jtcle
"""    

# T는 테스트 케이스의 개수
T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = list(map(int, input().split()))
    #출발점, 도착점 좌표
    n = int(input())
    #행성계 개수
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        d1 = float((((cx-x1)**2 + (cy-y1)**2)**(1/2)))
        d2 = float((((cx-x2)**2 + (cy-y2)**2)**(1/2)))
        #출발점과 도착점 모두 행성계 밖이라면?
        if d1 > r and d2 > r:
            count += 0
        #출발점은 행성계 안, 도착점은 행성계 밖이라면?
        elif d1 < r and d2 > r:
            count += 1
        #출발점은 행성계 밖, 도착점은 행성계 안이라면?
        elif d1 > r and d2 < r:
            count += 1
        #출발점과 도착점 모두 행성계 안이라면?
        else:
            count += 0
    print(count)


