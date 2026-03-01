n = int(input())
books = []

for _ in range(n):
    books.append(list(map(int,input().split())))

w,h = books[0]
prev = max(w,h)

i=0

while i<n:
    w,h = books[i]
    big= max(w,h)
    small = min(w,h)

    if big <=prev:
        prev=big
    elif small<=prev:
        prev=small
    else:
        break
    i+=1

if i==n:
    print ("YES")
else:
    print("NO")

'''
swapped = [False for i in range(n)]
i=0

while i<n-1:
    if books[i][1]>=books[i+1][1]:
        i+=1
        continue
    elif (books[i][0]>=books[i+1][1] and not swapped[i]):
        books[i][0],books[i][1]=books[i][1],books[i][0]
        swapped[i]=True
    elif (books[i][1]>=books[i+1][0] and not swapped[i+1] ):
        books[i+1][0],books[i+1][1]=books[i+1][1],books[i+1][0]
        swapped[i+1]=True
    elif (books[i][0]>=books[i+1][0] and not swapped[i] and not swapped[i+1] ):
        books[i][0],books[i][1]=books[i][1],books[i][0]
        books[i+1][0],books[i+1][1]=books[i+1][1],books[i+1][0]
        swapped[i]=True
        swapped[i+1]=True
    else:
        break 
    i+=1

if i<n-1:
    print("NO")
else:
    print("YES")

'''