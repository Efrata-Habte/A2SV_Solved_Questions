class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        _max=0
        left=0
        right=len(piles)-1

        while left<right:
            _max+=piles[right-1]
            right-=2
            left+=1

        return _max

        