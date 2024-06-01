class Solution(object):
    def findNonMinOrMax(self, nums:list[int]):
        n,m = min(nums), max(nums)
        res = set(nums)
        res.remove(n)
        if len(res) <= 0:
            return -1
        res.remove(m)
        if len(res) <= 0:
            return -1
        else:
            return res.pop()


s = Solution()
print(s.findNonMinOrMax([2,1,3]))