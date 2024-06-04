class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = set()
        start = 0
        answer = 0
        for i in range(len(s)):
            while s[i] in arr:
                arr.remove(s[start])
                start += 1
            arr.add(s[i])
            answer = max(answer,len(arr))
        return answer
