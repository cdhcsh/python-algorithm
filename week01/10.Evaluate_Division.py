from collections import deque
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = {}
        answer = []
        def _bfs(s: str, e: str) -> int:
            visit = {}
            queue = deque()
            if s not in nodes:
                return -1
            queue.append(s)
            visit.setdefault(s,1)
            while queue:
                node = queue.popleft()
                if node == e:
                    return visit.get(node)
                connects = nodes.get(node, [])
                for n, v in connects:
                    if n not in visit:
                        visit.setdefault(n, visit.get(node) * v)
                        queue.append(n)
            return -1

        for i, l in enumerate(equations):
            s, e = l
            if s in nodes:
                nodes.get(s).append((e, values[i]))
            else:
                nodes.setdefault(s, [(e, values[i])])
            if e in nodes:
                nodes.get(e).append((s, 1/values[i]))
            else:
                nodes.setdefault(e, [(s, 1/values[i])])
        for query in queries:
            s,e = query
            res = _bfs(s, e)
            answer.append(res)
        return answer

if __name__ == '__main__':
    sol = Solution()
    print(sol.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                           [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
