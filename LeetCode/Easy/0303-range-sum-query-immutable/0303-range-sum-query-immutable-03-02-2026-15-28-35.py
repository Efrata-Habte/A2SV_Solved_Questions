class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.total = [nums[0]]

        for i in range(1,len(self.nums)):
            temp = self.total[i-1] + self.nums[i]
            self.total.append(temp)

    def sumRange(self, left: int, right: int) -> int:
        return self.total[right] - self.total[left-1] if left > 0 else self.total[right]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)