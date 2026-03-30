class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)): 
            prefix = nums[i]
            ans[i] *= prefix
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            postfix *= nums[i]
            ans[i] *= postfix
        return ans