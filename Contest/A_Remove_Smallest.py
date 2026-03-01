t=int(input())

def remove_smallest(a,n):
    a.sort()
    for i in range(n-1):
        if a[i+1]-a[i]>1:
            print("NO")
            return    
    print("YES")

for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    remove_smallest(a,n)

    