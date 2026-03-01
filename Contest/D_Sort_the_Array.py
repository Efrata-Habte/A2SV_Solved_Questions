n = int(input())
arr = list(map(int, input().split()))

first = -1
last = -1

for i in range(n-1):
    if arr[i] > arr[i+1]:
        first = i
        break

if first == -1:
    print("yes")
    print(1, 1)
else:
    for i in range(n-1, 0, -1):
        if arr[i-1] > arr[i]:
            last = i
            break

    arr[first:last+1] = arr[first:last+1][::-1]

    if arr == sorted(arr):
        print("yes")
        print(first+1, last+1) 
    else:
        print("no")
