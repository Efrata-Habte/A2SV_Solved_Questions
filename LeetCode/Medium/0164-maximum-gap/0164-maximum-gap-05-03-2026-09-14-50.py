class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        gap = 0
        n = len(nums)

        nums.sort()

        for i in range(1,n):
            gap = max(gap, nums[i]-nums[i-1])

        return gap