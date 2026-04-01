class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = -1

        def possible(mid):
            hours = 0

            for p in piles:
                hours += math.ceil(p/mid)
            return hours

        while left <= right:
            mid = left + (right-left)//2
            if possible(mid) <= h:
                ans = mid
                right = mid -1
            else:
                left = mid + 1
        
        return ans