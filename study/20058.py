import sys

sys.setrecursionlimit(10**8)

def solve(n:int,ices:list[list[int]],q:list[int])->list[int]:
    d = [[0,1],[1,0],[0,-1],[-1,0]]
    def _locate(start:(int,int),l:int):
        tmp = [[0]*l for _ in range(l)]
        for i in range(l):
            for j in range(l):
                tmp[j][l-1-i] = ices[start[0]+i][start[1]+j]
        for i in range(l):
            for j in range(l):
                ices[start[0]+i][start[1]+j] = tmp[i][j]
    def _dfs(visit:set[(int,int)],start:(int,int))->int:
        res = 1
        for x,y in d:
            tx,ty = start[0]+x,start[1]+y
            if 0 <= tx < n and 0 <= ty < n and ices[tx][ty] > 0 and (tx,ty) not in visit:
                visit.add((tx,ty))
                res += _dfs(visit,(tx,ty))
        return res
    answer = [sum([sum(d) for d in ices]),0]
    for L in q:
        l = 2**L
        tmp = [[0]*n for _ in range(n)]
        if l > 1:
            for i in range(0,n,l):
                for j in range(0,n,l):
                    _locate((i,j),l)
        for i in range(0,n):
            for j in range(0,n):
                if ices[i][j] == 0:
                    continue
                for k in range(2):
                    tx,ty = i+d[k][0],j+d[k][1]
                    if 0 <= tx < n and 0 <= ty < n and ices[tx][ty] > 0:
                        tmp[i][j] += 1
                        tmp[tx][ty] += 1
        for i in range(n):
            for j in range(n):
                if tmp[i][j] < 3 and ices[i][j] > 0:
                    ices[i][j] -= 1
                    answer[0] -= 1
    visit = set()
    for i in range(n):
        for j in range(n):
            if ices[i][j] > 0:
                visit.add((i,j))
                answer[1] = max(answer[1],_dfs(visit,(i,j)))


    return answer


n,__ = map(int,sys.stdin.readline().split())
n = 2**n
data = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
q = list(map(int,sys.stdin.readline().split()))
print(*solve(n,data,q),sep='\n')




