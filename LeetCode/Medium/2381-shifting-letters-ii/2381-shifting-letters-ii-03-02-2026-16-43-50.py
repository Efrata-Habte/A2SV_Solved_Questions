class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        ans = []
        shift=[0]*n

        for left,right,drxn in shifts:
            if drxn:
                shift[left]+=1
                if right+1 < n :
                    shift[right+1] -=1
            else:
                shift[left]-=1
                if right+1 < n:
                    shift[right+1]+=1

        for i in range(1,n):
            shift[i]+=shift[i-1]
        
        for i in range(n):
            ch = ord(s[i]) - ord("a")
            newChar = chr(ord("a") + ((ch+shift[i]) % 26))
            ans.append(newChar)
        
        return "".join(ans)

        
        

