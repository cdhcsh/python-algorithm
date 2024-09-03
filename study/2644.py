import sys

def solve(n:int,start:int,end:int,data:list[list[int]])->int:
    nodes = [[] for _ in range(n+1)]
    for s,e in data:
        nodes[s].append(e)
        nodes[e].append(s)

    visit = {start:0}
    queue = [start]
    while queue:
        k = queue.pop(0)
        v = visit[k] + 1
        for c in nodes[k]:
            if c == end:
                return v
            if c not in visit:
                visit[c] = v
                queue.append(c)
    return -1


n = int(sys.stdin.readline())
start,end = map(int,sys.stdin.readline().split())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]
print(solve(n,start,end,data))


