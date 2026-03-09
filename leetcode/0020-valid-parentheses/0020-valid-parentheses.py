class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        correct = {")":"(","]":"[","}":"{"}

        for i in s:
            if i not in correct:
                stack.append(i)
                continue
            
            if stack and stack[-1]==correct[i]:
                stack.pop()
            else:
                return False
        
        return True if not stack else False
            
                        