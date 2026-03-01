def calc_min (chars):
    c = chars[0]
    swap = 0
    total = chars.count(c)
    for i in range(total):
        if chars[i]!=c:
            swap+=1
    return swap

n = int(input())
chars = list(x for x in input().strip())
chars+=chars
res = calc_min(chars)

for i in range(n):
    test = chars[i:i+n]
    res = min(res,calc_min(test))

print(res)