from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        answer = 0
        for i in range(len(height)):
            if stack and height[i] > height[stack[-1]]:
                pre = stack.pop()
                while stack and height[stack[-1]] <= height[i]:
                    h = stack.pop()
                    if height[h] <= height[pre]:
                        continue
                    answer += (height[h]-height[pre]) * ((i-1) - h)
                    pre = h
                if stack:
                    answer += (height[i] - height[pre]) * ((i - 1) - stack[-1])
            stack.append(i)
        return answer


s = Solution()
print(s.trap([4,2,0,3,2,5]))
