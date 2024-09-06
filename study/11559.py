import sys


def solve(data: list[str]) -> int:
    N,M = 12,6
    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def _down(target:list(set[(int,int)])):
        nonlocal N, M
        for g in target:
            for x,y in g:
                data[x][y] = '.'
        for j in range(M):
            blank = []
            for i in range(N - 1, -1, -1):
                if data[i][j] == '.':
                    blank.append(i)
                else:
                    if blank:
                        data[blank.pop(0)][j] = data[i][j]
                        data[i][j] = '.'
                        blank.append(i)

    def _scan(group:set[(int,int)],visit: set[(int, int)], start: (int, int)):
        nonlocal d
        x, y = start
        visit.add((x, y))
        group.add((x, y))
        for tx, ty in d:
            nx, ny = x + tx, y + ty
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if (nx,ny) not in visit and data[nx][ny] == data[x][y]:
                _scan(group, visit, (nx, ny))

    answer = 0
    while True:
        is_boom = False
        visit = set()
        target = []
        for i in range(N-1, -1, -1):
            l = 0
            for j in range(M):
                if data[i][j] == '.':
                    l += 1
                else:
                    group = set()
                    _scan(group, visit, (i,j))
                    if len(group) >= 4:
                        target.append(group)
                        is_boom = True
            if l == M:
                break
        if not is_boom:
            break
        else:
            answer += 1
            _down(target)
    return answer

data = [list(sys.stdin.readline().strip()) for _ in range(12)]
print(solve(data))