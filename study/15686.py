import sys


def solve(n: int, m: int, data: list[list[int]]) -> int:
    def _dfs(v:int,prev:int)->int:
        nonlocal m,n,answer
        if v == m:
            res = 0
            for h in houses:
                res += min(map(lambda i: abs(chickens[i][0]-h[0])+abs(chickens[i][1]-h[1]),selected))
            answer = min(answer,res)
            return
        nonlocal chickens,visited
        for i in range(prev,len(chickens)):
            if not visited[i]:
                visited[i] = True
                selected[v] = i
                _dfs(v+1,i)
                visited[i] = False

    answer = sys.maxsize
    chickens = []
    houses = []
    selected = [0] * m
    for i, l in enumerate(data):
        for j, num in enumerate(l):
            if num == 1:
                houses.append((i, j))
            elif num == 2:
                chickens.append((i, j))

    visited = [False] * len(chickens)
    _dfs(0,0)
    return answer

n, m = map(int,sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(int(n))]
print(solve(n,m,data))
