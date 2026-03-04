class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]

        for right in range(1, len(nums)):
            if nums[right - 1] >= 0:
                nums[right] += nums[right - 1]

            max_ = max(max_, nums[right])

        return max_
