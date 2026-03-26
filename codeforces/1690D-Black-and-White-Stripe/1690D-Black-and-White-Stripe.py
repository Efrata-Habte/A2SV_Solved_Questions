def solve():
    n, k = map(int,input().split())
    s = input()

    w_count = 0
    min_count = float("inf")
    left = 0

    for right in range(n):
        if s[right] == "W":
            w_count += 1

        while (right - left + 1) > k:
            if s[left] == "W":
                w_count -=1
            left+=1
            
        if (right - left + 1) == k:
            min_count = min(min_count,w_count)

    return min_count

for _ in range(t):
    print(solve())