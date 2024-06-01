class Solution(object):
    def maximumTripletValue(self, nums):

        big = (0, nums[0])
        sub = (0, nums[0])
        small = (1, nums[1])
        answer = max(0, (big[1] - small[1]) * nums[2])
        print(big[1], '-', small[1], '*', nums[2], '=', (big[1] - small[1]) * nums[2])
        for i in range(3, len(nums)):
            if nums[i - 2] - nums[i - 1] > big[1] - small[1]:
                big = (i - 2, nums[i - 2])
                small = (i - 1, nums[i - 1])
            if nums[i - 1] <= small[1]:
                small = (i - 1, nums[i - 1])
            if sub[1] > big[1] and sub[0] < small[0]:
                big = sub
            answer = max(answer, (big[1] - small[1]) * nums[i])
            print('big', big[0], 'small', small[0])
            print(big[1], '-', small[1], '*', nums[i], '=', (big[1] - small[1]) * nums[i])
            if nums[i] < small[1]:
                if big[1] < small[1]:
                    big = small
                small = (i, nums[i])
            if sub[1] < nums[i - 2]:
                sub = (i - 2, nums[i - 2])
        return answer


s = Solution()
print(s.maximumTripletValue([16, 15, 12, 5, 4, 12, 15, 17, 5, 18, 6, 16, 1, 17, 4]))
# print(s.maximumTripletValue([16,2,10,20,16,2,13,8,19]))
# print(s.maximumTripletValue([1,10,3,4,19]))
# print(s.maximumTripletValue([12,6,1,2,7]))
