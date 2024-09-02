import sys

def solve(commands:list[int])->list[int]:
    answer = []
    for data in commands:
        l = len(data)
        dp = [[0] * l for _ in range(l)]
        sub = [0] * (l+1);
        sub[1] = data[0]
        for i in range(l-1):
            sub[i+2] = sub[i+1] + data[i+1]
            dp[i][i+1] = data[i] + data[i+1]
        for k in range(2,l):
            for i in range(l-k):
                dp[i][i+k] = min([dp[i][i+j]+dp[i+j+1][i+k] for j in range(0,k)]) + (sub[i+k+1]-sub[i])
        answer.append(dp[0][-1])
    return answer

commands = []
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline().strip())
    commands.append(list(map(int, sys.stdin.readline().split())))
print(*solve(commands),sep='\n')
