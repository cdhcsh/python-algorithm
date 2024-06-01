class Solution(object):
    def maximumTripletValue(self, nums):
        answer = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[i] - nums[j] < 0:
                    break
                for k in range(j + 1, len(nums)):
                    answer = max(answer,(nums[i]-nums[j]) * nums[k])
        return answer

s = Solution()
print(s.maximumTripletValue([1, 10, 3, 4, 19]))
