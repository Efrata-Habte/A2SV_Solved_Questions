t=int(input())

for _ in range(t):
    n = int(input())
    
    if n<0:
        print("")
        continue
    if n==1:
        print(1,0)
        continue

    n=n-1
    alice=1
    bob=0
    is_alice=False
    is_zero=False
    i=1

    while n>0:
        curr=(4*i)+1
        if curr>n:
            curr=n
            n=0
            is_zero=True
        if is_alice:
            alice+= curr
            is_alice=False
        else:
            bob+=curr
            is_alice=True

        n-=curr
        i+=1

    print(alice,bob)




