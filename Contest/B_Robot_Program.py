def solve():
    t = int(input())
    for _ in range(t):
        n, x, k = map(int, input().split())
        s = input()

        pos = x
        first_zero = -1

        for i in range(n):
            pos += -1 if s[i] == 'L' else 1
            if pos == 0:
                first_zero = i + 1
                break

        if first_zero == -1 or first_zero > k:
            print(0)
            continue

        count = 1
        k -= first_zero

        pos = 0
        cycle = -1
        for i in range(n):
            pos += -1 if s[i] == 'L' else 1
            if pos == 0:
                cycle = i + 1
                break

        if cycle == -1:
            print(count)
            continue

        count += k // cycle
        print(count)

solve()
