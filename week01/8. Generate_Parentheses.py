from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def _solve(target: str, left: int, right: int):
            nonlocal n
            if left + right == 2 * n:
                answer.append(target)
                return
            if left < n:
                _solve(target+'(', left + 1, right)
            if right < n and right < left:
                _solve(target + ')', left, right + 1)

        answer = []
        _solve('', 0, 0)
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(8))
