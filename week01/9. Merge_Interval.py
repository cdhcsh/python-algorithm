from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        tmp = intervals[0]
        answer = []
        for l in intervals[1:]:
            if l[0] <= tmp[1]:
                tmp[1] = max(tmp[1], l[1])
            else:
                answer.append(tmp)
                tmp = l
        answer.append(tmp)
        return answer

if __name__ == '__main__':
    solution = Solution()
    print(solution.merge([[1,4],[4,5]]))