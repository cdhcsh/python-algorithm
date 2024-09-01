import sys

def solve(data:list[list:int])->int:
    dp = [[0]*len(data) for _ in range(len(data))]
    dp[0][0] = 1
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if i == j == len(dp)-1:
                break
            jump = data[i][j]
            if i + jump < len(dp):
                dp[i+jump][j] += dp[i][j]
            if j + jump < len(dp):
                dp[i][j+jump] += dp[i][j]

    return dp[-1][-1]


n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(solve(data))