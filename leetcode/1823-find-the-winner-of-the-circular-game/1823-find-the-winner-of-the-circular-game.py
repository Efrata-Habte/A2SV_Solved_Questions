class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1,n+1)]
        pos = 0
        while len(nums) > 1:
            pos = (pos + k - 1) % len(nums)
            nums.pop(pos)

        return nums[0]