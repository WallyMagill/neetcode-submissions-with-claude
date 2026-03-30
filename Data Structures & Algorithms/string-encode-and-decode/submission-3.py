class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ''
        for s in strs:
            ans += str(len(s)) + '#' + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            k = i
            while s[k] != '#':
                k += 1
            length = int(s[i:k])
            i = k + 1
            k = i + length
            ans.append(s[i:k])
            i = k + 1
            