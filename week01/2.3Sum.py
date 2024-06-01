import sys
from itertools import combinations


class Solution(object):
    def threeSum(self, nums):
        answer = []
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            self.twoSum(nums, i,answer)
        return answer
    def twoSum(self, nums, target,answer):
        arr = set()
        for i in range(target + 1, len(nums)):
            tmp = - nums[target] - nums[i]
            if tmp in arr:
                answer.append([tmp, nums[target], nums[i]])
                while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                    i += 1
            arr.add(nums[i])

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0,0,0,0]))
