from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        counta = Counter(a)
        countb = Counter(b)
        
        for i in countb:
            if i not in counta:
                return False  
            elif counta[i] != countb[i]:
                return False
        return True
