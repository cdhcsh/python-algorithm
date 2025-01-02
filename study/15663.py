import sys

def solve(m:int,data:list[int])->list[list[int]]:
    answer = set()
    def _dfs(n:int,i:int,arr:list[int]):
        if n == m:
            answer.add(arr)
            return
        for k in range(i,len(data)):
            _dfs(n+1,k+1,arr+[data[k]])
    _dfs(0,0,[])
    return answer

n,m = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
answer = solve(m,data)
answer.sort()
[print(*r) for r in answer]