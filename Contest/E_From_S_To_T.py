from collections import Counter

def solve():
    s = input()
    t = input()
    p = input()

    i = 0
    for char in t:
        if i < len(s) and s[i] == char:
            i += 1
    
    if i != len(s):
        print("NO")
        return

    count_s = Counter(s)
    count_p = Counter(p)
    count_t = Counter(t)

    for char in count_t:
        if count_t[char] > count_s[char] + count_p[char]:
            print("NO")
            return

    print("YES")

q = int(input())
for _ in range(q):
    solve()