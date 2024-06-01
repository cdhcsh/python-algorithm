# https://leetcode.com/contest/weekly-contest-164/problems/minimum-time-visiting-all-points/submissions/1272841091/

from typing import List


class Solution:
    def cal(self, a: list[int], b: list[int]):
        xd = abs(a[0] - b[0])
        yd = abs(a[1] - b[1])
        return min(xd, yd) + abs(xd - yd)

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        p = points[0]
        for next in points[1:]:
            answer += self.cal(p, next)
            p = next
        return answer
