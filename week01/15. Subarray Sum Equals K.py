from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer = 0
        dict = 0
        d = {0: 1}
        for i in nums:
            dict = dict + i
            if dict - k in d:
                answer = answer + d[dict - k]
            if dict not in d:
                d[dict] = 1
            else:
                d[dict] = d[dict] + 1
        return answer

if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1,1,1], 2))