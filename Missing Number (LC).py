class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        target_sum= (n*(n+1))//2
        curr_sum=sum(nums)
        return target_sum - curr_sum
