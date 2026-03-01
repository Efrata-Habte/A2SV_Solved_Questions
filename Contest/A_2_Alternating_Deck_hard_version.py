t = int(input())

for _ in range(t):
    n = int(input())

    alice_w=1
    alice_b=0
    bob_w=0
    bob_b=0
    is_alice=False
    is_w=True
    is_b=False
    i=1
    curr=n-1
    while i<n-1:
        j=0
        if is_alice:
            while j<(i+1)+(i+2) and curr>0:
                if is_w:
                    alice_w+=1
                    is_w=False
                    is_b=True
                else:
                    alice_b+=1
                    is_b=False
                    is_w=True
                j+=1
                curr-=1
            is_alice=False

        else:
            while j<(i+1)+(i+2) and curr>0:
                if is_w:
                    bob_w+=1
                    is_w=False
                    is_b=True
                else:
                    bob_b+=1
                    is_b=False
                    is_w=True
                j+=1
                curr-=1
            is_alice=True
        i+=1
        if curr<0:
            break
    print(alice_w,alice_b,bob_w,bob_b)