class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] 
        s2 = float('-inf') 

        for n in reversed(nums):
            if n < s2:
                return True
            
            while stack and n > stack[-1]:
                s2 = stack.pop()
            
            stack.append(n)
            
        return False