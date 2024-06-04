class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        start = 0
        end = len(height) - 1
        while start < end:
            answer = max(answer , (end-start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return answer