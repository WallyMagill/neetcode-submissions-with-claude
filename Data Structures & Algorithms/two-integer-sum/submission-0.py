class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i, n in enumerate(nums):
            goal = target - n
            if goal in check:
                return [check[goal], i]
            check[n] = i