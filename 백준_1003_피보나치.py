# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 15:07:07 2023

@author: jtcle
"""

#fibonacci(N)을 출력했을 때 0과 1이 몇 번 출력되는지
#다이나믹 프로그래밍?
#일반적인 재귀를 사용 시 컴퓨터의 비효율
#따라서 앞에서 계산된 값을 저장해서 사용하는 것.


def fib(N):
    zeros=[1,0,1] # 0이 출력되는 횟수 리스트
    ones=[0,1,1] # 1이 출력되는 횟수 리스트
    if N >= 3:
        for i in range(2,N):
            #2부터 N-1까지
            zeros.append(zeros[i-1] + zeros[i])
            #zeors 리스트 끝부분에 0의 출력횟수 추가됨
            ones.append(ones[i-1] + ones[i])
            #ones 리스트 끝부분에 1의 출력횟수 추가됨
    print(f"{zeros[N]} {ones[N]}")
    #zeros와 ones의 N번째 요소 출력
 
T = int(input())
for _ in range(T):
    N = int(input())
    fib(N)
    