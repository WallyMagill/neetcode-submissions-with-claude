class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum() and left < right:
                left += 1
            if not s[right].isalnum() and left < right:
                right -= 1
            if s[left].tolower() != s[right].tolower():
                return False
        return True