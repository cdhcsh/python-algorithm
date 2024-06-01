from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        tmp = -(10**9)
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < tmp:
                return True
            while stack and stack[-1] < nums[i]:
                tmp = stack.pop()
            stack.append(nums[i])
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.find132pattern([1,0,1,-4,-3]))