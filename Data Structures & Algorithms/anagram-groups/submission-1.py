class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            groups[''.join(sorted(s))].append(s)
        ans = []
        for g in groups:
            temp = list(groups[g].values())
            ans.append(temp)
        return ans