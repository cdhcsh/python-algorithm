import sys

def solve(n:int):
    dp = [0] * 31
    dp[2] = 3
    for i in range(4,n+1):
        if i % 2 == 0:
            dp[i] += dp[i-2] * dp[2]
            for j in range(i-4,-1,-2):
                dp[i] += dp[j] * 2
            dp[i] += 2

    return dp[n]


n = int(sys.stdin.readline())
print(solve(n))