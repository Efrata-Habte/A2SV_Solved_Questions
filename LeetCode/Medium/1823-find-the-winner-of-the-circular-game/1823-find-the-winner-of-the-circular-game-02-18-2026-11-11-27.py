class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        n=[i for i in range(1,n+1)]
        prev=0

        while len(n)>1:
            pos=(k+prev-1)%len(n)
            n.remove(n[pos])
            prev=pos
    
        return n[0]