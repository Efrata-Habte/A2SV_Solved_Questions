matrix= [list(map(int,input().split())) for _ in range(5)]

pos=[]

for r in range(5):
    for c in range(5):
        if matrix[r][c]==1:
            pos.append((r,c))

print (abs(2-pos[0][0])+abs(2-pos[0][1]))