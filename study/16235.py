import sys
import heapq
from heapq import heappop, heappush
from collections import deque


def solve(n:int,m:int,k:int,A:list[list[int]],trees:list[list[int]])->int:

    ground =  [[deque() for _ in range(n)] for __ in range(n)]
    old =  [[0] * n for _ in range(n)]
    count = len(trees)
    foods = [[5] * n for _ in range(n)]

    def _spring_summer():
        nonlocal count
        for i in range(n):
            for j in range(n):
                tmp = deque()
                dead = 0
                while ground[i][j]:
                    tree = ground[i][j].popleft()
                    if tree <= foods[i][j]:
                        foods[i][j] -= tree
                        tree += 1
                        tmp.append(tree)
                        if tree % 5 == 0:
                            old[i][j]+=1
                    else:
                        dead += tree//2
                        count -= 1
                ground[i][j] = tmp
                foods[i][j] += dead

    def _increase(i:int,j:int,):
        nonlocal count
        for a in range(-1,2):
            for b in range(-1,2):
                if a == b == 0: continue
                x,y = i + a,j + b
                if 0 <= x < n and 0 <= y < n:
                    ground[x][y].appendleft(1)
                    count += 1

    def _fall_winter():
        for i in range(n):
            for j in range(n):
                [_increase(i,j) for _ in range(old[i][j])]
                old[i][j] = 0
                foods[i][j] += A[i][j]
    # ======================================================= #

    for i,j,y in trees:
        ground[i-1][j-1].append(y)

    for _ in range(k):
        _spring_summer()
        _fall_winter()

    return count


n,m,k = map(int,sys.stdin.readline().split())
A = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
trees = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
print(solve(n,m,k,A,trees))