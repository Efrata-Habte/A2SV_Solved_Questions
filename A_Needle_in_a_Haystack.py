from collections import Counter

n = int(input())

def Needle_in_haystack():
    s = input()
    t = input()

    s_count = Counter(s)
    t_count = Counter(t)

    for key, val in s_count.items():
        if key not in t_count or val > t_count[key]:
            return "Impossible"
        else:
            t_count[key] -= val

    result = []
    k=0

    t_count = sorted(t_count.items(), key=lambda x: x[0])

    for i, j in t_count:
        while k <len(s) and s[k]<=i:
            result.append(s[k])
            k+=1
        result.append(i*j)

    result.append(s[k:])

    return "".join(result)


for _ in range(n):
    print(Needle_in_haystack())