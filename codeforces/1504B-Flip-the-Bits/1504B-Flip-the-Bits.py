def solve():
    n = int(input())
    a = input()
    b = input()

    balance = [0]*n
    curr = 0

    for i in range(n):
        if a[i] == "1":
            curr += 1
        else:
            curr -= 1
        
        balance[i] = curr
    
    # print(balance)
    flipped = False

    for i in range(n-1,-1,-1):
        current = a[i]

        if flipped:
            current = "1" if current == "0" else "0"
        
        if current == b[i]:
            continue

        if balance[i] != 0 :
            return "NO"
        
        flipped = not flipped
    
    return "YES"

for _ in range(t):
    print(solve())