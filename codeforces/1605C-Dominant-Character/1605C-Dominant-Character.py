from collections import defaultdict
t = int(input())

def solve():
    n = int(input())
    s = input()
    
    if "aa" in s:
        return 2
    elif "aca" in s or "aba" in s:
        return 3
    elif "acba" in s or "abca" in s:
        return 4
    elif "abbacca" in s or "accabba" in s:
        return 7
    else:
        return -1

for _ in range(t):
    print(solve())