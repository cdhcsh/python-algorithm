from typing import List
from re import split


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        answer = []
        operators = ['+', '-', '*']

        def cal(oper: list[str]) -> int:
            nonlocal N
            res = pre = int(oper[0])
            i = 1
            while i < len(oper):
                m = int(oper[i + 1])
                if oper[i] == '+':
                    res += m
                elif oper[i] == '-':
                    m = -m
                    res += m
                elif oper[i] == '*':
                    res -= pre
                    m = m * pre
                    res += m

                pre = m
                i += 2
            return res

        def _dfs(n: int, oper: list[str]):
            nonlocal N, answer
            if n == N:
                if cal(oper) == target:
                    answer.append(''.join(oper))
                return
            if oper[-1] != '0':
                tmp = oper[-1]
                oper[-1] = str(int(oper[-1]+num[n]))
                _dfs(n + 1, oper)
                oper[-1] = tmp
            for i in range(3):
                oper.append(operators[i])
                oper.append(num[n])
                _dfs(n + 1, oper)
                oper.pop()
                oper.pop()

        _dfs(1, [num[0]])
        return answer


if __name__ == '__main__':
    s = Solution()
    print(s.addOperators("105", 5))
