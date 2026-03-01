arr= list(map(int,(input().split())))
n=arr[0]
target = arr[1]
count=0

factor= target/n

while factor%2==0 or factor%3==0:
    if factor%2==0:
        factor/=2
    else:
        factor/=3
    count+=1

if factor==1:
    print(count)
else:
    print(-1)