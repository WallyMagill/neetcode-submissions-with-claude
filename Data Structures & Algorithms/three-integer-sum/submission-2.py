class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and nums[i - 1] == n:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    ans.append[[n, nums[l], nums[r]]]
                    l += 1
                    r -= 1
                    while nums[l - 1] == nums[l]:
                        l += 1
        return ans
            