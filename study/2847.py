import sys

def solve(data:list[int])->int:
    answer = 0
    m = data[-1]
    for i in data[::-1]:
        if i < m:
            m = i
        else:
            print(i,i-m)
            answer += i - m
        m -= 1
    return answer

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
print(solve(data))