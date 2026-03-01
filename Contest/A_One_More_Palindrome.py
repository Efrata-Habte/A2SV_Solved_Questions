from collections import Counter

t = int(input())

def one_more_palindrome():
    s = input()
    s_count = Counter(s)
    n = len(s)

    if len(s_count)==1:
        return "NO" 
    
    left =0

    while left<n//2:
        if left+1 < n//2:
            if s[left]!= s[left+1]:
                return "YES"
        left+=1
    
    return "NO"

for _ in range(t):
    print (one_more_palindrome())
