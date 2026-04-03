class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        def power(res, p):
            r = 1
            while p > 0:
                if p % 2 == 1:
                    r = (r * res) % MOD
                res = (res * res) % MOD
                p //= 2
            return r

        odd_count = n//2
        even_count = n-odd_count
        return (power(5, even_count) * power(4 , odd_count)) % MOD


        # n -=1
        # def count(n):
        #     if n == -1:
        #         return 1
        #     if n%2==0:   
        #         return count(n-1) * 5
        #     return count(n - 1) * 4
        
        # return count(n) % (10**9 + 7)
        