class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return True if set(nums) == len(nums) else False