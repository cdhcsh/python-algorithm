from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = bisect_left(nums, target)
        r = bisect_right(nums, target) - 1
        if n == 0 or l >= n or r >= n or nums[l] != target or nums[r] != target:
            return [-1, -1]
        else:
            return [l, r]
