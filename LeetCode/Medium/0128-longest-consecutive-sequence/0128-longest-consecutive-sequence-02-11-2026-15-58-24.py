class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        _max = 0
        nums.sort()
        curr = 0
        n=len(nums)

        if n==0:
            return 0
        if n==1:
            return 1

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                curr += 1
            elif nums[i+1]-nums[i]==0:
                continue
            else:
                curr = 0

            _max = max(curr, _max)
        return _max+1 
