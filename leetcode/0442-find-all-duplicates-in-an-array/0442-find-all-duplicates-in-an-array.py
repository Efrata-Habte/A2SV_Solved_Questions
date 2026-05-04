class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                answer.append(nums[i])

        return answer