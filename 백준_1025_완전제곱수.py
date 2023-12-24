# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:32:49 2023

@author: jtcle
"""


import math
import sys

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
    
# N by M 행렬 입력받기

answer = -1

for i in range(N):
    for j in range(M):
        for row in range(-N,N):
            for col in range(-M,M):
                S = ''
                x, y = i, j
                if x == 0 and y == 0:
                    continue
                while 0 <= N and 0 <= M:
                    S += str(arr[x][y])
                if int(math.sqrt(int(S)))**2 == int(S):
                    answer = max(int(S), answer)
                    
                x += row
                y += col
print(answer)
                
# 모든 행과 열을 판별하기 위한 4중 for문

    

from  math import sqrt


N,M=map(int,input().split())

A=[list(map(int,input()))for _ in range(N)]

answer=-1

for i in range(N):
    for j in range(M):
        for d1 in range(-N,N):
            for d2 in range(-M,M):
                num=''
                x,y=i,j
                while 0<=x<N and 0<=y<M:
                    num+=str(A[x][y])
                    if d1==0 and d2==0:
                        break
                    if int(sqrt(int(num)))**2==int(num):
                        answer=max(int(num),answer)

                    x+=d1
                    y+=d2

print(answer)