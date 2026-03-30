class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        maxSet = 0
        l = 0
        for c in s:
            while c in check:
                check.remove(s[l])
                l += 1
            check.add(c)
            maxSet = max(maxSet, len(check))
        return maxSet