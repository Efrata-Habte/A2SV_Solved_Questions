class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = Counter(nums)
        answer = []
        
        for key, val in nums.items():
            if val > n / 3:
                answer.append(key)

        return answer
