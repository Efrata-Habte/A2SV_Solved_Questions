class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 1
        min_val = nums[0]

        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
            min_val = min(min_val,nums[i])

        if min_val<0:
            start = abs(min_val)+1
        
        return start
