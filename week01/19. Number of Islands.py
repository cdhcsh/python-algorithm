from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        d = [[0, 1],[0, -1], [1, 0], [-1, 0]]
        answer = 0
        visit = [[True] * (len(grid[0])) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visit[i][j]:
                    queue = deque([(i, j)])
                    visit[i][j] = False
                    while queue:
                        x,y = queue.popleft()
                        for dx, dy in d:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                                if grid[nx][ny] == '1' and visit[nx][ny]:
                                    queue.append((nx, ny))
                                    visit[nx][ny] = False
                    answer += 1
        return answer

if __name__ == '__main__':
    s = Solution()
    print(s.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))