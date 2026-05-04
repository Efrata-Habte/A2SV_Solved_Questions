class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's cycle detection algorithm

        # pahse -1 detecting cycle (treat the array as a linked list)
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break

        # phase -2 finding the entrance point of the cycle
        slow = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow