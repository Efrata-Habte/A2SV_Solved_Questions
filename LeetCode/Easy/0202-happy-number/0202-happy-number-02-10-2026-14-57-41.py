class Solution:
    def isHappy(self, n: int) -> bool:
        is_happy = False

        while not is_happy:
            temp = 0
            while n > 0:
                digit = n % 10
                temp += digit**2
                n //= 10
            n = temp
            if temp == 1:
                is_happy = True
            elif temp == 4:
                break

        return is_happy
