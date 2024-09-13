import sys

def solve(n:int,data:list[int])->list[int]:
    stack = []
    answer = [-1] * n
    for i in range(n):
        while stack and data[stack[-1]] < data[i]:
            answer[stack.pop()] = data[i]
        stack.append(i)
    return answer


n = int(sys.stdin.readline())
stack = list(map(int,sys.stdin.readline().split()))
print(*solve(n,stack))