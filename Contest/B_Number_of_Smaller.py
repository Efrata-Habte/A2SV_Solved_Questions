# n1,n2=map(int,input().split())
# arr1=list(map(int,input().split()))
# arr2=list(map(int,input().split()))
# k=0
# ans=[]
# for i,j in enumerate(arr2):
#     while k<n1:
#         if j<=arr1[k]:
#             break
#         k+=1
#     ans.append(k)
# print(" ".join(map(str,ans)))





















n,m = map(int,input().split())
num1=list(map(int,input().split()))
num2=list(map(int,input().split()))

p1=0
answer=[]

for i in range(m) :
    while p1<n:
        if num2[i] > num1[p1] :
            p1+=1
        else:
            break
        
    answer.append(p1)

for j in answer:
     print (j , end=" ")