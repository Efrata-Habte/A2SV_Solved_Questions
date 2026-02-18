class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)
        binary = binary[2:]

        return False if "11" in binary or "00" in binary else True
