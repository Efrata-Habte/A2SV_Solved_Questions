class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = Counter(nums)
        for i,j in num.items():
            if j == 1 :
                return i
