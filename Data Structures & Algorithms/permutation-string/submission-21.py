class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        count1 = collections.Counter(s1)
        count2 = collections.Counter()
        for i in range(len(s1)):
            count2[s2[i]] += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if count1 == count2:
                return True
            count2[s2[r]] += 1
            count2[s2[l]] -= 1
        return True if count1 == count2 else False