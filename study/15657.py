import sys

def solve(m:int,data:list[int])->list[list[int]]:
    answer = []
    def _dfs(n:int,i:int,arr:list[int]):
        if n == m:
            answer.append(arr)
            return
        for k in range(i,len(data)):
            _dfs(n+1,k,arr+[data[k]])
    data.sort()
    _dfs(0,0,[])
    return answer

n,m = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
answer = solve(m,data)
[print(*r) for r in answer]