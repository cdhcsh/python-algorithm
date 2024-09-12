import sys

def solve(m:int,n:int,data:list[int])->int:
    l = 1
    r = 10**9
    answer = 0
    while l <= r:
        mid = (l+r)//2
        c = 0
        for i in data:
            c += i//mid
        if c >= m:
            answer = max(answer,mid)
            l = mid + 1
        else:
            r = mid - 1
    return answer

m,n = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
print(solve(m,n,data))