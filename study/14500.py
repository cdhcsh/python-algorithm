import sys


def solve(n: int, m: int, data: list[list[int]]) -> int:
    d = [[0, 1], [-1, 0], [1, 0]]
    t = [[[1, 1],[2, 0] ,[1,0],[0, 0]],
         [[1, -1],[2, 0] ,[1,0],[0, 0]],
         [[1, 1], [0, 2],[0, 1], [0, 0]],
         [[-1, 1],[0, 2],[0, 1], [0, 0]]]
    answer = 0

    def _dfs(c: int, start: tuple[int, int], sum: int, visit: set[tuple[int, int]]):
        nonlocal answer
        if c >= 4:
            answer = max(answer, sum)
            return
        for x, y in d:
            tx, ty = start[0] + x, start[1] + y
            if 0 <= tx < n and 0 <= ty < m and (tx, ty) not in visit:
                visit.add((tx, ty))
                _dfs(c + 1, (tx, ty), sum + data[tx][ty], visit)
                visit.remove((tx, ty))

    answer = 0
    for i in range(n):
        for j in range(m):
            _dfs(0, (i, j), 0, set((i, j)))
            for l in t:
                tmp = 0
                for x, y in l:
                    tx, ty = i + x, j + y
                    if not (0 <= tx < n and 0 <= ty < m):
                        break
                    tmp += data[tx][ty]
                else:
                    answer = max(answer, tmp)

    return answer


n, m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(solve(n, m, data))
