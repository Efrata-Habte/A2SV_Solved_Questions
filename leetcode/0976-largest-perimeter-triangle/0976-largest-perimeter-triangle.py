class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        p = 1
        max_ = 0

        for i in range(2, n):
            a = nums[l]
            b = nums[p]
            c = nums[i]
            perimeter = a + b + c
            if a + b > c and b + c > a and c + b > a:
                max_ = max(max_, perimeter)
            l += 1
            p += 1

        return max_
