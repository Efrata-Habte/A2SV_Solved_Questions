n , m = map(int,input().split())

files = []
original_sum=0
changes =[]

for i in range(n):
    files.append(tuple(map(int,input().split())))
    original_sum+=files[i][0]
    changes.append (files[i][0]-files[i][1])

changes.sort(reverse=True)
j=0

while original_sum > m and j<n:
    original_sum-=changes[j]
    j+=1

if original_sum <=m:
    print(j)
else:
    print(-1)