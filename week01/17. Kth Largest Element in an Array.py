from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [0]*(10**4 + 1)
        for n in nums:
            arr[n] += 1
        for i in range(len(arr)-1, -1, -1):
            if arr[i] >= k:
                return i
            k -= arr[i]

