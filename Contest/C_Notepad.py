t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    history = {}
    found = False

    for i in range(n - 1):
        pair = s[i:i+2]
        
        if pair in history and history[pair] <= i:
            found = True
            break
        
        if pair not in history:
            history[pair] = i +2

    if found:
        print("YES")
    else:
        print("NO")