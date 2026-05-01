class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        right = 0

        while i < 3:
            left = right
            while left < n:
                if nums[left] == i:
                    nums[left], nums[right] = nums[right], nums[left]
                    right += 1
                left += 1

            i += 1
