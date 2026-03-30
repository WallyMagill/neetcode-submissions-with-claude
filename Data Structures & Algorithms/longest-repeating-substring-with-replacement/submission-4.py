class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.Counter()
        maxfreq = 0
        l = 0
        ans = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxfreq = max(maxfreq, count[s[r]])
            while (r - l + 1) - maxfreq > k:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans