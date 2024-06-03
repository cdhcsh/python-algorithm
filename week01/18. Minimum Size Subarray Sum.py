from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        s = e = 0
        sum = nums[0]
        answer = n + 1
        l = 1
        while s <= e and e < n:
            if sum >= target:
                answer = min(answer, l)
                if s == e:
                    s += 1
                    e += 1
                    if s < n:
                        sum = nums[s]
                else:
                    sum -= nums[s]
                    s += 1
                    l -= 1
            else:
                e += 1
                if e >= n:
                    break
                sum += nums[e]
                l += 1
        if answer == n + 1:
            return 0
        else:
            return answer


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(4, [1,4,4]))
