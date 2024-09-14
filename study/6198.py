import sys

def solve(data:list[int])->int:
    answer = 0
    stack = []
    for h in data:
        while stack and stack[-1] <= h:
            stack.pop()
        answer += len(stack)
        stack.append(h)
    return answer

n = int(sys.stdin.readline())
data = [int(sys.stdin.readline()) for _ in range(n)]
print(solve(data))
