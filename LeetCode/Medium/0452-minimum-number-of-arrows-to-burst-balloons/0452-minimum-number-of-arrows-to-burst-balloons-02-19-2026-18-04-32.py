class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0],x[1]))
        print(points)
        count=0
        prev=[]

        for i,j in points:
            if prev:
                if (i<=prev[1]) or (j<=prev[1]):
                    prev[0],prev[1]=max(prev[0],i),min(prev[1],j)
                    continue
                else:
                    count+=1
                    prev[0]=i
                    prev[1]=j
            else:
                count+=1
                prev.append(i)
                prev.append(j)

        return count