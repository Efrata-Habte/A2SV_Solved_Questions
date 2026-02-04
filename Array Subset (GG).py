#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        counta=Counter(a)
        countb=Counter(b)
        
        for i in countb:
            if (i not in counta) or (counta[i]<countb[i]):
                return False
            
        return True
    
    
    
