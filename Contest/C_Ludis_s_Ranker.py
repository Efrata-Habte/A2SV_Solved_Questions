from collections import Counter

n=int(input())
arr=list(map(int,input().split()))

arr_count=Counter(arr)
arr_count= dict(sorted(arr_count.items(),key=lambda x :x[0],reverse=True))

rank=0
for i in arr_count:
    temp= arr_count[i]
    arr_count[i]=rank+1
    rank +=temp

ans=[arr_count[j] for j in arr]

for k in ans:
    print (k, end=" ")