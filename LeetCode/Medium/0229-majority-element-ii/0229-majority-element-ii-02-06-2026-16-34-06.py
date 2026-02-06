class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target= len(nums)/3
        count=Counter(nums)
        ans=[]

        for key,val in count.items():
            if val > target:
                ans.append(key)

        return ans