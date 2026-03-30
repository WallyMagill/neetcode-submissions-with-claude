class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check = set()
        maxSet = 0
        l = 0
        for c in s:
            if c in check:
                while c in check and check:
                    check.remove(s[l])
                    l += 1
            check.add(c)
            maxSet = max(maxSet, len(check))
        return maxSet