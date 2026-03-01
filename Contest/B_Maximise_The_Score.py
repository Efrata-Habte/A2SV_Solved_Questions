t = int(input())

def maximise_the_score():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    max_score=0

    for i in range(0,2*n,2):
        max_score +=arr[i]
    
    return max_score

for _ in range(t):
    print(maximise_the_score())
