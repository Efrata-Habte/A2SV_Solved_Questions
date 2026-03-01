t=int(input())

for _ in range(t):
    rating = input()
    n=len(rating)
    i=0
    a=''
    _max=0
    while i<n:
        if rating[i] !="0" :
            a+= rating[i]
            i+=1
            while i<n and rating[i]=='0':
                a+=rating[i]
                i+=1
            
        if i<n and int(a) <int(rating[i:]):
            _max=i
        else:
            break

    if _max==0:
        print(-1)
    else:
        print(rating[:_max] + " "+ rating[_max:])    
     


