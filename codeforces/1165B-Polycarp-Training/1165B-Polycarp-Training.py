n = int(input())
contests = list(map(int,input().split()))

contests.sort()
days = 0
k = 1

for i in range(n):
    if contests[i] >= k:
        days += 1
        k += 1
    
print(days)