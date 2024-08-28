# 7 . . . . . . .         7 . . . . . . .
# 6 . . . . . . C         6 . . . . . /-C
# 5 . . . . . . *         5 . . . . . | *
# 4 * * * * * . *         4 * * * * * | *
# 3 . . . . * . .         3 . . . . * | .
# 2 . . . . * . .         2 . . . . * | .
# 1 . C . . * . .         1 . C . . * | .
# 0 . . . . . . .         0 . \-------/ .
#   0 1 2 3 4 5 6           0 1 2 3 4 5 6

import sys


def solve(w: int, h: int, data: list[list[int]]) -> int:
    start = ()
    end = ()
    for i in range(h):
        for j in range(w):
            if data[i][j] == 'C':
                if start == end:
                    start = (i, j)
                else:
                    end = (i, j)
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    visit = [[[100000] * 4 for __ in range(w)] for _ in range(h)]
    prev_directions = [[-5] * w for _ in range(h)]
    q = []
    q.insert(0, start)
    visit[start[0]][start[1]] = [0,0,0,0]
    while q:
        x, y = q.pop(0)
        for pd in range(4):
            for i,d in enumerate(directions):
                if abs(pd-i) == 2:
                    continue
                tx,ty = x + d[0], y + d[1]
                if not (0 <= tx < h and 0 <= ty < w) or data[tx][ty] == '*':
                    continue
                if pd < 0:
                    v = -1
                else:
                    v = visit[x][y][pd]
                if pd != i:
                    v += 1
                if visit[tx][ty][i] > v:
                    visit[tx][ty][i] = v
                    q.insert(0, (tx,ty))
                    prev_directions[tx][ty] = i
    for i in range(h):
        for j in range(w):
            m = min(visit[i][j])
            if m == 100000:
                m = '*'
            print(m,end='')
        print()
    return min(visit[end[0]][end[1]])

w,h = map(int,sys.stdin.readline().split())
data = [sys.stdin.readline() for _ in range(h)]
print(solve(w,h,data))