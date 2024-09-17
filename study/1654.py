import sys

def solve(n:int,data:list[int]):
    answer = 0
    left = 1
    right = max(data)
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for l in data:
            cnt += l // mid
        if cnt >= n:
            answer = max(mid, answer)
            left = mid + 1
        else:
            right = mid - 1
    return answer


k,n = map(int,sys.stdin.readline().split())
data = [int(sys.stdin.readline()) for _ in range(k)]
print(solve(n,data))