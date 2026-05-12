import math

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        
        def heapify_down(idx):
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2

            if left < n and piles[left] > piles[largest]:
                largest = left
            
            if right < n and piles[right] > piles[largest]:
                largest = right

            if largest != idx:
                piles[idx], piles[largest] = piles[largest], piles[idx]
                heapify_down(largest)

        for i in range(n // 2 - 1, -1, -1):
            heapify_down(i)

        for _ in range(k):
            piles[0] = math.ceil(piles[0] / 2)
            heapify_down(0)

        return sum(piles)