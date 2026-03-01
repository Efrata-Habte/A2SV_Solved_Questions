from collections import Counter
t = int(input())

for _ in range(t):
    m,s=map(int,input().split())
    arr = list(map(int,input().split()))

    arr_count=Counter(arr)
    i=1

    while s>0:
        if i in arr_count:
            i+=1
            continue
        arr.append(i)
        s-=i
        i+=1

    n= len(arr)

    if s==0 and (n*(n+1))/2 == sum(arr):
        print("YES")
    else:
        print("NO")



