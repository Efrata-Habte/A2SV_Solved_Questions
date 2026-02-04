class Solution:    
    def findUnion(self, a, b):
        a = set(a)
        b = set(b)
        
        ans = list(a)
        
        for i in b:
            if i not in ans:
                ans.append(i)
                
        return ans
