def solve():
    n = int(input())
    arr1 = list(map(int,input().split()))
    m = int(input())
    arr2 = list(map(int,input().split()))
    max_1 = max(0,arr1[0])
    max_2 = max(0,arr2[0])

    for i in range(1,n):
        arr1[i] += arr1[i-1]
        max_1 = max(max_1,arr1[i])
    # print(max_1)
    
    for j in range(1,m):
        arr2[j] += arr2[j-1]
        max_2 = max(max_2,arr2[j])
    # print(max_2)
    
    print(max_1 + max_2)  

for _ in range(t):
    solve()