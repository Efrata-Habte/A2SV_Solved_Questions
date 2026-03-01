n,m = map(int,input().split())
nums1= list(map(int,input().split()))
nums2=list(map(int,input().split()))

answer=[]

p1=0
p2=0

while p1 < n and p2<m:
    if nums1[p1]<=nums2[p2]:
        answer.append(nums1[p1])
        p1+=1
    else:
        answer.append(nums2[p2])
        p2+=1

if p1<n:
    answer.extend(nums1[p1:])
elif p2<m:
    answer.extend(nums2[p2:])

for i in answer:
    print(i,end=" ")