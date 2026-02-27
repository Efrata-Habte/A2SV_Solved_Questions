from collections import Counter

n, m = map(int,input().split())
num1 = Counter(list(map(int,input().split())))
num2 = Counter(list(map(int,input().split())))
count = 0

for key, val in num1.items():
    if key in num2:
        count += val*num2[key]

print(count)