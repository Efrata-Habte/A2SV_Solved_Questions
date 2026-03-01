t=int(input())

def solve():
    current=input()

    if "**" in current or "><" in current or "*<" in current or ">*" in current:
        return -1
    else:
        left=current.count('<')
        right=current.count('>')
        ast=current.count('*')
        return max(left,right)+ast

for _ in range(t):
    print (solve())