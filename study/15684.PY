import sys


def solve(n: int, h: int, defaults: set[(int, int)]) -> int:
    data = [[0] * n for i in range(h)]

    def _add_line(i: int, j: int):
        data[i - 1][j - 1] = 1
        data[i - 1][j] = -1

    def _del_line(i: int, j: int):
        data[i - 1][j - 1] = 0
        data[i - 1][j] = 0

    def _validate() -> bool:
        for j in range(n):
            p = j
            for i in range(h):
                p += data[i][p]
            if p != j:
                return False
        return True

    [_add_line(i, j) for i, j in defaults]
    if _validate():
        return 0

    visit = [[True]*n for _ in range(h)]
    for i,j in defaults:
        visit[i-1][j] = False
    answer = 10
    def _dfs(x: int, c: int):
        nonlocal n, h, answer
        if _validate():
            answer = min(answer, c)
        elif c < 3:
            for i in range(x, h + 1):
                for j in range(1, n):
                    if visit[i-1][j] and visit[i-1][j-1]:
                        if j < n-1 and not visit[i-1][j+1]:
                            continue
                        visit[i-1][j] = False
                        _add_line(i,j)
                        _dfs(i, c + 1)
                        _del_line(i,j)
                        visit[i-1][j] = True

    _dfs(1, 0)
    if answer > 3:
        return -1
    else:
        return answer


n, m, h = map(int, sys.stdin.readline().split())
defaults = set()
[defaults.add(tuple(map(int, sys.stdin.readline().split()))) for _ in range(m)]
print(solve(n, h, defaults))
