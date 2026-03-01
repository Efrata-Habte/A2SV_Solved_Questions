from collections import defaultdict
t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort()
    count = defaultdict(int)
    count[arr[0]]+=1
    l = 0
    ans = 0

    for r in range(1,n):
        prev = arr[r-1]
        count[arr[r]]+=1

        while len(count) > k :
            count[arr[l]]-=1
            if count[arr[l]]==0:
                del count[arr[l]]
            l+=1
        
        if prev+1 < arr[r]:
            l = r
            count.clear()
            continue


        ans = max(ans,r-l+1)

    print (ans)

        