class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count=Counter(nums)
        
        for num,count in num_count.items():
            if count>1:
                return True
        
        return False