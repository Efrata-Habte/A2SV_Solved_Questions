n= int(input())
games= list(map(int,input().split()))

total = n*(n+1)//2

print(total-sum(games))