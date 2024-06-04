from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * (n-i + 1) for i in range(n+1)]

        for i in range(n):
            dp[1][i] = nums[i]

        for l in range(2, n+1):
            for p in range(len(dp[l])):
                dp[l][p] = max(nums[p]-dp[l-1][p+1],nums[p+l-1]-dp[l-1][p])

        return dp[n][0] >= 0



if __name__ == '__main__':
    s = Solution()
    print(s.predictTheWinner([1,1]))
