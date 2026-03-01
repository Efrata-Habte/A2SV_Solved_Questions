from collections import Counter

n=int(input())
arr=input()
count= (Counter(arr))

def remainingLength(count,n):
    if len(count)==1:
        print(n)
    else:
        num1=count['1']
        num0=count['0']
        print(abs(num1-num0))

remainingLength(count,n)