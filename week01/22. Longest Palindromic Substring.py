class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l:int,r:int)->str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        if len(s) <= 0 or s == s[::-1]:
            return s
        answer = ''
        for i in range(len(s)-1):
            answer = max(answer,check(i,i+1),check(i,i+2),key=len)
        return answer

