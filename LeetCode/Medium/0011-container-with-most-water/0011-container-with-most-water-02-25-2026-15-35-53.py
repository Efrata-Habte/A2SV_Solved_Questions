class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        max_water = 0
        volume = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            volume = h * w

            max_water = max(max_water, volume)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
