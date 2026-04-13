class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return False if set(nums) != len(nums) else True