t = int(input().strip())

def booooring_day():
    n,l,r = map(int,input().split())
    arr = list(map(int,input().split()))

    left=0
    curr=0
    count = 0

    for right in range(n):
        curr += arr[right]

        while curr>r and left<=right:
            curr-=arr[left]
            left+=1

        if l<= curr <= r:
            count+=1
            curr=0
            left=right+1
    
    print(count)

for _ in range(t):
    booooring_day()