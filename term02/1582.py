#https://leetcode.com/submissions/detail/1272833968/
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        visit = [[False] * len(mat[0]) for _ in range(len(mat))]
        answer = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and not visit[i][j]:
                    visit[i][j] = True
                    flag = True
                    for x in range(len(mat)):
                        if x != i and mat[x][j] == 1:
                            visit[x][j] = True
                            flag = False
                    for y in range(len(mat[0])):
                        if y != j and mat[i][y] == 1:
                            visit[i][y] = True
                            flag = False
                    if flag:
                        answer += 1
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.numSpecial([[1,0,0],[0,1,0],[0,0,1]]))
