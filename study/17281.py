import sys
from itertools import permutations


def solve(n: int, data: list[list[int]]) -> int:
    def _cal(heat:list[int]):
        score = 0
        ing = 0
        no = 5
        while ing < n:
            ru = 0
            out = 3
            while out > 0:
                res = data[ing][heat[no]]
                if res == 0:
                    out -= 1
                elif res == 4:
                    score += (ru.bit_count() + 1)
                    ru = 0
                else:
                    ru = ru * 2 ** res + 2 ** (res - 1)
                    score += (ru // 8).bit_count()
                    ru = ru & 7
                no = (no + 1) % 9
            ing += 1
        return score

    target = permutations(range(1, 9))
    answer = 0
    for t in target:
        answer = max(answer, _cal(list(t)+[0]))
    return answer


n = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(solve(n, data))
