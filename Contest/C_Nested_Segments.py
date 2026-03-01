n= int(input())
segments=[]

for _ in range(n):
    segments.append(tuple(map(int, input().split())))

mapp=segments.copy()
segments.sort()
is_found=False
temp=[]

for s in range(n):
    segment = segments[s]
    for j in range(n):
        if s==j:
            continue
        if segment[0]<= segments[j][0] and segment[1]>=segments[j][1]:
            is_found=True
            temp.append(segments[j])
            temp.append(segment)
            break
    
    if is_found:
        break

if is_found:
    first_idx=mapp.index(temp[0])
    mapp[first_idx]=()
    print(first_idx+1,mapp.index(temp[1])+1)
else:
    print(-1,-1)
