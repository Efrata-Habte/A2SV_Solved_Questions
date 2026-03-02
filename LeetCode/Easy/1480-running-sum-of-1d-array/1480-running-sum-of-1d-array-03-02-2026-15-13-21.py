class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        _sum = [0]

        for i in range(len(nums)):
            _sum.append(_sum[i]+nums[i])

        return _sum[1:]