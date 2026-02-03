class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        return x==x[::-1]

# optimized solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        reversed_num=0
        n=x

        while n>0:
            digit=n%10
            reversed_num = reversed_num*10 +digit
            n//=10
        
        return x==reversed_num
