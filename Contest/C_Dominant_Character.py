t = int(input())

def dominant_character(s,n):

    if "aa" in s:
        return 2
    elif "aba" in s or "aca" in s:
        return 3
    elif "abac" in s or "acab" in s or "caba" in s or "baca" in s or "abca" in s or "acba" in s:
        return 4
    else:
        return -1

for _ in range(t):
    n = int(input())
    s = input()
    print(dominant_character(s,n))