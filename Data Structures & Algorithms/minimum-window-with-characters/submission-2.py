class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = collections.Counter(t)
        window = collections.Counter()
        have, need = 0, len(countT)
        l = 0
        ans = ""
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                curr = s[l:r+1]
                if ans == "" or len(curr) < len(ans):
                    ans = curr
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return ans