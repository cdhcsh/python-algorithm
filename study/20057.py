import sys


def solve(n: int, send: list[list[int]]) -> int:
    answer = 0
    def _add(x:int,y:int,amount:int):
        nonlocal answer
        if 0 <= x < n and 0 <= y < n:
            send[x][y] += amount
        else:
            answer += amount
    loc = (n // 2, n // 2)
    d = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    wind = [[([0,-2],5),
            ([-1,-1],10),([1,-1],10),
            ([-1,0],7),([1,0],7),
            ([-2,0],2),([2,0],2),
            ([-1,1],1),([1,1],1)],
            [([2,0],5),
             ([1,-1],10),([1,1],10),
             ([0,-1],7),([0,1],7),
             ([0,-2],2),([0,2],2),
             ([-1,-1],1),([-1,1],1)],
            [([0, 2], 5),
             ([-1, 1], 10), ([1, 1], 10),
             ([-1, 0], 7), ([1, 0], 7),
             ([-2, 0], 2), ([2, 0], 2),
             ([-1, -1], 1), ([1, -1], 1)],
            [([-2, 0], 5),
             ([-1, -1], 10), ([-1, 1], 10),
             ([0, -1], 7), ([0, 1], 7),
             ([0, -2], 2), ([0, 2], 2),
             ([1, -1], 1), ([1, 1], 1)],
            ]
    c = 1
    r = 0
    p = 0
    pd = 0
    while loc != (0,0):
        loc = (loc[0]+d[pd+p][0],loc[1]+d[pd+p][1])
        res = send[loc[0]][loc[1]]
        if res >= 10:
            for l,R in wind[pd+p]:
                s = send[loc[0]][loc[1]] * R // 100
                res -= s
                if s > 0:
                    _add(loc[0]+l[0],loc[1]+l[1],s)
        _add(loc[0]+d[pd+p][0],loc[1]+d[pd+p][1],res)
        send[loc[0]][loc[1]] = 0
        r += 1
        if r == c:
            if p == 1:
                c += 1
                p = 0
                pd = (pd + 2) % 4
            else:
                p = 1
            r = 0
    return answer
n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(solve(n, data))