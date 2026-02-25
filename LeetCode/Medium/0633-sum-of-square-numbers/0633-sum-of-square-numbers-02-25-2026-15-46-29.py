class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt = int(c ** (0.5))

        left = 0
        right = sqrt

        while left <= right:
            summ = left**2 + right**2
            if summ == c:
                return True
            elif summ < c:
                left += 1
            else:
                right -= 1

        return False
