class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ones = 0
        left = 0 
        k = 0

        for right in range(len(nums)):
            if nums[right]==0:
                k+=1

            while left < right and k>1:
                if nums[left] ==0:
                    k-=1
                left+=1

            max_ones = max(max_ones,right - left)
        
        return max_ones
