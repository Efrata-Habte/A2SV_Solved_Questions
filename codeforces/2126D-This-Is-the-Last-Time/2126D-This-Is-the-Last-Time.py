def solve():
    n, k = map(int,input().split())
    casino = []

    

    for i in range(n):
       (a,b,c) = map(int,input().split())
       casino.append((a,b,c))


    casino = sorted(casino, key=lambda x : x[0],reverse=False)
    # print(casino)
    max_ = 0

    for i in casino:
        if k >= i[0] and i[0] <= i[2] <= i[1]:
            if k<i[2]:
                k = i[2]
            max_ = max(max_,k)
    
        
    return max(max_, k)

for _ in range(t):
    print(solve())