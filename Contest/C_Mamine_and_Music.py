n, k = map(int, input().split())
arr = list(map(int, input().split()))


instruments = []
for i in range(n):
    instruments.append((arr[i], i + 1))

instruments.sort()

max_indices = []
curr_days = 0

for days, index in instruments:
    if curr_days + days <= k:
        curr_days += days
        max_indices.append(index)
    else:
        break

print(len(max_indices))
print(*(max_indices))
