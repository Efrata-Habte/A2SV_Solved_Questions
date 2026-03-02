class NumArray:

    def __init__(self, nums: List[int]):
        self.total = [0]

        for i in range(0,len(nums)):
            temp = self.total[i] + nums[i]
            self.total.append(temp)

    def sumRange(self, left: int, right: int) -> int:
        return self.total[right] - self.total[left]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)