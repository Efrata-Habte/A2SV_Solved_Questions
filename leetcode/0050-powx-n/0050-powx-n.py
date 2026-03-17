class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n

        return self.fastPow(x,n)

    def fastPow(self, x:float,n:int)->float:

        if n == 0:
            return 1.0

        halfs = self.fastPow(x,n//2)

        if n%2 == 0:
            return halfs*halfs
        else:
            return halfs*halfs*x
