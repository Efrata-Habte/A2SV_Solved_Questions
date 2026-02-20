class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer=["" for i in range(len(nums))]
        for i in range(len(nums)):
            nums[i]=(i,nums[i])

        nums.sort(key=lambda x: x[1])

        answer[nums[0][0]]=0
        for i in range(1,len(nums)):
            if nums[i][1]==nums[i-1][1]:
                answer[nums[i][0]]= answer[nums[i-1][0]]
            else:
                answer[nums[i][0]]=i
        
        return answer