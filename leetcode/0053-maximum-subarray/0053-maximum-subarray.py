class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        for right in range(1,len(nums)):
            if nums[right-1]>=0:
                nums[right]+=nums[right-1]

        return max(nums)
