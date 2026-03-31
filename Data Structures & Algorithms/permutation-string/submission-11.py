class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) > len(s2):
            return False
        p1 = p2 = 0
        while p2 < len(s2) - 1:
            while s1[p1] == s2[p2]:
                p1 += 1
                p2 += 1
                if p1 == len(s1):
                    return True
            p1 = 0
            p2 += 1
        return False
        