class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        n = len(nums)
        suffix = 1
        

        for i in range(n):
            if i == 0:
                left.append(1)
                continue
            left.append(left[-1]*nums[i-1])
        
        for i in range(n-1,-1,-1):
            if i == n-1:
                right.append(1*left[i])
            else:
                right.append(left[i]*suffix) 
            suffix  = nums[i]*suffix
        
        right = right[::-1]

        return right
