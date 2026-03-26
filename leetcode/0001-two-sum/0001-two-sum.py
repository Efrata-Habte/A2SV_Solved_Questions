class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        container={}
        diff=0

        for i in range(len(nums)):
            diff=target-nums[i]
            if nums[i] in container:
                return [container[nums[i]],i]  
            container[diff]=i
            
        
