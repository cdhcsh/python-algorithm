import sys

def solve(data:list[str])->int:
    def _check(num:int)->bool:
            return num ** 0.5 % 1 == 0
    n = len(data)
    m = len(data[0])
    res = -1
    for i in range(n):
        for j in range(m):
            for dx in range(-n,n):
                for dy in range(-m,m):
                    if dx == 0 and dy == 0:
                        continue
                    s = ''
                    x,y = i,j
                    while 0 <= x < n and 0 <= y < m:
                        s += data[x][y]
                        if _check(int(s)):
                            res = max(res,int(s))
                        x += dx
                        y += dy
    return res


if __name__ == '__main__':
    n,m = map(int,sys.stdin.readline().split())
    data = [sys.stdin.readline().strip() for _ in range(n)]
    print(solve(data))





