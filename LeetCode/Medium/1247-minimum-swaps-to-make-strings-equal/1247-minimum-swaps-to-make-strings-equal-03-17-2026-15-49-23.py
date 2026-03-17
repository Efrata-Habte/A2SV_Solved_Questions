class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if len(s1) != len(s2):
            return -1

        unmatched1 = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                unmatched1.append(s1[i])

        if len(unmatched1) == 0:
            return 0
        
        if len(unmatched1) % 2 == 1:
            return -1

        unmatched1.sort()        
        swap = 0

        for i in range(0,len(unmatched1),2):
            if unmatched1[i:i+2] == ["x","x"] or unmatched1[i:i+2] == ["y","y"]:
                swap+=1
            elif unmatched1[i:i+2] == ["x","y"] or unmatched1[i:i+2] == ["y","x"]:
                swap+=2
        
        return swap        
