class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        dict = {}
        mat = 0
        while r < len(s):
            if s[r] in dict and l <= dict[s[r]]:
                l = dict[s[r]]+1
            dict[s[r]] = r
            mat = max(mat,r-l+1)
            r+=1
        return mat