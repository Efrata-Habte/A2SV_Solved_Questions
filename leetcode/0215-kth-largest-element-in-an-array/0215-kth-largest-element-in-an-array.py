class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        smallest, largest = min(nums), max(nums)
        size = largest - smallest + 1

        count = [0] * size

        for num in nums:
            count[num - smallest] += 1

        remaining = k
        for i in range(size - 1, -1, -1):  
            remaining -= count[i]
            if remaining <= 0:
                return i + smallest