from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodes = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        queue = deque()
        visit = [0] * numCourses

        for start,dist in prerequisites:
            nodes[start].append(dist)
            indegree[dist] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                visit[i] = 1

        while queue:
            current = queue.popleft()
            for n in nodes[current]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    visit[n] = 1
                    queue.append(n)

        return sum(visit) == numCourses




if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(numCourses=2, prerequisites=[[1,0]]))

