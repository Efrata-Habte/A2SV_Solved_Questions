class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = (n*(n+1))//2
        numbers = set()
        summ = 0
        answer = []

        for num in nums:
            if num in numbers:
                answer.append(num)
                summ -= num
            numbers.add(num)
            summ += num
        
        missing = total - summ
        answer.append(missing)

        return answer
        


