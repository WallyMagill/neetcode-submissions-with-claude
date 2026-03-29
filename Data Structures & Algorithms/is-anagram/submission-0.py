class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        for i in len(s):
            count[ord(s[i] - ord('a'))] += 1
            count[ord(t[i] - ord('a'))] -= 1
        for n in count:
            if n != 0:
                return False
        return True